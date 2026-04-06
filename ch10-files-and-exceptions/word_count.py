from pathlib import Path


def count_words(path):
    try:
        contents = path.read_text(encoding="utf-8").rstrip()
    except FileNotFoundError:
        pass
        # print(f"Sorry, the file {path} does not exit.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ["alice.txt", "siddharta.txt", "moby_dick.txt", "little_women.txt"]
for filename in filenames:
    path = Path(filename)
    count_words(path)
