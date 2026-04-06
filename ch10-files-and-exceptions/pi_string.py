from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text().rstrip()

pi_string = ""
lines = contents.splitlines()
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
