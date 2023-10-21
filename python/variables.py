nome = "Alan Junqueira"
print(nome)
print('name variable value = {}'.format(nome))
print(f'name variable value = {nome}')

# ? Multiple attribution
a, b = 1, 2
print("Before change")

print(f'Variable names: a={a}, b={b}')

# ? First trade
temp = a
a = b
b = temp
print("First change")
print(f'Variable names: a={a}, b={b}')

# ? Second trade
a, b = b, a
print("Second change")
print(f'Variable names: a={a}, b={b}')