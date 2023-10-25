# Implement a function that calculates the number factorial

def iterative_factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

def recursive_factorial(number):
    if number == 1 or number == 0:
        return 1

    return number * recursive_factorial(number - 1)

print(iterative_factorial(5))
print(recursive_factorial(5))