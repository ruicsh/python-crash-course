numbers = list(range(1, 10))

ordinals = []
for n in numbers:
    if n == 1:
        ordinals.append("1st")
    elif n == 2:
        ordinals.append("2nd")
    elif n == 3:
        ordinals.append("3rd")
    else:
        ordinals.append(f"{n}th")

for ordinal in ordinals:
    print(ordinal)
