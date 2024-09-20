Fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# ? Using functional programming, print only the even numbers.


def is_even(x): return x % 2 == 0


# * Solution 1
# ? Using filter
even_numbers = list(filter(is_even, Fibonacci))
print(even_numbers)

# * Solution 2
# ? Using list comprehension
even_numbers = [x for x in Fibonacci if is_even(x)]
print(even_numbers)

# * Solution 3
# ? Using for loop
even_numbers = []
for x in Fibonacci:
    if is_even(x):
        even_numbers.append(x)
print(even_numbers)

# * Solution 4
# ? Using for loop and range
even_numbers = []
for i in range(len(Fibonacci)):
    if is_even(Fibonacci[i]):
        even_numbers.append(Fibonacci[i])
print(even_numbers)

# * Solution 5
# ? Using for loop and enumerate
even_numbers = []
for i, x in enumerate(Fibonacci):
    if is_even(Fibonacci[i]):
        even_numbers.append(Fibonacci[i])
print(even_numbers)

# * Solution 6
# ? Using while loop
even_numbers = []
i = 0
while i < len(Fibonacci):
    if is_even(Fibonacci[i]):
        even_numbers.append(Fibonacci[i])
    i += 1
print(even_numbers)

# * Solution 7
# ? Using while loop and range
even_numbers = []
i = 0
while i < len(Fibonacci):
    if is_even(Fibonacci[i]):
        even_numbers.append(Fibonacci[i])
    i += 1
print(even_numbers)
