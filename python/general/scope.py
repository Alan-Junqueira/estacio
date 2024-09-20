def multiplicador(numero):
    a = 2  # esta variável tem escopo local
    print(f"Inside function, variable a value: {a}")
    return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"Outside function, variable a value: {a}")

###


def multiplicador(numero):
    return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"B variable value: {b}")

###


def multiplicador(numero):
    global a  # todas as referências à variável a são para a global
    a = 2      # a global será alterado
    print(f"Inside function, variable a value: {a}")
    return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"B variable value: {b}")
print(f"Outside function, variable a value: {a}")
