from pathlib import Path

path = Path("alice.txt")
contents = path.read_text().rstrip()

count = 0
for line in contents.splitlines():
    count += line.lower().count("the ")
print(f"'the' appears {count} times.")
