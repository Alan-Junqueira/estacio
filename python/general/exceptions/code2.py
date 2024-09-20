def divide(x, y):
    try:
        result = x / y
        print(f"The answer is {result}")
    except ZeroDivisionError:
        print("You can't divide by zero!")
