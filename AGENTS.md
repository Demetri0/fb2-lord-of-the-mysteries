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

Чтобы не парсить весь fb2, используй готовые файлы в папке `context/`:

- `context/index.md` — краткое описание каждой из 1432 глав (одно предложение на главу), сгруппировано по томам. Используй для навигации по сюжету и поиска нужной главы.
- `context/sequences.md` — хронологический лог ключевых событий связанных с Последовательностями (Путями): раскрытие названий уровней (`Reveal`), повышения персонажей (`LevelUP`), вступления в Клуб Таро (`Join`).

`generate_context.py` — скрипт которым эти файлы были сгенерированы (использует `qwen` CLI).

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
├── assets // Resources used for landing page (index.html)
│   ├── bg.mp4
│   ├── bg.webm
│   ├── favicon.png
│   ├── og-image.jpg
│   └── poster.webp
├── CHANGELOG.md
├── epub // Ignore this folder it was attempt to convert fb2 to epub, so it is outdated output not sources
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
├── reader.html    // Browser-based fb2 reader (serve with python3 -m http.server 8080)
├── generate_context.py // Script to regenerate context/ files using qwen CLI
└── context/
    ├── index.md       // One-line summary per chapter (all 1432 chapters)
    └── sequences.md   // Chronological log of Sequence-related events

```
