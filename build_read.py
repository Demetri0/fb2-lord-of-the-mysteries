#!/usr/bin/env python3
"""
Собирает веб-версию книги в папке read/ из Lord Of The Mysteries.fb2

Конвертирует fb2 в epub3 через fbc (https://github.com/rupor-github/fb2cng),
распаковывает содержимое epub в read/, добавляет на страницы глав навигацию
(назад / оглавление / вперёд) и генерирует read/index.html с оглавлением.

Использование:
    python build_read.py [путь_к_fbc]

Примеры:
    python build_read.py
    python build_read.py ~/bin/fbc
    FBC=~/bin/fbc python build_read.py
"""

import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

FB2_FILE = Path("Lord Of The Mysteries.fb2")
READ_DIR = Path("read")

NAV_MARKER = "<!-- read-nav -->"


def convert(fbc: str, epub_file: Path):
    """Конвертирует fb2 в epub3."""
    subprocess.run(
        [fbc, "convert", "--to", "epub3", "--ow", "-o", str(epub_file), str(FB2_FILE)],
        check=True,
    )


def unpack(epub_file: Path):
    """Распаковывает OEBPS/ из epub в read/, предварительно очищая её."""
    if READ_DIR.exists():
        # read/ целиком генерируется этим скриптом, но на всякий случай
        # не удаляем папку, если она не похожа на результат его работы
        if any(READ_DIR.iterdir()) and not (READ_DIR / "nav.xhtml").exists():
            sys.exit(f"Ошибка: {READ_DIR}/ существует и не похожа на сгенерированную, не трогаю")
        shutil.rmtree(READ_DIR)
    READ_DIR.mkdir()

    with zipfile.ZipFile(epub_file) as z:
        for name in z.namelist():
            if not name.startswith("OEBPS/") or name.endswith("/"):
                continue
            target = READ_DIR / name[len("OEBPS/"):]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(name))

    # Сам epub тоже кладём рядом, чтобы его можно было скачать
    shutil.copy(epub_file, READ_DIR / "book.epub")


def spine_pages() -> list[str]:
    """Возвращает страницы книги в порядке чтения (spine из content.opf)."""
    opf = (READ_DIR / "content.opf").read_text(encoding="utf-8")
    hrefs = dict(re.findall(r'<item id="([^"]+)" href="([^"]+)"', opf))
    pages = [hrefs[i] for i in re.findall(r'<itemref idref="([^"]+)"', opf)]
    return [p for p in pages if re.fullmatch(r"index\d+\.xhtml", p)]


def page_info(page: str) -> tuple[str, bool]:
    """Возвращает заголовок страницы и признак того, что это страница тома (h1)."""
    text = (READ_DIR / page).read_text(encoding="utf-8")
    title = re.search(r"<title>(.*?)</title>", text, re.S).group(1).strip()
    return html.unescape(title), "<h1" in text


def add_navigation(pages: list[str]):
    """Добавляет на каждую страницу viewport и ссылки назад / оглавление / вперёд."""
    for i, page in enumerate(pages):
        path = READ_DIR / page
        text = path.read_text(encoding="utf-8")
        if NAV_MARKER in text:
            continue

        links = []
        links.append(f'<a href="{pages[i - 1]}">← Назад</a>' if i > 0 else "<span></span>")
        # "./", а не "index.html": некоторые серверы (например serve) редиректят
        # index.html на папку без слеша, и относительные ссылки оглавления ломаются
        links.append('<a href="./">Оглавление</a>')
        links.append(f'<a href="{pages[i + 1]}">Вперёд →</a>' if i + 1 < len(pages) else "<span></span>")
        nav = (
            f'{NAV_MARKER}<nav class="read-nav" style="display:flex;justify-content:space-between;'
            f'gap:1em;margin:1em 0;font-family:sans-serif">{"".join(links)}</nav>'
        )

        text = text.replace(
            "<head>",
            '<head><meta name="viewport" content="width=device-width, initial-scale=1"/>',
            1,
        )
        text = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + nav, text, count=1)
        text = text.replace("</body>", nav + "</body>", 1)
        path.write_text(text, encoding="utf-8")


def write_index(pages: list[str]):
    """Генерирует read/index.html с оглавлением по томам."""
    items = []
    in_volume = False
    for page in pages:
        title, is_volume = page_info(page)
        link = f'<a href="{page}">{html.escape(title)}</a>'
        if is_volume:
            if in_volume:
                items.append("</ol></details>")
            items.append(f"<details><summary>{link}</summary><ol>")
            in_volume = True
        else:
            items.append(f"<li>{link}</li>")
    if in_volume:
        items.append("</ol></details>")

    (READ_DIR / "index.html").write_text(
        f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Повелитель Тайн — Оглавление</title>
  <style>
    :root {{ color-scheme: light dark; }}
    body {{ max-width: 48em; margin: 0 auto; padding: 1em 16px; font-family: sans-serif; line-height: 1.5; }}
    summary {{ font-size: 1.2em; font-weight: bold; margin: .5em 0; cursor: pointer; }}
    ol {{ list-style: none; padding-left: 1em; }}
  </style>
</head>
<body>
  <h1>Повелитель Тайн</h1>
  <p><a href="book.epub">Скачать epub</a> · <a href="../">На главную</a></p>
  {"".join(items)}
</body>
</html>
""",
        encoding="utf-8",
    )


def main():
    fbc = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("FBC", "fbc")
    if not shutil.which(os.path.expanduser(fbc)):
        sys.exit(f"Ошибка: не найден fbc ({fbc}), укажите путь аргументом или в переменной FBC")

    with tempfile.TemporaryDirectory() as tmp:
        epub_file = Path(tmp) / "book.epub"
        convert(os.path.expanduser(fbc), epub_file)
        unpack(epub_file)

    pages = spine_pages()
    add_navigation(pages)
    write_index(pages)
    print(f"Готово: {len(pages)} страниц в {READ_DIR}/")


if __name__ == "__main__":
    main()
