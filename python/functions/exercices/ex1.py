vehicles = ["airplane", "car", "ship", 'bus']

# ? Using functional programming, transform vehicles to uppercase.

# * Solution 1
# ? Using map
vehicles_upper = list(map(lambda x: x.upper(), vehicles))

# * Solution 2
# ? Using list comprehension
vehicles_upper = [x.upper() for x in vehicles]

# * Solution 3
# ? Using for loop
vehicles_upper = []
for x in vehicles:
    vehicles_upper.append(x.upper())

# * Solution 4
# ? Using for loop and range
vehicles_upper = []
for i in range(len(vehicles)):
    vehicles_upper.append(vehicles[i].upper())

# * Solution 5
# ? Using for loop and enumerate
vehicles_upper = []
for i, x in enumerate(vehicles):
    vehicles_upper.append(vehicles[i].upper())
