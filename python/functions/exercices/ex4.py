from functools import reduce
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ? Using functional programming, add up the elements in the list.

# * Solution 1
# ? Using reduce
sum_list = reduce(lambda x, y: x + y, number_list)
print(sum_list)

# * Solution 2
# ? Using for loop
sum_list = 0
for x in number_list:
    sum_list += x
print(sum_list)
