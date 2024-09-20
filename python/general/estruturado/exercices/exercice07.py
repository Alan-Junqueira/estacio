# Implement a function that determine if the number is prime

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


print(is_prime(2))
