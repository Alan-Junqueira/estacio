# Implement a solution that adds all even numbers in a list

list = [10, 2, 5, 7, 6, 3]
result = 0

for number in list:
    if number % 2 == 0:
        result += number

print(result)