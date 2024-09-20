from functools import reduce
import operator


def sum(numbers):
    if not numbers:
        return 0
    first = numbers[0]
    rest = numbers[1:]
    return first + sum(rest)


print('ex1')
print(sum([2, 4, 6, 8, 10]))

print('ex2')
list = ["Ferrari"]
new_list = list + ["Porsche"]
print(new_list)

print('ex3')
print(operator.add(10, 20))

print('ex4')
print(reduce(operator.add, [10, 20]))
print(reduce(operator.concat, ["Learning reduce"]))
