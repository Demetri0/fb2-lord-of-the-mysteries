#!/usr/bin/env python3
"""
Генерирует context/index.md и context/sequences.md из fb2-файла.
Использует `claude -p` для анализа каждой главы.

Запуск:
    python3 generate_context.py

Прогресс сохраняется в context/.progress — можно прерывать и продолжать.
"""

import subprocess
import json
import sys
import os
import xml.etree.ElementTree as ET
from pathlib import Path

FB2_FILE = "Lord Of The Mysteries.fb2"
CONTEXT_DIR = Path("context")
INDEX_FILE = CONTEXT_DIR / "index.md"
SEQ_FILE = CONTEXT_DIR / "sequences.md"
PROGRESS_FILE = CONTEXT_DIR / ".progress"

NS = {"fb2": "http://www.gribuser.ru/xml/fictionbook/2.0"}

PROMPT_TEMPLATE = """Ты анализируешь главу из книги «Повелитель Тайн» (Lord of the Mysteries).

Глава: {chapter_title}
Том: {volume_title}

Текст главы:
{chapter_text}

Верни JSON строго в таком формате (без markdown, только JSON):
{{
  "summary": "одно предложение — самые ключевые события главы (макс 25 слов, на русском)",
  "seq_events": [
    "строка события если есть, иначе пустой массив"
  ]
}}

Для seq_events включай ТОЛЬКО события связанные с Последовательностями (Путями/Sequences):
- Reveal: когда раскрывается название Последовательности какого-либо уровня какого-либо Пути
- LevelUP: когда персонаж повышает свой уровень Последовательности (выпил/усвоил зелье)
- Вступление персонажа в Клуб Таро

Формат строки события: "Глава N — [Reveal/LevelUP/Join] описание"
Если событий нет — верни пустой массив [].
"""


def get_text(el, strip=True):
    """Рекурсивно извлекает текст из XML элемента."""
    parts = []
    if el.text:
        parts.append(el.text)
    for child in el:
        parts.append(get_text(child, strip=False))
        if child.tail:
            parts.append(child.tail)
    result = "".join(parts)
    return result.strip() if strip else result


def parse_chapters(fb2_path):
    """Возвращает список глав: [{num, title, volume_title, text}]"""
    tree = ET.parse(fb2_path)
    root = tree.getroot()

    # Найти body (без атрибута name — основное тело)
    body = None
    for b in root.findall("fb2:body", NS):
        if b.get("name") is None:
            body = b
            break
    if body is None:
        body = root.find("fb2:body", NS)

    chapters = []
    chapter_num = 0

    for volume in body:
        if volume.tag != f"{{{NS['fb2']}}}section":
            continue
        vol_title_el = volume.find("fb2:title/fb2:p", NS)
        vol_title = vol_title_el.text.strip() if vol_title_el is not None else ""

        for chapter in volume:
            if chapter.tag != f"{{{NS['fb2']}}}section":
                continue
            chapter_num += 1
            ch_title_el = chapter.find("fb2:title/fb2:p", NS)
            ch_title = ch_title_el.text.strip() if ch_title_el is not None else f"Глава {chapter_num}"

            # Собрать текст (без тега title)
            text_parts = []
            for child in chapter:
                tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
                if tag == "title":
                    continue
                text_parts.append(get_text(child))

            text = "\n".join(p for p in text_parts if p)
            # Обрезаем до ~3000 символов чтобы не перегружать контекст
            if len(text) > 3000:
                text = text[:3000] + "\n[...текст обрезан...]"

            chapters.append({
                "num": chapter_num,
                "title": ch_title,
                "volume_title": vol_title,
                "text": text,
            })

    return chapters


def call_claude(prompt):
    """Вызывает claude -p и возвращает текст ответа."""
    result = subprocess.run(
        ["qwen", prompt],
        capture_output=True, text=True, timeout=60,
        stdin=subprocess.DEVNULL
    )
    if result.returncode != 0:
        raise RuntimeError(f"claude error: {result.stderr[:200]}")
    return result.stdout.strip()


def load_progress():
    if PROGRESS_FILE.exists():
        return int(PROGRESS_FILE.read_text().strip())
    return 0


def save_progress(num):
    PROGRESS_FILE.write_text(str(num))


def find_skipped_chapters():
    """Возвращает множество номеров глав помеченных как '?' в index.md."""
    skipped = set()
    if not INDEX_FILE.exists():
        return skipped
    import re
    pattern = re.compile(r"- \*\*Глава (\d+)[^*]*\*\*: \?$")
    for line in INDEX_FILE.read_text(encoding="utf-8").splitlines():
        m = pattern.match(line)
        if m:
            skipped.add(int(m.group(1)))
    return skipped


def retry_skipped(chapters):
    """Перегенерирует только главы помеченные '?' в index.md."""
    skipped = find_skipped_chapters()
    if not skipped:
        print("Пропущенных глав не найдено.")
        return

    print(f"Найдено пропусков: {len(skipped)} — главы {sorted(skipped)}")

    # Читаем весь index.md
    content = INDEX_FILE.read_text(encoding="utf-8")

    seq_f = open(SEQ_FILE, "a", encoding="utf-8")

    try:
        for ch in chapters:
            if ch["num"] not in skipped:
                continue

            print(f"[retry] {ch['title']}...", end=" ", flush=True)

            prompt = PROMPT_TEMPLATE.format(
                chapter_title=ch["title"],
                volume_title=ch["volume_title"],
                chapter_text=ch["text"],
            )

            try:
                response = call_claude(prompt)
                clean = response.strip()
                if clean.startswith("```"):
                    clean = clean.split("```")[1]
                    if clean.startswith("json"):
                        clean = clean[4:]
                data = json.loads(clean)
                summary = data.get("summary", "").strip()
                seq_events = data.get("seq_events", [])
            except Exception as e:
                print(f"ОШИБКА: {e}")
                continue

            # Заменяем строку с ? на правильную
            import re
            old_line = re.compile(
                r"- \*\*" + re.escape(ch["title"]) + r"\*\*: \?"
            )
            new_line = f"- **{ch['title']}**: {summary}"
            content = old_line.sub(new_line, content)

            for event in seq_events:
                if event.strip():
                    seq_f.write(f"{event.strip()}\n")
            seq_f.flush()

            print("OK")

    finally:
        seq_f.close()

    INDEX_FILE.write_text(content, encoding="utf-8")
    print("\nГотово — index.md обновлён.")


def main():
    retry_mode = "--retry" in sys.argv

    print(f"Парсинг {FB2_FILE}...")
    chapters = parse_chapters(FB2_FILE)
    print(f"Найдено глав: {len(chapters)}")

    CONTEXT_DIR.mkdir(exist_ok=True)

    if retry_mode:
        retry_skipped(chapters)
        return

    start_from = load_progress()
    if start_from > 0:
        print(f"Продолжаем с главы {start_from + 1}")

    # Открываем файлы в append-режиме если продолжаем
    mode = "a" if start_from > 0 else "w"
    index_f = open(INDEX_FILE, mode, encoding="utf-8")
    seq_f = open(SEQ_FILE, mode, encoding="utf-8")

    if start_from == 0:
        index_f.write("# Index — Повелитель Тайн\n\n")
        seq_f.write("# Последовательности — Повелитель Тайн\n\n")

    current_volume = None

    try:
        for ch in chapters:
            if ch["num"] <= start_from:
                current_volume = ch["volume_title"]
                continue

            if ch["volume_title"] != current_volume:
                current_volume = ch["volume_title"]
                index_f.write(f"\n## {current_volume}\n\n")
                index_f.flush()

            print(f"[{ch['num']}/{len(chapters)}] {ch['title']}...", end=" ", flush=True)

            prompt = PROMPT_TEMPLATE.format(
                chapter_title=ch["title"],
                volume_title=ch["volume_title"],
                chapter_text=ch["text"],
            )

            try:
                response = call_claude(prompt)
                clean = response.strip()
                if clean.startswith("```"):
                    clean = clean.split("```")[1]
                    if clean.startswith("json"):
                        clean = clean[4:]
                data = json.loads(clean)
                summary = data.get("summary", "").strip()
                seq_events = data.get("seq_events", [])
            except Exception as e:
                print(f"ОШИБКА парсинга: {e}")
                summary = "?"
                seq_events = []

            index_f.write(f"- **{ch['title']}**: {summary}\n")
            index_f.flush()

            for event in seq_events:
                if event.strip():
                    seq_f.write(f"{event.strip()}\n")
            seq_f.flush()

            save_progress(ch["num"])
            print("OK")

    finally:
        index_f.close()
        seq_f.close()

    print(f"\nГотово!")
    print(f"  {INDEX_FILE}")
    print(f"  {SEQ_FILE}")
    if PROGRESS_FILE.exists():
        PROGRESS_FILE.unlink()


if __name__ == "__main__":
    main()
