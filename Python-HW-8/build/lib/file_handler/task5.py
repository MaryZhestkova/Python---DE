import pickle
import json
from pathlib import Path


def json_to_pickle(path: Path) -> None:
    for file in path.iterdir():
        if file.is_file() and file.suffix == '.json':
            with open(file, 'r', encoding='utf-8') as f_read:
                data = json.load(f_read)
            with open(path / f'{file.stem}.pickle', 'wb') as f_writebyte:
                pickle.dump(data, f_writebyte)


if __name__ == '__main__':
    json_to_pickle(Path('/Users/mariyazhestkova/Desktop/Python_course/Python-HW-8/'))