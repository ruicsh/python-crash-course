from pathlib import Path

filenames = ["cats.txt", "dogs.txt"]
for filename in filenames:
    try:
        path = Path(filename)
        print(path.read_text().rstrip())
    except FileNotFoundError:
        pass
