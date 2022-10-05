# Lord Of The Mysteries

Данный проект осуществляет редакцию книги Повелитель Тайн, на русском языке.

Начат проект был, по причине того что мною не было найдено ни одного нормального,
полноценного перевода этой книги.
В сети присутствуют сайты с более-или-менее сносным форматированием **лишь некоторых** глав, однако переводом книги занималось множество разных людей в разное время, и каждый вносил свою *индивидуальность*.

Данный проект ставит перед собой 2 главных цели:
1. Привести форматирование диалогов, мыслей, и т.п. к единообразию;
2. Привести в порядок все наименования, которые часто переименовывались переводчиками.

p/s: На данный момент редакция ограничена 600 главами, пока не завершится их редактура
нет планов браться за оставшиеся 6 сотен.

## Help Wanted

Все желающие помочь — Добро Пожаловать! Буду рад любой помощи.

Взаимодействие осуществляется непосредственно через github.com, являющимся подходящей платформой
для подобных действий. Вы можете создавать issue, и описывать найденные вами ошибки, либо
присылать Pull Request-ы непосредственно с внесёнными вами правками.

Если вы никогда не работали с git/github то вам вероятно будет не просто,
я не буду вдаваться в подробности, самым простым способом будет воспользоваться [этой ссылкой](https://github.dev/Demetri0/fb2-lord-of-the-mysteries/), вам потребуется разобраться как [сделать Fork](https://github.com/Demetri0/fb2-lord-of-the-mysteries/fork) репозитория, сделать commit, а затем создать Pull Request.

Погуглите, статей в интернете много, например вот некоторые из них (Последние 2 самые полезные, рекомендую):
- https://www.dataschool.io/how-to-contribute-on-github/
- https://microsoft.github.io/workshop-library/short/intro-github-dev/
- https://gprivate.com/617ak
- https://gprivate.com/617ao

Если вы всё-же не осилили, использование GitHub для непосредственного редактирования,
то вы можете прислать то что вы отредактировали у себя локально, сюда в [issue](https://github.com/Demetri0/fb2-lord-of-the-mysteries/issues/new).
Это конечно потратит больше моего времени и уменьшит ценность вашей помощи, но всё же лучше чем ничего.

Если вы собираетесь делать всё по примерам уже отредактированных глав,
то ссылки ниже вам читать не обязательно, однако это может оказаться полезным.

- Вам может пригодится самое базовое понимания языка разметки (как вкладывать теги друг в друга и что за зверь такой эти теги) [XML](http://citforum.ru/internet/xmlxslt/xmlxslt.shtml)
- А так же полезно будет, ознакомиться с форматом [Fiction Book 2.0](http://gribuser.ru/xml/fictionbook/shema_comments.html)

**Для тех воистину прекрасных людей, которые таки решились и хотят помочь с редакцией:**

- Заголовки глав, которые на данный момент отформатированы неправильно, используются как маркер того что данная глава ещё не редактировалась;
- Если вы хотите взяться за редактирование:
	- Убедитесь, что выбранную вами главу ещё никто не редактировал [тут](https://github.com/Demetri0/fb2-lord-of-the-mysteries/pulls);
	- Делайте по одной главе и присылайте на каждую отдельный Pull Request;
	- Не беритесь исправлять имена/названия чего-либо, вы можете внести лишь дополнительный хаос, запишите где находится ошибка, что она из себя представляет и как по вашему мнению должно быть правильно и [создайте issue](https://github.com/Demetri0/fb2-lord-of-the-mysteries/issues/new) с описанием ошибки;
	- Используйте только те варианты форматирования что указаны в этом файле в разделе [Форматирование](#форматирование). Даже если оно не идеально, его нужно менять по всей книге, и если оно будет однообразно неправильно везде, то изменение этого займёт не более 10 минут, [создайте issue](https://github.com/Demetri0/fb2-lord-of-the-mysteries/issues/new) если вы считаете что какое-либо форматирование можно улучшить и опишите ваше видение;
	- Не беритесь исправлять что-либо во всём файле, есть высокая вероятность что кто-то другой может внести изменение в тот же самый участок текста из за чего возникнет конфликт, [создайте issue](https://github.com/Demetri0/fb2-lord-of-the-mysteries/issues/new) и опишите встреченную вами проблему.

## Специальные символы

| Symbol |   UTF  | Title    | Usage |
|--------|--------|----------|-------|
|    —   | U+2014 | EM DASH  | диалоги, разделение информации на предложения |
|    –   | U+2013 | EN DASH  | диапазон значений (например: 3–5) |
|    …   | U+2026 | Ellipsis | Многоточие |
|    «   | U+00AB | Left-Pointing Double Angle Quotation Mark | мысли персонажа |
|    »   | U+00BB | Right-Pointing Double Angle Quotation Mark | мысли персонажа |
|    “	 | U+201C | LEFT DOUBLE QUOTATION MARK | Значения в кавычках и прочее |
|    ”	 | U+201D | RIGHT DOUBLE QUOTATION MARK | Значения в кавычках и прочее |

## Форматирование:
### Заголовки разделов:
```xml
<section>
  <title><p>Том 1</p></title>
</section>
```

### Заголовки глав:
```xml
<title>
  <p>Глава 1 — Кроваво-красный</p>
</title>
```

### Повествование
```xml
<p>После серии неприятных ощущений, Чжоу Минжуй медленно собрал волю в кулак.</p>
```

### Мысли персонажа:
```xml
<p><emphasis>«Боль! Как больно! Как болит голова!»</emphasis></p>
<p><emphasis>«Она так заботится об отсталом братце?»</emphasis> — Чжоу Минжуй улыбнулся и кивнул — Хорошо.</p>
```

### Диалоги:
```xml
<p>— Клейн, не покупай много мяса и бобов</p>
<p>— Ясно, хорошо, — беспомощно ответил Чжоу Минжуй.</p>
```

### Музыкальные вставки

- Может обернуть в `<poem />`?

```xml
<p>♫ Монстры приснятся тебе.</p>
<p>♫ Драконы в твоих снах.</p>
```

### Любые надписи и то что написано (например на листочке)
Если это что-то что читает персонаж, то можно использовать вариант с мыслями персонажа,
но только в случае если это короткое предложение и не разбитое на абзацы.
Длинные же тексты лучше записывать через `<poem>`,
Вариант с цитатами можно просто оборачивать в кавычки.

- Может дополнительно оборачивать в `<code>`?
- Общение с Арродесом в виде приёмника пока не в счёт

```xml
<poem>
  <stanza>
    <v>Происходящее с баронетом Рафтером Пондом.</v>
  </stanza>
</poem>
```

### Примечания редактора:
```xml
<p>«Похоже, это как любовь Е Гун к дракону» <sup>(Прим. ред.: боязнь того, что нравится)</sup></p>
```


### О Тире и Дефисах:
- https://mts-vhod.ru/kak-pishetsya-diapazon-czifr-cherez-tire-ili-defis/


### Карта все Путей/Последовательностей
- [EN] https://lordofthemysteries.fandom.com/wiki/Pathways
- [ZH] https://lordofthemysteries.fandom.com/zh/wiki/%E6%AD%8C%E9%A2%82%E8%80%85%E9%80%94%E5%BE%84#%E5%BA%8F%E5%88%979_-_%E6%AD%8C%E9%A2%82%E8%80%85

### Ссылки на другие сайты с этой книгой

- https://ranobes.com/ranobe/134618-lord-of-the-mysteries.html (Вроде полный перевод)
- https://ifreedom.su/ranobe/povelitel-tajn/ (Вроде полный перевод)
- https://xn--80ac9aeh6f.xn--p1ai/povelitel-tayn/glava-546-duhovnyy-mir (Вроде полный перевод)
- https://jaomix.ru/category/povelitel-tajn/ (Полный перевод)
-
- https://ranobe.me/ranobe224 (Вроде полный перевод)
- https://ranobe-novels.ru/povelitel-tajn-veb-novella/ (Вроде полный перевод) (И перевод кажется гавно, но можно редактировать)
- https://ranobehub.org/ranobe/510-lord-of-the-mysteries (Кажется есть какая-то активность)
- https://ranobelib.me/lord-of-the-mysteries?section=info
- https://bloiteka.info/2021/02/09/cuttlefish-that-loves-diving-povelitel-tayn-01-povelitel-tayn.html
- https://aume.ru/6511-povelitel-tayn-glavy-400-625.html
- https://tl.rulate.ru/book/70038
- https://www.litlib.net/bk/144592/read
- https://loghorizont.ru/povelitel-tajn-3/
- https://librebook.me/povelitel_tain/vol3/64
- https://mangalib.me/lord-of-the-mysterious?section=chapters
