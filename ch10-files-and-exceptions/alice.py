from pathlib import Path

path = Path("alice.txt")
try:
    contents = path.read_text(encoding="utf-8").rstrip()
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exit.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
