class ContaBancaria:
    def __init__(self, titular:str = '', saldo:float = 0.0) -> None:
        self.titular = titular.title()
        self.saldo = saldo


    def depositar(self, valor:float) -> None:
        if valor >= 0:
            self.saldo += valor
            print(f'Deposito de {valor} kz realizado na conta de {self.titular}.')
        else:
            print('Valor invalido')


    def sacar(self, valor:float) -> None:
        if self.saldo < valor:
            print(f'Saque de {valor} kz nao permitido! Saldo insuficiente')
        else:
            self.saldo -= valor
            print(f'Saque de {valor} kz realizado na conta de {self.titular}.')


    def mostrar_saldo(self) -> None:
        print(f'Saldo actual de {self.titular}: {self.saldo} kz.')


    def __str__(self) -> str:
        return f'Titular da conta: {self.titular}\nSaldo actual: {self.saldo}'

# Programa principal:
conta1 = ContaBancaria('Moises', 0)
conta2 = ContaBancaria('Margareth', 0)

conta1.depositar(1000)
conta1.sacar(500)
conta1.mostrar_saldo()
print()
conta2.depositar(2000)
conta2.sacar(2500)
conta2.mostrar_saldo()
