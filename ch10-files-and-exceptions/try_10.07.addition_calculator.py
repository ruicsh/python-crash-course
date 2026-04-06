while True:
    try:
        first_number = int(input("What is the first number? "))
        second_number = int(input("What is the second number? "))
        sum = first_number + second_number
        print(sum)
    except ValueError:
        print("That is not a number.")
