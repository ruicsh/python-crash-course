favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}

people = ["jen", "rory", "james", "phil"]

for person in people:
    if person in favorite_languages.keys():
        print(f"Thanks, {person.title()}, for taking the poll.")
    else:
        print(f"{person.title()} please take the poll.")
