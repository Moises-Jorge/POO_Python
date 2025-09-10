# pylint: disable-all
class ContaBancaria:
    def __init__(self, titular:str = '', saldo:float = 0) -> None:
        self.__titular = titular.title()
        self.__saldo = saldo
        
    
    def get_saldo(self) -> float:
        return (self.__saldo)
    
    
    def get_titular(self) -> str:
        return (self.__titular)
    
    
    def set_saldo(self, novo_saldo: float) -> bool:
        if novo_saldo > 0:
            self.__saldo = novo_saldo
            return True
        return False
    
    
    def depositar(self, valor:float) -> bool:
        if valor > 0:
            self.__saldo += valor
            return True
        return False
    
    
    def sacar(self, valor:float) -> bool:
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False
    
    
    def transferir(self, destino:"ContaBancaria", valor: float) -> bool:
        if 0 < valor <= self.__saldo:
            self.sacar(valor)
            destino.depositar(valor)
            return True
        return False
    
    
    def __str__(self) -> str:
        return (f'Titular: {self.__titular}\nSaldo: {self.__saldo:.2f} Kz')
    
    
# Programa Principal
conta1 = ContaBancaria("Julio", 2500)
conta2 = ContaBancaria("Ana", 4000)
conta2.set_saldo(500)

if conta2.transferir(conta1, 1000) == True:
    print(f'Transferencia efetuada com sucesso para a conta de {conta1.get_titular()}\n')
else:
    print('Erro na transferencia\n')
conta2.depositar(500)

print(conta1)
print(conta2)