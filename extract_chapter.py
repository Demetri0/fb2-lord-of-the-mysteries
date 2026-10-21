#!/usr/bin/env python3
"""
Извлекает указанную главу из книги Lord Of The Mysteries.fb2

Использование:
    python extract_chapter.py <номер_главы> [output_file]

Примеры:
    python extract_chapter.py 1001
    python extract_chapter.py 1001 chapter_1001.xml
"""

import sys
import xml.etree.ElementTree as ET
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


def extract_chapter(chapter_num: int) -> ET.Element:
    """Извлекает главу из FB2 файла."""
    fb2_path = Path(__file__).parent / "Lord Of The Mysteries.fb2"
    
    if not fb2_path.exists():
        raise FileNotFoundError(f"Файл книги не найден: {fb2_path}")
    
    tome = find_tome(chapter_num)
    local_index = get_local_index(chapter_num, tome)
    
    tree = ET.parse(fb2_path)
    root = tree.getroot()
    
    # Находим тело книги
    body = root.find(f'{FB2_NS}body')
    if body is None:
        raise ValueError("Не найдено <body> в FB2 файле")
    
    # Находим том (section с индексом tome)
    tomes = body.findall(f'{FB2_NS}section')
    if tome > len(tomes):
        raise ValueError(f"Том {tome} не найден (всего томов: {len(tomes)})")
    
    tome_section = tomes[tome - 1]
    
    # Находим главу (вложенная section с индексом local_index)
    chapters = tome_section.findall(f'{FB2_NS}section')
    if local_index > len(chapters):
        raise ValueError(f"Глава {local_index} не найдена в томе {tome} (всего глав в томе: {len(chapters)})")
    
    chapter_section = chapters[local_index - 1]
    
    return chapter_section


def main():
    if len(sys.argv) < 2:
        print("Использование: python extract_chapter.py <номер_главы> [output_file]")
        print("Пример: python extract_chapter.py 1001 chapter_1001.xml")
        sys.exit(1)
    
    try:
        chapter_num = int(sys.argv[1])
    except ValueError:
        print(f"Ошибка: '{sys.argv[1]}' не является числом")
        sys.exit(1)
    
    output_file = sys.argv[2] if len(sys.argv) > 2 else f"chapter_{chapter_num}.xml"
    
    try:
        chapter = extract_chapter(chapter_num)

        # Регистрируем пространства имён, чтобы избежать префиксов ns0, ns1
        ET.register_namespace('', 'http://www.gribuser.ru/xml/fictionbook/2.0')
        ET.register_namespace('l', 'http://www.w3.org/1999/xlink')

        # Создаём валидный XML с пространством имён
        root = ET.Element('{http://www.gribuser.ru/xml/fictionbook/2.0}FictionBook')
        root.set('xmlns:l', 'http://www.w3.org/1999/xlink')

        body = ET.SubElement(root, '{http://www.gribuser.ru/xml/fictionbook/2.0}body')
        body.append(chapter)

        tree = ET.ElementTree(root)
        ET.indent(tree, space='  ')

        tree.write(output_file, encoding='UTF-8', xml_declaration=True)
        print(f"Глава {chapter_num} успешно извлечена в {output_file}")
        
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
