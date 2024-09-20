class Pessoa:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

pessoa1 = Pessoa('João', 'Rua 1')
pessoa2 = Pessoa('Maria', 'Rua 2')

print(f"Nome: {pessoa1.get_name()}, Endereço: {pessoa1.get_address()}")
print(f"Nome: {pessoa2.get_name()}, Endereço: {pessoa2.get_address()}")