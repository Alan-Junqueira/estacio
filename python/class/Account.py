class Account:
    def __init__(self, number, cpf, accountHolder, balance):
        self.number = number
        self.cpf = cpf
        self.accountHolder = accountHolder
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if (self.balance < value):
            print("Saldo insuficiente")
            return False
        self.balance -= value
        return True

    def transfer(self, accountToTransfer, value):
        if self.saldo < value:
            return ("Não existe saldo suficiente")
        else:
            accountToTransfer.deposit(value)
            self.balance -= value
        return ("Transferencia Realizada")

    def print_balance(self):
        print(
            f"number: {self.number} \n cpf: {self.cpf}\nsaldo: {self.balance}")


def main():
    c1 = Account(1, 1, "Joao", 1000)  # Objeto sendo instanciado
    print(f"Nome do titular da conta: {c1.accountHolder}")
    print(f"Número da conta: {c1.number}")
    print(f"CPF do titular da conta: {c1.cpf}")
    c1.deposit(300)
    withdraw = c1.withdraw(100)
    c1.print_balance()
    print(f"O saque foi realizado? {withdraw}")


# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual a "__main__".
# Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso,
# é um chamado ao método main do script

if __name__ == "__main__":
    main()
