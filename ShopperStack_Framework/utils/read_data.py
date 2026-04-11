import json
from pathlib import Path

# for reading the json file
def read_json(file_path):
    path = Path(file_path)

    if not path.is_absolute():
        root = Path(__file__).resolve().parent.parent
        root_path = root / file_path
        if root_path.exists():
            path = root_path
        elif path.exists():
            path = path
        else:
            path = Path.cwd() / file_path

    with open(path) as f:
        return json.load(f)