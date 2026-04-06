from pathlib import Path
import json

path = Path("favorite_number.json")

if path.exists():
    number = json.loads(path.read_text())
    print(f"I know your favorite number! It's {number}.")
else:
    try:
        number = int(input("What is your favorite number? "))
        contents = json.dumps(number)
        path = Path("favorite_number.json")
        path.write_text(contents)
    except ValueError:
        print("That is not a number.")
