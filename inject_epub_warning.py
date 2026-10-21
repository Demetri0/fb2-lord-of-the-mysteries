#!/usr/bin/env python3
"""
Добавляет предупреждение об устаревшей версии вверх каждой страницы в epub/
и запрещает её индексацию поисковиками (meta robots noindex)

Предупреждение ведёт на ту же главу в актуальной веб-версии read/
(соответствие ищется по заголовку главы), а если глава не найдена — на оглавление.
Повторный запуск заменяет уже вставленное предупреждение, а не дублирует его.

Сначала нужно собрать read/ (см. build_read.py).

Использование:
    python inject_epub_warning.py
"""

import html
import re
import sys
from pathlib import Path

EPUB_DIR = Path("epub")
READ_DIR = Path("read")

BEGIN = "<!-- outdated-warning -->"
END = "<!-- /outdated-warning -->"

NOINDEX = '<meta name="robots" content="noindex"/>'

STYLE = (
    "margin:0 0 1em;padding:.75em 1em;border:1px solid #e0b84c;border-radius:6px;"
    "background:#fff3cd;color:#664d03;font-family:sans-serif;font-size:.95em;line-height:1.4"
)


def normalize(title: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", title))).strip()


def chapter_key(title: str) -> str:
    """Ключ для сопоставления: «Глава N», если есть, иначе весь заголовок.
    Названия глав могли поменяться при редактуре, а номер — нет."""
    m = re.match(r"Глава (\d+)\b", title)
    return f"Глава {m.group(1)}" if m else title


def read_pages() -> dict[str, tuple[str, str]]:
    """Возвращает {ключ: (файл, заголовок)} для страниц read/."""
    pages = {}
    for path in sorted(READ_DIR.glob("index*.xhtml")):
        m = re.search(r"<title>(.*?)</title>", path.read_text(encoding="utf-8"), re.S)
        if m:
            title = normalize(m.group(1))
            pages.setdefault(chapter_key(title), (path.name, title))
    return pages


def warning(target: tuple[str, str] | None) -> str:
    if target:
        file, title = target
        link = f'Актуальная версия этой главы: <a href="../read/{file}">{html.escape(title)}</a>'
    else:
        link = 'Актуальная версия книги: <a href="../read/">читать онлайн</a>'
    return (
        f'{BEGIN}<div class="outdated-warning" style="{STYLE}">'
        f"⚠ <strong>Это устаревшая версия книги</strong>, она больше не обновляется. {link}"
        f"</div>{END}"
    )


def main():
    if not (READ_DIR / "index.html").exists():
        sys.exit(f"Ошибка: {READ_DIR}/ не собрана, сначала запустите build_read.py")

    pages = read_pages()
    matched = unmatched = 0

    for path in sorted(EPUB_DIR.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), "", text, flags=re.S)
        if NOINDEX not in text:
            text = text.replace("<head>", "<head>\n    " + NOINDEX, 1)

        m = re.search(r"<h[1-3][^>]*>(.*?)</h[1-3]>", text, re.S)
        target = pages.get(chapter_key(normalize(m.group(1)))) if m else None
        if target:
            matched += 1
        else:
            unmatched += 1
            print(f"Не найдена глава для {path.name}, ссылка на оглавление")

        text, n = re.subn(r"(<body[^>]*>)", lambda b: b.group(1) + warning(target), text, count=1)
        if n == 0:
            print(f"Пропущен {path.name}: нет <body>")
            continue
        path.write_text(text, encoding="utf-8")

    print(f"Готово: {matched} со ссылкой на главу, {unmatched} со ссылкой на оглавление")


if __name__ == "__main__":
    main()
