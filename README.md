# Lord Of The Mysteries

## Специальные символы

| Symbol | UTF-16 |  HTML   | Title    | Usage |
|--------|--------|---------|----------|-------|
|    —   | U+2014 | &mdash; | EM DASH  | диалоги, раздеение информации на предложения |
|    –   | U+2013 | &ndash; | EN DASH  | диапозон значений |
|    …   | U+2026 | &mldr;  | Ellipsis | Многоточие |
|    «   | U+00AB | &laquo; | Left-Pointing Double Angle Quotation Mark | мысли персонажа |
|    »   | U+00BB | &raquo; | Right-Pointing Double Angle Quotation Mark | мысли персонажа |
|    “	 | U+201C | &ldquo; | LEFT DOUBLE QUOTATION MARK | Значения в ковычках и прочее |
|    ”	 | U+201D | &rdquo; | RIGHT DOUBLE QUOTATION MARK | Значения в ковычках и прочее |

- Номиналом вверх - отрицательный
- 

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
<p><emphasis>«Она так заботитсяоб отсталом братце?»</emphasis> — Чжоу Минжуй улыбнулся и кивнул — Хорошо.</p>
```

### Диалоги:
```xml
<p>— Клейн, не покупай много мяса и бобов</p>
<p>— Ясно, хорошо, — беспомощно ответил Чжоу Минжуй.</p>
```

### Музыкальные вставка
Может обернуть в `<poem />`?
```xml
<p>♫ Монстры приснятся тебе.</p>
```

### Любые надписи и то что написанно (например на листочке)
Если это что-то что читает персонаж, то можно использовать вариант с мыслями персонажа,
но только в случае если это короткое предложение и не разбитое на абзацы.
Длинные же тексты лучше записывать через `<poem>`,
Вариант с цитатами можно просто оборачивать в ковычки.

- Может дополнительно оборачивать в `<code>`?
- Общение с Арродесом в виде приёмника пока не всчёт

```xml
<poem>
	<stanza>
		<v>Происходящее с баронетом Рафтером Пондом.</v>
	</stanze>
</poem>
```

### Приечания редактора:
```xml
<p>«Похоже, это как любовь Е Гун к дракону» <sup>(Прим. ред.: боязнь того, что нравится)</sup></p>
```

## Деньги Лоэн
- 1 фунт = 20 сул
- 1 сул = 12 пенсов

## Персонажи:
- **Чжоу Минжуй** - ГГ в исходном мире
	- Склонения:
		- Чжоу Минжуе
		- Чжоу Минжуя
		- Чжоу Минжую
- **Клейн Моретти** - ГГ в мире попаданца, он же "Шут" (Кляйн/Клей/Клэйн/Клайн)
- **Бенсон** - Брат Клейна Моретти
- **Мелисса** - младшая сестра Клейна Моретти
- **Велш** => **Уэлш** - Тот кто приобрёл дневник и один из трёх Кто работал с дневником Антигонов, убит вместе с Клейном
- **Франк** - домовладелец в первой хате Клейна Моретти
- **Венди Смирин** - владелица пекарни
- **Одри Холл** - подчинённая шута, она же "Справедливость" / "Судья" / "Джастис"
- **Элджер Уилсон** / **Алгер Вилсон** - подчинённый шута, он же "Висельник" / "Повешенный" / Alger Wilson
- **Форс Уолл** - приспешница мисс Справедливости, она же "Маг"
- **Розанна** - коллега Клейна
- **Старина Нил** / **Старый нил** - коллга Клейна
- **Мис Орианна** - козначей, коллега Клейна
- **Яркий??** - коллега Клейна (заменён на Роял)
- **Роял Рейден** - штатный член ночных ястребов (девушка)
- **Кенли Уайт** - неспрящая, штатный сотрудник ночных ястребов
- **Леонард Митчелл** - штатный сотрудник Ночных Ястребов, полуночный поэт 8 последовательности
- **Инс Зангвилл** - утративший контроль архиепископ сбежавший с артефактом `0-008`
- **Сика Трон** - Полуночная Поэтесса
- **Гавэйну** - учитель рукопашного боя Клейна (фехтования?)
- **Деррик Берг** - Из народа ночи он же "Солнце" / "Солнышко" / "Маленькое Солнышко" / "маленькое солнце" / "Крошка Солнце"
- **Цезимир** - Дьякон церкви богини вечной ночи, Крестет Цезимир («Меч Богини»)
- **Сиакам Локхарт** - Секретарь Герцога Негана, 5 последовательность, МИ-9
- **Дэн Смит** / Данн Смит - Капитан Ночных Ястребов в Охранной Компании Терновник
- **Розелл** / Рассел / Розель - предыдущий переселенец
- Мисс **Шерон** / Шэрон - телохранительницапЯ
- Змей Меркурия Уилл Ауцептин - Мальчик потерявший ногу которого лечил доктор
- **Элланд** - Капитан коробля на котором Клейн отплыл из Баклунда (Простой Элланд/ Справедливый?)
- **Джан Коттман** - дьякон Уполномоченных Карателей, мб Жан? Морской Король
- **Джимми Некер**
- **Виктор Коннорс** - "Сумасшедший Капитан"
- **Элен** / Элена - девушка похищенная для развлечений Демонессой Трейси
- **Мистер Дур**/Мистер Портал
- **Мистер Азик** - Мистер Консул Смерти империи Балам, учитель Клейна
- **Дракон Воображения Анквельт**
- **Ловиа Тиффани** -- член Совета Шести, Города Серебра, Пастырь

## Члены Клуба Таро
- **Шут** / Мистер Дурак - ГГ
- **Мир** / Мистер Уорлд - Твинк ГГ
- **Справедливость** / Мисс Джастис / Правосудие - Одри Холл
- **Висельник** / Повешенный - Элджер Уилсон
- **Солнце** / Солнышко - Деррик из города Серебра
- **Маг** - Фосс/ Фось / Фос, подруга Одри Холл и Сио Дерчи 
- **Луна** - Эмлин, вампир (Сангвин)
- **Отшельник** - Каттлея Жрец Тайн, Адмирал Звёзд / Звёздный Адмирал

## Организации:
- Ночные ястребы / Дозорные ночи / Ночные дозорные
- «Алая Перчатка» - кодовое названиее элитной команды Ночных Ястребов
- Церковь Вечной Богини == Церковь Богини Вечной Ночи?
- Алхимики Психологии (ранее: Психологические Алхимики)
- Разум Машины == Механизм Коллективного Разума ? / Машиной Разума === Разум Машины
- Аскетический Одрен Моисея (от него получена Ястребами формула Жрец Тайн №9) (Орден Аскетов Моисея)
- Орден Сумеречных Отшельников - тайная организация желающая призвать Истинного Творца? / Орден Сумеречных Отшельников рассматривает Падшего Создателя как своего врага
- 
- Нспз - аббревиатуры должны быть uppercase (Национального Совета Природного Здравоохранения)

## Языки:
- **Древний язык Фейсак/Фусак** - составляет основу алфавита северных континентов (Fossic eng.)
- **Древний язык Гермес** - ???
- **Хелленс** - язык относящийся к поклонению и молитвам

## Свечение Братства Чистого Света
- **Венитане** - Жёлтое Свечение
- **?** - Красное Свечение (Точно не **Нанид**)

## Артефакты:
- **Скрижаль Осквернения** / Богохульная Скрижаль - табличка с записями о зельях
- `1-?` - **Дневник Антигонов**, который переводил Клейн с товарищами
- `?-?` - **Ползучий голод** / Всепожирающий Глад / Извивающийся Глад / Пожирающий Голод  - перчатка, поглощает души и получает из них соответствующие способности и силы, если не кормить пожрёт душу владельца
- `?-?` - **«Голос Скверны»** - амулет созданный из уха
- `?-?` - **Свеча ментального ужаса** - была использована Клейном для убийства оригинальной сущьности Епископа Утравски
- `?-?` - **Алая Корона Луны** - создает в определенном диапазоне эффект полнолуния. Для тех, кто изголодался по крови, она станет своеобразным призывом к действию и потере самоконтроля.
- `1-063` - Зеркальце создаёт иллюзию
- `1-042` - 
- `0-008` - Похож на простое пере пишущее без чернил. Похищен падшим Архиепископом.
- `2-049` - Кукла, берущая людей под контроль.
- `2-030` - «Неисчерпаемый яд» искушает всех живых существ, заставляя чувствовать непреодолимую жажду и желание его выпить.
- `2-078` - «Дверь смерти».
- `2-111` - Зеркало дающее ответ на вопрос но играющее в игру "парвда или действие"
- `2-?` - **Брошь солнца** / Солнечная Брошь
- `2-081` - 2-091? Кольцо содержащие в себе силы шестой последовательности Пути Чтеца. Я различаю, распознаю и, главное, запоминаю и имитирую все Потусторонние силы, что я видел раньше
- `2-105` - «Похититель Кровеносных Сосудов» / "Венозный Вор" человек, у которого был этот артефакт, мог украсть чью-либо способность в определенном радиусе
- `?-?` - Трут Увеличивает харизму владельца и перенимает силы Потусторонних в радиусе 50м
- `3-217` - **Спиритическое зеркало**
- `3-625` - **Тканевая Кукла Несчастья** (3-06252 - опечатка?)
- `3-611` - **Пряди Волос Спокойствия**
- `3-782` - **Мутировавшая Священная Солнечная Эмблема**, обладает свойством успокаивать любые трупы в радиусе пятнадцати метров от себя. Но у неё есть недостаток – она действует и на обычных людей.
- `3-1328` - **«Хрустальный глаз»** - монокль без труда разглядывать духовные тела, а также призраков и прочих злых духов

### Уникальности
- Кубик Вероятности - Уникальность пути Монстра
- Арродес - предположительно Уникальность пути Провидца? (догадка)

## Шармы
- Сонный
- Заупокойный

## Достопримечательности:
- **Врат Чанис/Чанов/Ханис** - врата в штабе Ястребов
- **Университет Хой** - место выпуска Клейна Моретти
- **Королевство Лоэн/Лоен/Руен** - Королевство в котором происходит основное дйство начала книги
- **Тинген** / **Тенгон** / **Тингон** - город спавна ГГ
- **Южный Фенэто** - страна
- **Масин** - страна
- **Ланбург** - страна
- **Бэклэнд** - столица королевства Руен
- **Зоутлэнд-стрит** / Зойтленд / Зоутленд / Зутленд / Зойтлэнд / Зойтланд / Зоут… - улица, в 36 доме которой находится офис охранной компании Терновник
- **река Тассок** / река Туссак
- **Охранная комания Терновник** / охранную контору «Блэкторн»
- **Район Баклундского Моста** / Баклунд-Бридж
- **Минск-Стрит** / Минек-Стрит - Улица на которой находится дом сыщика Шерлока Мориарти (д.15 р. Шервуд/Червуд)
- **Город Серебра / Серебряный Град (City of Silver) - Место где проживает Деррик(Солнце)
- **Баклунд** / Бэкленд / Баклунод - Город проживания Одри Холл и Шерлока Мориарти
- **Даффодил-Стрит** - улица где находится дом Клейна, после первого переезда.
- **Гавань Банси/Бинси** / **Гавань Бинси(Бенси?)** (древн.) - место в море близ Бэклунда
- **Рорстед, Баям, Город Щедрости** / Щедроград
- **Триер** - город, сталица Интиса
- **Город Чудес Ливисейд**

## Божества:
- **Вечное палящее Солнце**
- **Повелитель Штормов** (Тиран - так называют его последователи мудрости и знаний)
- **Бог Мудрости и Знаний**
- **Богиня Ночи**
- **Богиня Земли**
- **Бог Войны**
- **Бог Пара и Машин** / **Бог Мастерства** / **Бог ремесла**

### Не совсем боги
- Калвети === Калветуа
- Бог Морей Кальветуа - дух действующий на архипелаге Рорстед

### Ангелы
- Еретик Амон
- Королева бедствий Кохинем
- Злой дух - предположительно Красный Ангел - Медичи
- Пожиратель Хвоста Уроборос
- Творец Чудес Заратул из дневника Розелла
- Адам, сын Создателя
- Гермес?
- Змей Судьбы - Уилл Осептин

## Карты Таро
1. Шут / Дурак / Безумец
2. Маг / Волшебник
3. Монархиня / Верховная жрица / Папесса
4. Императрица / Хозяйка
5. Император / Хозяин / Иepoфaнт / Bepxoвный жpeц
6. Влюблённые
7. Колесница / Повозка / Возничий
8. Справедливость / Правосудие
9. Отшельник / Старец / Искатель
10. Колесо Фортуны / Колесо судьбы
11. Сила
12. Повешенный / Висельник
13. Смерть
14. Умеренность / Воздержание
15. Дьявол
16. Башня / Разрушаемая башня / Сгоревший храм
17. Звезда
18. Луна / Сумерка
19. Солнце
20. Суд
21. Мир / Вселенная

## Зелья / Последовательности:
- Путешественник?

- Писарь?

- Чтец (Церковь Бога Знаний и Мудрости)
	- Эрудит №6
	- Хранитель Знаний / Детектив №7
	
- Учёный №9 (последовательность Розелла) / Эрудит? (Путём Эрудита - владает церковь бога пара и машин)
	- Археолог №8
	- Оценщик №7
	- Ремесленник / Механник (совр.) №6
	- Астромант / Астроном (совр.) №5
	- Алхимик №4
	- Знаток Тайн №3
	
- Путь Бурь
	- Моряк №9 / Жрец Шторма (древн.) / Матрос / Морехода
	- Благословенный Ветром №6
	- Певец Морей №5 / Певец Океанов
	- Сущность Катаклизма №4
	- Морской Король №3
	
- Божий Певец Заклинаний, Эйс Снейк
	
- Путь Церкви Вечного Палящего Солнца (Солнце)
	- Бард №9 - позволяет Потустороннему воодушевлять и усиливать себя и союзников своими песнями
	- Жрец Света №8 / Светлый проситель / Свет Просящим / Носитель света - Они могли применять заклинания и ритуалы из домена Солнца, которые очень эффективны против зомби и духов
	- Солнечный Первосвященник №7 / Высший Жрец Солнца
	- Священник света (древн.) / Солнечный священник - усиливала все заклинания и ритуалы домена Солнца
	- Нотариус №5/№6?
	- Незапятнанный тенью №4 / Неомрачённый / Незатенённый

- Путь Великана «Охотник на демонов» / Путь гиганта / Божественный воин крови / Гигант - Владеет мир ночи и Церковь Бога Битвы
	- Воин №9
	- Гладиатор / Борец / Боксёр №8 (Варвар? - врядли, пересекается с другим путём)
	- Мастер орижия №7
	- Паладин Рассвета №6 / Рассветный паладин
	- Страж №5
	- Охотник на демонов №4
	
- Искателем Тайн №9 - Владеет орден Авроры
	- Слушатель №8
- Проситель [секретов] №9 (Жрец Тайн) / Тайный Проситель
	- Шепчущий №8 / Слушатель?
	- Теневой Подвижник №7 / Теневой Аскет (Орден Авроры/Епископ розы) (Теневой Подвижник правильнее)
	- Священник Роды №6
	- Пастырь №5 - способен поглощать чужие души включая приведений и злых духов и использовать их навыки
	- Угодником Тайн?
- Жнец тайн №9 (Чернокнижник? / Проситель тайн?) - Владеет Аскетический орден Моисея
	- Ученый Ближнего Боя
- зелья Тайного Жреца (п.п. Mystical Pryer === Проситель? == Жрец тайн? Тайный Мудрец?
	- Чернокнижник
	- Читающий Свитки
	- Мистик №4
	- Мастер Созвездий №5 (Астроном??? другой путь?)
	
- Магистр Мистицизма

- Зритель/Аудитория №9 - Этот Путь происходит от расы Драконов (путь Дракона) (путь Мечтателя??)
	- Телепат №8
	- Психиатр / Психоаналитик (древн.) №7
	- Зоркий №2 / Распознаватель
	- Автор №1
	- Визионер №0 / Мечтатель
	
- Ученик №9
	- Мастер Уловок №8 / Трикмастер / Мастер трюков / Трюкач
	- Астролог №7
	
- Арбитр №9 - Арбитры выглядят очень убедительно и властно, к тому же обладают выдающимися способностями к бою, и всегда готовы встретить любую неожиданность»
	- Шериф №8
	- Дознаватель №7 / Следователь
	
- Путь Луны
	- Аптекарь №9
	- Дресировщик №8 / Укротитель Зверей
	- Вампир №7
	- Профессор Зельеварения №6 / Кровавый Барон (вамп.) / Профессор Зелий
	- Алый Учёный №5 / Виконт (вамп.)
	- Король-Шаман №4

- Путешественник

- Пророк №4 (Prophet)

- Сущность Катаклизма №4 (Disaster's main sacrifice)

- Путь Зверя (Монстра) / Путь Колеса Фортуны
	- Монстр №9 - только Школа Мышления Жизни контролирует начало этого пути
	- Везунчик №7
	- Победитель №5
	- Советник Судьбы ?
	- Предсказатель №2 / Прорицатель
	- Змей Меркурий / Змей Меркурия / Змей Судьбы №1
	- Колесо Фортуны №0 ???

- Путь Бездны (древн.) / Путь Дьявола - секта освящения крови (<=> Мутант)
	- Преступник №9
	- Хладнокровный (древн.) №8 / Падший Ангел
	- Серийный убийца №7
	- Дьявол №6
	- Апостол Желаний №5

- Путь Мутанта - Школа Мысли Розы (<=> Бездна)
	- Заключённый №9
	- Сумасшедший №8
	- Оборотень №7
	- Зомби №6
	- Призрак №5
	- Марионетка №4
	
- Манипулятор №4 (Operator)

- Воин №8
- Охотник №8

- Заверитель Душ (Вероятно путь Моряка?)

- Провидец №9
  - Клоун №8
  - Фокусник №7 / Иллюзионист
  - Безликий №6
  - Марионеточник №5 / зелья Мастера Человеческих Марионеток
  - Чудотворец №2

- Народ Ярости №9
	
- Епископ Роз (Путь просителя тайн)

- Путь Темного Императора (названия должны соответствовать пути Демонессы, но с префиксами, Вместо Порочности — Порочный Барон, Смятения — Гуру Смятения, Падшей — Граф Падших, Хаоса — Принц Хаоса. -?- возможно перепутан с путём охотника)
	- Адвокат №9 / Юрист
	- Варвар №8
	- Взяточник №7 / Взяткодатель
	- Порочный Барон №6 / Барон Искажения
	- Гуру Смятения №5
	- Граф Падших №4
	- Неистовый Чародей №3
	- Герцог Беспорядка №2
	- Принц Хаоса №1
	- Темный Император №0

- Путь Красного Священника (Путь Заговорщика?) / Путь Охотника
	- Охотник №9
	- Провокатор №8
	- Пиромант №7 / Пироманьяк / Огненный Маг (древн.)
	- Заговорщик №6
	- Красный Жрец №0
	
- Путь Демонессы / Путь Ассасина
	- Убийца / Ассассин №9
	- Подстрекатель
	- Ведьма №7
	- Наслаждение №6 / Удовольствие
	- Демонесса Бедствий №5
	- ~~Демонесса~Наслаждения~№4~/~Демонесса~Удовольствий~~ --| ?????????? Леди Отчаяния / Демонесса Отчаяния
	- Вечно Юная Демонесса???
	
- Преступник №9

- Мародёр №9
	- Мошенник / Аферист №8

- Путь Смерти / Путь Феникса (древн.)
	- Сборщик трупов №9 
	- Копатель Могил / Гробокопатель №8 (Могильщик)
	- Духовный Медиум №7
	- Проводник Духов №6  (Духовный Наставник?/Духовная наставница)
	- Привратник №5
	- Консул Смерти????
	- Неумирающий

- Усмиритель Душ
- Паразит

- Путь Вечной Ночи
	- Бессонница №9 (Роял - бессонная, Кенли - бессонная) (Роял == Кенли?) (Бессонница === неспрящий?) (Вечной Ночи древн.)
	- Полуночный поэт №8
	- Ночной кошмар №7
	- Ночной страж №4

- Божий Певец Заклинаний - Эйс Снейк

- Фермер

## Другое
- Ритуал повышения удачи / Ритуал улучшения удачи / Ритуал изменения удачи
- «Закон Нерушимости Черт Потустороннего».

## Notes

- Чертой Человекоподобной Тени, ранее «Тень с человеческой кожей» Черта/Характеристика
- Исправить вхождения `— … —`
- архипелаг Аура к --- есть ли более удачное наименование?
- богохульной скрижалью => Скрижалью осквернения
- «Дейли Обсервер» - газета в которой работает репортёр Майк
- Священная клятва, данная Брошью «Солнца» -- одно из заклинаний надо проверить все совпадения
— Шут не из этой эпохи. Таинственный Властитель над серым туманом. Король в желтом и черном, любимец удачи… [п/п: Изменил мольбу, в дальнейшем буду использовать такой вариант]
- Карлсон === Карслон
- первородного Творца === Истинный Творец?
- Хвала Леди === Хвала Богини === Хвала Богини Вечной Ночи
- Законы Сохранения и Нерушимости Потусторонних Черт / нерушимость и сохранность Потусторонних Черт
- Законом Конвергенции Потусторонних Черт - Чем выше сила, тем больше притяжение
- Так как Инс был Ночным Хранителем пути Церкви Богини Вечной Ночи
- властелином ужаса - последовательность? Какой путь? Богиня вечной ночи, ястребы
- желто-белое свечение
- Королева Алой луны, Ауэрния
- Урагана Килангоса / Цилану
- Прикованный Бог
- Sanguine === Сангвин
- Арродес === Аррод
- Карту Ереси / Богохульную Карту
- Дракона Воображения, Анквельта
- Есть ли способ избавить от чужого влияния эссенцию Потустороннего?
- Дейси = Дейзи - Девочка прачки ЛиВ
ходимости Потусторонних Черт с одного и того же пути и чем выше их сила, тем сильнее притяжение
- Герман Спрэрроу == Герман Воробей - личина Клейна после событий в сталице
- На анлейте Смерть упоминалась не как «She», а как «He» в мужском роде. Я пока что сделала «Она», но будьте готовы к тому, что возможно в будущем Смерть будет «Он».
- Я заимел одну очень древнюю книгу. В ней упоминалось истинное имя Первородной Демонессы! Ее зовут Чик.
- спидлоудер
- Старый Куинн
- Баям === Байам
- Абсолютно Черное Око - Черта осквернённая создатилем, которой пользуется клейн для управления марионеткой
- — Поздравляю, мистер 4,200 фунтов -- локализовать цены
- Охотника с Тысячью лиц / Тысячеликого Охотника?
- Ловкого Мастера Розаго -- почему ловкого? О_о (Марионеточник?)
- голова короля была смотрела вверх -- тут должно быть про орёл/решка но я не помню какой из них положительный
- Клейн взял карту Темного Императора и поместил ее в свое Духовное Тело. -- духовное или астральное как было раньше? нуэно сделать консистентно
- Ядовитый флакон == Флакон С Ядом или как там его, тоже надо выровнять везде перевод
- "Это была Последовательность Жреца и его силы Света" -- Жреца? речь про тайного жреца или жреца пути света?
- Империи Трунсоэст
- Тело Души === Духовное Тело
- создавшим всё Господом -- речь о создателе, но не падшем, путаница задолбала
- Карта Ереси
- Похоже, собственно, на модель закона слияния признаков Потусторонних…
- стезя === путь
- признаки === Черты
- немертвых === нежити
- Джимми Накер === Никер
- признаков - Черт
- Своеобразия? - что это?
- Хлыст для Разума ? может переименовать в Хлыст Разума?
- барона-Кровниго === Кровового Барона?
- Бесноватым === Падшим Творцом?
- Змея Меркурия === Змей Меркурий
- Серебряном Граде === Городе Серебра
- Церкви Матери-Земли --- убрать тире
- мисс Автор === мисс Поэт --- Речь идёт про Сику Трон Которая скорее всего Полуночный Поэт, кроме того это создаёт ошибку т.к. Автор это 2 последовательность пути Зрителя
- формула незамутненного -- кого б@#ть?
- Ядро даже может быть в Нижнем Мире -- где блядь?
- Можете присоединяться, если у вас есть этот предмет --- фраза на значке Ланевуса
- Внутри Леонарда Митчелла поселился ангел из рода Зороэст

- Он потряс рукой и резко встряхнул ее -- про фигурку, удачный перевод вместо чего -то там с кистью

- Переводчики
- Ranobe Mania
- H1t3ki
- LinuxDemon
- I'm not sleeping
- Mad Hat
- Перевод от В1ЕЗК!.
- Перевод от ARLEKIN17 (From 545...)

- Автор: Cuttlefish That Loves Diving (爱潜水的乌贼)

Альтернативное название:
- Guǐmì Zhī Zhǔ
- LotM
- 诡秘之主
- 序列的戰
- 序列 的 戰爭
- ราชันโลกพิศวง
- ราชันเร้นลับ
- Quỷ bí chi chủ

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

Ему вспомнились слова Старины Нила. Бывший соратник Клейна однажды обмолвился, что четвертая последовательность Церкви Матери-Земли обладала большим потенциалом к алхимии. Четвертая же последовательность Пути Саванта, едва-ли могла похвастаться такой же способностью.


«9 ноября, похоже, что в Путях кроется секрет. Архиепископ Эстин сказал, что после становления Потусторонним пятой Последовательности, остальные Последовательности можно заменить другими из одного или даже двух Путей! Другими словами начиная от средней до высших Последовательностей! Но это ограничивается только теми же одним-двумя Путями. Если выбрать зелье не из того Пути, то самый лучший исход это – лёгкое сумасшествие и невозможность идти дальше».

«Таким образом, можно заменять Пути, начиная уже с четвёртой Последовательности. «Бессонный» и «Сборщик трупов». Да. «Послушник Церкви» и «Жрец Тайн» на высших ступенях тоже могут быть заменителями друг для друга».
