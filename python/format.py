hour = 10
minute = 15
second = 30

print(str(hour) + ' : ' + str(minute) + ' : ' + str(second))
print('{} : {} : {}'.format(hour, minute, second))
print(f'{hour} : {minute} : {second}')
print('{:4}, {:5}'.format(10, 100))
print('{:8.5}'.format(10/3))

seq = [0, 1, 2]
print(seq)

hello = 'Hello world!'
print(hello[0:4])
print(hello[2:8])
print(hello[::-1])
print(hello[8:2:-1])

L = [1,2,3,4,5,6,7,8]
print(L[::-1])