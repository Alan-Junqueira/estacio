# Implement a function that returns the sum of all even numbers in a list

def is_even(number):
    return number % 2 == 0

def sum_even_numbers(list):
    result = 0

    for number in list:
        if is_even(number):
            result += number

    return result

print(sum_even_numbers([10, 2, 5, 7, 6, 3]))