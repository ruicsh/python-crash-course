def make_sandwich(*items):
    print("\nMaking a sandwich with:")
    for item in items:
        print(f" - {item}")


make_sandwich("cheese")
make_sandwich("chesse", "ham")
make_sandwich("cheese", "ham", "mayo")
