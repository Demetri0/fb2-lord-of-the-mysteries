---
name: regenerating-epub
description: Use when the fb2 book changed and the online version must be updated, when asked to rebuild or regenerate read/, book.epub or the epub/ folder, or when read/ pages, the reading theme, reader.js, the TOC or the outdated-epub banner need changes in this repository.
---

# Перегенерация read/ и epub/

## Overview

`read/` (веб-версия + `book.epub`) **целиком генерируется** из `Lord Of The Mysteries.fb2` скриптом `build_read.py`; `epub/` — старый вывод Calibre, который `inject_epub_warning.py` помечает устаревшим. Всё ручное живёт в исходниках:

| Что меняешь | Где править |
|-------------|-------------|
| Текст книги | `Lord Of The Mysteries.fb2` |
| Тема чтения | `assets/read-theme.css` |
| Прогресс, «Продолжить», sync/QR | `assets/read-reader.js` |
| Навигация, `<head>`, оглавление | `build_read.py` |
| Плашка в `epub/` | `inject_epub_warning.py` |

Файлы внутри `read/` руками не правят: следующая сборка удаляет папку.

## Процедура

1. **Ветка.** Работай не в `main`: `git switch -c <имя>`.

2. **fbc v1.9.4** ([fb2cng](https://github.com/rupor-github/fb2cng)). Тема завязана на его CSS-классы, другую версию не бери без проверки вывода. Если `~/bin/fbc` нет:
   ```bash
   d=$(mktemp -d) && mkdir -p ~/bin \
     && curl -sL -o "$d/fbc.zip" https://github.com/rupor-github/fb2cng/releases/download/v1.9.4/fbc-linux-amd64.zip \
     && unzip -q "$d/fbc.zip" fbc -d ~/bin && rm -rf "$d" && ~/bin/fbc --version
   ```

3. **Сборка, строго в этом порядке** (второй скрипт берёт ссылки из свежей `read/`):
   ```bash
   python3 build_read.py ~/bin/fbc
   python3 inject_epub_warning.py
   rm -f fbc.log   # fbc пишет лог в текущую папку
   ```

4. **Проверка:**
   ```bash
   xmllint --noout read/*.xhtml && echo XHTML_OK
   grep -L 'name="robots" content="noindex"' read/*.xhtml read/index.html epub/*.html | wc -l   # 0
   cmp assets/read-reader.js read/reader.js && cmp assets/read-theme.css read/theme.css
   git status --short | grep -v '^ M read/' ; git diff --stat | tail -1
   ```
   `inject_epub_warning.py` должен сообщить «1440 со ссылкой на главу, 1 со ссылкой на оглавление» (± новые главы).

5. **Сдвиг глав.** Файлы называются по порядку: `index00002.xhtml` = Глава 1. Сравни число страниц до и после (`ls read/index*.xhtml | wc -l`) и `git diff --stat -- read/`. Если глава вставлена или удалена **в середине** — имена после неё сдвинутся, и прогресс читателей (`localStorage`, ссылки `?sync=`) укажет не на ту главу. Скажи об этом пользователю до коммита. Главы в конце ничего не сдвигают.

6. **Только дата?** Если fb2 не менялся, изменятся лишь `read/content.opf` (`dcterms:modified`) и `read/book.epub` — откати их `git restore`, коммитить нечего.

7. **Посмотреть глазами:** `python3 -m http.server 4321` → `http://localhost:4321/read/`. Не используй `npx serve`: он режет `.html` и слеш в конце, и относительные ссылки ведут в корень (404).

8. **Коммит** в ветке, слияние в `main` и push — только когда пользователь попросит.

## Common Mistakes

| Ошибка | Последствие |
|--------|-------------|
| Правка в `read/` вместо `assets/` или `build_read.py` | Пропадёт при следующей сборке |
| `inject_epub_warning.py` до `build_read.py` | Ссылки из `epub/` на старые имена файлов |
| Забыт `rm fbc.log` | Мусор в `git status` (он в `.gitignore`, но удаляй) |
| Скрипт XHTML-страницы с расчётом на `defer` | Chrome игнорирует `defer` в XHTML — код запускается до `<body>` |
