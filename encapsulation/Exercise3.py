# pylint: disable-all
class   ContaBancaria:
    def __init__(self, titular:str = '', saldo:float = 0, senha:str = '') -> None:
        self.titular    = titular.title()
        self._saldo     = saldo
        self.__senha    = senha
    
    
    def depositar(self, valor:float) -> bool:
        if valor > 0:
            self._saldo += valor
            return True
        return False
    
    
    def sacar(self, valor:float, senha:str) -> bool:
        if 0 < valor <= self._saldo and senha == self.__senha:
            self._saldo -= valor
            return True
        return False
    
    
    def exibir_saldo(self) -> None:
        print(f"O saldo na sua conta eh: {self._saldo} Kz!")


# Teste