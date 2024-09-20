number_list = [9.56783, 7.57568, 3.00914, 6.2321]
precision_list = [2, 2, 3, 3]

# ? Using functional programming, round number list values at the same order of precision list.

# * Solution 1
# ? Using map
rounded_list = list(map(lambda x, y: round(x, y), number_list, precision_list))
print(rounded_list)
