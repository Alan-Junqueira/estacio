class Pessoa:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_weight(self, weight):
        self.weight = weight

    def set_height(self, height):
        self.height = height

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height

    def get_imc(self):
        return self.weight / (self.height * self.height)

    def get_category(self):
        imc = self.get_imc()
        if imc < 18.5:
            return 'Abaixo do peso'
        elif imc >= 18.5 and imc < 25:
            return 'Peso normal'
        elif imc >= 25 and imc < 30:
            return 'Sobrepeso'
        elif imc >= 30 and imc < 35:
            return 'Obesidade grau 1'
        elif imc >= 35 and imc < 40:
            return 'Obesidade grau 2'
        else:
            return 'Obesidade grau 3'
