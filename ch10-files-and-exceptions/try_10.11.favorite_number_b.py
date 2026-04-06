from pathlib import Path
import json


path = Path("favorite_number.json")
number = json.loads(path.read_text())
print(f"I know your favorite number! It's {number}.")
