import operator
from functools import partial
import collections

add_1 = partial(operator.add, 1)

print('ex1')
print(add_1(5))

print('ex2')
person = collections.namedtuple('Person', 'name age')
people = [person('John', 20), person('Jane', 30), person('Joe', 25)]

print(sorted(people, key=operator.attrgetter('name')))
print(sorted(people, key=operator.attrgetter('age')))

print('ex3')
sort_name = partial(sorted, key=operator.attrgetter('name'))
sort_age = partial(sorted, key=operator.attrgetter('age'))

print(sort_name(people))
print(sort_age(people))
