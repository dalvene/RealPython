while True:
    try:
        number = input("Enter an integer: ")
        number = int(number)
        break
    except ValueError:
        print("That is not an integer. Try again.")
print(number, "is an integer")
