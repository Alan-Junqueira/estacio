weight = eval(input('Write your weight: '))
height = eval(input('Write your height: '))

imc = weight / (height ** 2)

print(f"Your IMC is {imc:.2f}")
