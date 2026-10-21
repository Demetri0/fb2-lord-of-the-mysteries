# AGENTS.md

Данный проект осуществляет редакцию книги Повелитель Тайн, на русском языке.

Начат проект был, по причине того что мною не было найдено ни одного нормального, полноценного перевода этой книги.
В сети присутствуют сайты с более-или-менее сносным форматированием **лишь некоторых** глав, однако переводом книги занималось множество разных людей в разное время, и каждый вносил свою *индивидуальность*.

Данный проект ставит перед собой 3 главных цели:
- [x] Привести форматирование диалогов, мыслей, и т.п. к единообразию;
- [ ] Привести в порядок все наименования, которые часто переименовывались переводчиками; (70% done)
- [ ] Улучшить лаконичность и граммотность текста.

## Основная информация

Файл с текстом книги: `Lord Of The Mysteries.fb2` (29Mb);
Это fb2 (FictionBook) Книга в xml формате.
В файле `naming.md` находится много важной информации о названиях и именах в книге.
В файле `formatting.md` находится полезная информация по принятому форматированию.
В файле `index.html` можно посмотреть карту всех Последовательностей (классов способностей)

## Контекстные файлы для AI-агентов

Главные файлы для агентов — этот `AGENTS.md` и папка `.agents/` (скиллы в `.agents/skills/`). `CLAUDE.md` и `.claude/skills` только ссылаются на них (импорт и симлинк): новые инструкции и скиллы добавляй сюда, а не в `.claude`.

Чтобы не парсить весь fb2, используй готовые файлы в папке `context/`:

- `context/index.md` — краткое описание каждой из 1432 глав (одно предложение на главу), сгруппировано по томам. Используй для навигации по сюжету и поиска нужной главы.
- `context/sequences.md` — хронологический лог ключевых событий связанных с Последовательностями (Путями): раскрытие названий уровней (`Reveal`), повышения персонажей (`LevelUP`), вступления в Клуб Таро (`Join`).

`generate_context.py` — скрипт которым эти файлы были сгенерированы (использует `qwen` CLI).

## Скрипты

Все скрипты запускаются из корня репозитория (пути к файлам в них относительные).

| Скрипт | Для чего | Запуск |
|--------|----------|--------|
| `extract_chapter.py` | Достать одну главу из fb2 в отдельный XML-файл | `python3 extract_chapter.py 1001 [out.xml]` |
| `replace_chapter.py` | Вставить отредактированную главу обратно в fb2 | `python3 replace_chapter.py 1001 out.xml [--backup]` |
| `generate_context.py` | Пересоздать `context/index.md` и `context/sequences.md` | `python3 generate_context.py [--retry]` |
| `build_read.py` | Собрать веб-версию книги `read/` и `read/book.epub` | `python3 build_read.py путь/к/fbc` |
| `inject_epub_warning.py` | Пометить старый `epub/` устаревшим | `python3 inject_epub_warning.py` |

Браузерные (не запускаются из консоли):

| Файл | Для чего |
|------|----------|
| `reader.html` | Читалка fb2 прямо из репозитория: грузит `Lord Of The Mysteries.fb2` через `fetch`, поиск по главам, помнит главу в `localStorage`. Нужен HTTP-сервер: `python3 -m http.server 8080` |
| `assets/read-reader.js` | Логика `read/`: место чтения, прогресс, перенос на другое устройство. Копируется в `read/reader.js` |
| `assets/read-theme.css` | Тема `read/` для чтения. Копируется в `read/theme.css` |

### Как они работают

**`extract_chapter.py` / `replace_chapter.py`** — по глобальному номеру главы находят том по таблице `TOMES` (та же, что в разделе «Тома и диапазоны глав» ниже) и локальный индекс `<section>` внутри тома. `extract` пишет главу в файл (по умолчанию `chapter_N.xml`), `replace` подменяет `<section>` главы содержимым файла и перезаписывает fb2 целиком через ElementTree (после запуска проверь `git diff --stat`: изменения должны быть только в этой главе); с `--backup` перед этим рядом сохраняется копия всего fb2 `Lord Of The Mysteries.backup.<время>.fb2`. Удобная пара для правки одной главы без открытия 29-мегабайтного файла.

**`generate_context.py`** — парсит fb2, по каждой главе вызывает `qwen` с промптом «краткое содержание + события Последовательностей» и собирает ответы в `context/`. Прогресс пишется в `context/.progress`, поэтому прерванный запуск продолжается с места остановки; `--retry` повторяет главы, которые не удалось разобрать. Долгий: одна глава — один вызов LLM.

**`build_read.py`** — генерирует `read/` с нуля:
1. конвертирует fb2 в epub3 через `fbc` ([fb2cng](https://github.com/rupor-github/fb2cng), v1.9.4) и распаковывает `OEBPS/` в `read/` (папка удаляется и создаётся заново);
2. кладёт рядом `book.epub` для скачивания, копирует тему и скрипт из `assets/`;
3. на каждую страницу главы (`indexNNNNN.xhtml`, порядок из `content.opf`) добавляет `lang="ru"`, `noindex`, шрифт Lora, тему, `reader.js` и навигацию «Назад / Оглавление / Вперёд»;
4. генерирует `read/index.html` — русское оглавление по томам.

**`inject_epub_warning.py`** — в каждую страницу старого `epub/` (вывод Calibre 2023 года) вставляет `noindex` и плашку «Это устаревшая версия» со ссылкой на ту же главу в `read/`. Главы сопоставляются по номеру «Глава N» (названия с тех пор менялись), остальное — по точному заголовку. Блок обёрнут в `<!-- outdated-warning -->`, повторный запуск заменяет его, а не дублирует. Требует собранную `read/`.

**`assets/read-reader.js`** — хранит в `localStorage` (ключ `lotm-read:v1`) абзац у верхнего края экрана и список дочитанных страниц (дочитана = долистал до нижней навигации). В оглавлении рисует «Продолжить чтение», прогресс, отметки ✓ и кнопку «На другом устройстве»: ссылка `?sync=1.<стр>.<абзац>.<дочитана>.<битовая маска>` или QR-код (qrcode-generator 1.4.4 с cdnjs, грузится по клику, с SRI).

### Перегенерация read/ и epub/

Пошаговая инструкция с проверками — скилл `.agents/skills/regenerating-epub/SKILL.md`. Прочитай его перед пересборкой.

Главное: **`read/` целиком генерируется** — не правь файлы в ней, правь `build_read.py` и `assets/read-*`. Вставка или удаление главы в середине fb2 сдвигает имена файлов `indexNNNNN.xhtml` после неё, и сохранённый у читателей прогресс укажет не на ту главу.

## Доступные утилиты для работы с XML и др.

- `xmlstarlet`
- `xmllint`
- `jq`
- `pup`

## Тома и диапазоны глав (ТОЧНЫЕ ДАННЫЕ)

| Том | Название | Главы | XML-индекс |
|-----|----------|-------|------------|
| 1 | Джокер | 1-213 | (//f:body/f:section)[1] |
| 2 | Безликий человек | 214-482 | (//f:body/f:section)[2] |
| 3 | Путешественник | 483-732 | (//f:body/f:section)[3] |
| 4 | Бессмертный | 733-946 | (//f:body/f:section)[4] |
| 5 | Красный Жрец | 947-1150 | (//f:body/f:section)[5] |
| 6 | Искатель Света | 1151-1266 | (//f:body/f:section)[6] |
| 7 | Перевёрнутый человек / Висельник | 1267-1353 | (//f:body/f:section)[7] |
| 8 | Шут | 1354-1394 | (//f:body/f:section)[8

## Формула для извлечения главы

```bash
# Где N - глобальный номер главы
# Том определяется по таблице выше
# local = N - startChapter + 1

xmlstarlet sel -N f="http://www.gribuser.ru/xml/fictionbook/2.0" \
  -t -c "(//f:body/f:section)[TOM]/f:section[LOCAL]" \
  "Lord Of The Mysteries.fb2"
```

**Пример:** Глава 1001 находится в Томе 5 (главы 947-1150)
- local = 1001 - 947 + 1 = 55
- Команда: `(//f:body/f:section)[5]/f:section[55]`

## Структура файла книги Lord Of The Mysteries.fb2
```xml
<?xml version='1.0' encoding='UTF-8'?>
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink">
  <description>
    <title-info>
      <genre>antique</genre>
      <author>
        <first-name>Каракатица</first-name>
        <middle-name>Которая Любит</middle-name>
        <last-name>Нырять</last-name>
      </author>

      <book-title>Повелитель Тайн</book-title>
      <annotation>
        <p><strong>Повелитель Тайн</strong></p>
      </annotation>

      <keywords>боги, детектив, заклинания, мистика, оружие, перерождение в ином мире, переселение души,
        сверхъестественное, триллер, уровни</keywords>

      <coverpage>
        <image l:href="#cover"/>
      </coverpage>

      <lang>ru</lang>
    </title-info>
    <document-info>
      <author>
        <first-name>Demetrio</first-name>
        <middle-name/>
        <last-name/>
      </author>
      <date>12.09.2022</date>
      <id>622c9320-8de0-4af1-9900-c82d58183cc4</id>
      <version>1.0</version>
    </document-info>
  </description>

  <body>
    <section>
      <title>
        <p>Том 1 — Джокер</p>
      </title>

      <section>
        <title>
          <p>Глава 1 — Кроваво-красный</p>
        </title>

        <p><emphasis>«Боль!»</emphasis></p>
      </section>
    </section>

    <!-- SKIPPED SECTIONS -->

    <section>
      <title>
        <p>Том 8 — Шут</p>
      </title>

      <section>
        <title>
          <p>Глава 1354 — Эта ночь</p>
        </title>

        <p>Поздно ночью звон открывающихся дверей и окон разбудил Венделя от глубокого сна. Он осторожно скатился с кровати и осмотрел окрестности.</p>
      </section>
    </section>
  </body>

  <binary id="cover" content-type="image/jpeg">
    <!-- BINARY DATA -->
  </binary>
</FictionBook>
```

## Доступные файлы в проекте

```
$ls -la
total 29504
-rw-rw-r--  1 d3i0 d3i0     3914 Feb 21 02:16  AGENTS.md
drwxrwxr-x  2 d3i0 d3i0     4096 Oct  9  2023  assets/
-rw-rw-r--  1 d3i0 d3i0     1339 Apr  6  2024  CHANGELOG.md
drwxrwxr-x  2 d3i0 d3i0    69632 Dec  2  2023  epub/
-rw-rw-r--  1 d3i0 d3i0     1696 Jan 15  2025  feed.xml
-rw-rw-r--  1 d3i0 d3i0     4071 Feb 21 02:32  formatting.md
drwxrwxr-x  8 d3i0 d3i0     4096 Feb 21 02:17  .git/
drwxrwxr-x  3 d3i0 d3i0     4096 Jan 16  2025  .github/
-rw-rw-r--  1 d3i0 d3i0        8 Oct  8  2022  .gitignore
-rw-rw-r--  1 d3i0 d3i0       53 Apr  6  2024  google6450b993c468309f.html
-rw-rw-r--  1 d3i0 d3i0    49627 Jan 17  2025  index.html
-rw-rw-r--  1 d3i0 d3i0 29565393 Feb 19 23:45 'Lord Of The Mysteries.fb2'
-rw-rw-r--  1 d3i0 d3i0   182076 Aug 18  2025  naming.md
-rw-rw-r--  1 d3i0 d3i0   176578 Apr  6  2024  naming.old.md
-rw-rw-r--  1 d3i0 d3i0     5830 Jan 13  2025  notes.md
-rw-rw-r--  1 d3i0 d3i0    17182 Jan 13  2025  README.md
-rw-rw-r--  1 d3i0 d3i0    10233 Jan 14  2025  seq-events
drwxrwxr-x  4 d3i0 d3i0     4096 Jun 10  2025  .source/
-rw-rw-r--  1 d3i0 d3i0     1909 Jan 13  2025 'Sun Pathway.md'
```

```
$tree
.
├── AGENTS.md
├── assets // Resources used for landing page (index.html) and read/
│   ├── book/ // Book cover for feed.xml (cover.jpg + cover-thumb.jpg 300px), copied from the fb2
│   ├── bg.mp4
│   ├── bg.webm
│   ├── favicon.png
│   ├── og-image.jpg
│   ├── poster.webp
│   ├── read-reader.js // Source of read/reader.js (progress, continue, sync)
│   └── read-theme.css // Source of read/theme.css (reading theme)
├── CHANGELOG.md
├── epub // OUTDATED Calibre output (2023), kept online with an "outdated" banner + noindex. Not sources
│   ├── index.html
│   ├── index_split_001.html
│   ├── ...
│   ├── index_split_999.html
│   ├── page_styles.css
│   └── stylesheet.css
├── feed.xml
├── formatting.md
├── google6450b993c468309f.html
├── index.html     // Landing Page
├── Lord Of The Mysteries.fb2
├── naming.md      // Some chaotic user notes about namings in a book
├── naming.old.md  // Some outdated rambling user notes about namings in a book
├── notes.md       // Some chaotic user notes about book
├── README.md      // Some information about project
├── seq-events     // Attempt to collect information about key events in a book linked to chapters
├── Sun Pathway.md // Some notes about namings in Sun Pathway
├── read/          // GENERATED by build_read.py: current web version + book.epub. Never edit by hand
├── reader.html    // Browser-based fb2 reader (serve with python3 -m http.server 8080)
├── build_read.py          // Builds read/ from the fb2 via fbc
├── inject_epub_warning.py // Marks epub/ as outdated, links to read/
├── extract_chapter.py     // Extract one chapter to XML
├── replace_chapter.py     // Put an edited chapter back into the fb2
├── generate_context.py // Script to regenerate context/ files using qwen CLI
├── .agents/skills/   // MAIN location of agent skills (regenerating-epub: how to regenerate read/ and epub/)
├── .claude/skills -> ../.agents/skills // symlink for Claude Code, do not put files here
├── CLAUDE.md      // only imports AGENTS.md (@AGENTS.md), edit AGENTS.md instead
└── context/
    ├── index.md       // One-line summary per chapter (all 1432 chapters)
    └── sequences.md   // Chronological log of Sequence-related events

```
