favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}

for user, language in favorite_languages.items():
    print(f"{user.title()}'s favorite_language is {language.title()}.")

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages.get(name, "").title()
        print(f"\t{name.title()}, I see you love {language}!")

if "erin" not in favorite_languages.keys():
    print("Erin, please take your poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
