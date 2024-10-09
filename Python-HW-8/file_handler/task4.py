import csv
import json
from pathlib import Path


def csv_to_json(csv_file: Path, json_file: Path) -> None:
    json_list = []
    with open(csv_file, 'r', encoding='utf-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_read):
            json_dict = {}
            if i != 0:
                level, id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = f'{int(id):010}'
                json_dict['name'] = name.title()
                json_dict['hash'] = hash(f"{json_dict['name']}{[id]}")
                json_list.append(json_dict)


    with open(json_file, 'w', encoding='utf-8') as f_write:
        json.dump(json_list, f_write, indent=2)


if __name__ == '__main__':
    csv_to_json(Path('/Users/mariyazhestkova/Desktop/Python_course/Python-HW-8/users.csv'), Path('/Users/mariyazhestkova/Desktop/Python_course/Python-HW-8/new_users.json'))
    