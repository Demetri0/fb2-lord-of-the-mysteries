#!/usr/bin/env python3
"""
Заменяет указанную главу в книге Lord Of The Mysteries.fb2

Использование:
    python replace_chapter.py <номер_главы> <файл_с_главой>

Примеры:
    python replace_chapter.py 1001 chapter_1001_edited.xml
    python replace_chapter.py 1001 chapter_1001.xml --backup

С опцией --backup создаётся резервная копия оригинальной главы.
"""

import sys
import shutil
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

# Карта томов: (номер_главы_начала, номер_главы_конца, номер_тома)
TOMES = {
    1: (1, 213),
    2: (214, 482),
    3: (483, 732),
    4: (733, 946),
    5: (947, 1150),
    6: (1151, 1266),
    7: (1267, 1353),
    8: (1354, 1394),
}

FB2_NS = '{http://www.gribuser.ru/xml/fictionbook/2.0}'
XLINK_NS = '{http://www.w3.org/1999/xlink}'


def find_tome(chapter_num: int) -> int:
    """Находит номер тома по номеру главы."""
    for tome, (start, end) in TOMES.items():
        if start <= chapter_num <= end:
            return tome
    raise ValueError(f"Глава {chapter_num} не найдена в доступных томах (1-1394)")


def get_local_index(chapter_num: int, tome: int) -> int:
    """Вычисляет локальный индекс главы внутри тома."""
    start_chapter = TOMES[tome][0]
    return chapter_num - start_chapter + 1


def load_chapter_from_file(file_path: Path) -> ET.Element:
    """Загружает главу из XML файла."""
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Ищем первую section внутри body
    body = root.find(f'{FB2_NS}body')
    if body is not None:
        section = body.find(f'{FB2_NS}section')
        if section is None:
            raise ValueError(f"В файле {file_path} не найдена <section> внутри <body>")
        # Возвращаем глубокую копию, чтобы не было проблем с пространствами имён
        return ET.fromstring(ET.tostring(section, encoding='unicode'))
    
    # Если body нет, ищем section напрямую
    section = root.find(f'{FB2_NS}section')
    if section is None:
        raise ValueError(f"В файле {file_path} не найдена <section>")
    
    return ET.fromstring(ET.tostring(section, encoding='unicode'))


def replace_chapter(chapter_num: int, new_chapter_file: str, create_backup: bool = False) -> None:
    """Заменяет главу в FB2 файле."""
    fb2_path = Path(__file__).parent / "Lord Of The Mysteries.fb2"
    
    if not fb2_path.exists():
        raise FileNotFoundError(f"Файл книги не найден: {fb2_path}")
    
    new_chapter_path = Path(new_chapter_file)
    if not new_chapter_path.exists():
        raise FileNotFoundError(f"Файл главы не найден: {new_chapter_path}")
    
    tome = find_tome(chapter_num)
    local_index = get_local_index(chapter_num, tome)
    
    # Создаём резервную копию если нужно
    if create_backup:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = fb2_path.parent / f"Lord Of The Mysteries.backup.{timestamp}.fb2"
        shutil.copy2(fb2_path, backup_path)
        print(f"Резервная копия создана: {backup_path}")
    
    # Загружаем новую главу
    new_chapter = load_chapter_from_file(new_chapter_path)
    
    # Загружаем книгу
    tree = ET.parse(fb2_path)
    root = tree.getroot()
    
    # Находим тело книги
    body = root.find(f'{FB2_NS}body')
    if body is None:
        raise ValueError("Не найдено <body> в FB2 файле")
    
    # Находим том
    tomes = body.findall(f'{FB2_NS}section')
    if tome > len(tomes):
        raise ValueError(f"Том {tome} не найден (всего томов: {len(tomes)})")
    
    tome_section = tomes[tome - 1]
    
    # Находим главу
    chapters = tome_section.findall(f'{FB2_NS}section')
    if local_index > len(chapters):
        raise ValueError(f"Глава {local_index} не найдена в томе {tome}")
    
    old_chapter = chapters[local_index - 1]
    
    # Заменяем главу: создаём новую и заменяем старый узел
    chapter_index = list(tome_section).index(old_chapter)
    tome_section.remove(old_chapter)
    tome_section.insert(chapter_index, new_chapter)

    # Регистрируем пространства имён, чтобы избежать префиксов ns0, ns1
    ET.register_namespace('', 'http://www.gribuser.ru/xml/fictionbook/2.0')
    ET.register_namespace('l', 'http://www.w3.org/1999/xlink')

    # Сохраняем книгу
    ET.indent(tree, space='  ')
    tree.write(fb2_path, encoding='UTF-8', xml_declaration=True)
    
    print(f"Глава {chapter_num} успешно заменена из {new_chapter_file}")


def main():
    if len(sys.argv) < 3:
        print("Использование: python replace_chapter.py <номер_главы> <файл_с_главой> [--backup]")
        print("Пример: python replace_chapter.py 1001 chapter_1001_edited.xml")
        sys.exit(1)
    
    try:
        chapter_num = int(sys.argv[1])
    except ValueError:
        print(f"Ошибка: '{sys.argv[1]}' не является числом")
        sys.exit(1)
    
    new_chapter_file = sys.argv[2]
    create_backup = '--backup' in sys.argv
    
    try:
        replace_chapter(chapter_num, new_chapter_file, create_backup)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
