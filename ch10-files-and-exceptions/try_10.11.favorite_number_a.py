from pathlib import Path
import json

try:
    number = int(input("What is your favorite number? "))
    contents = json.dumps(number)
    path = Path("favorite_number.json")
    path.write_text(contents)

except ValueError:
    print("That is not a number.")
