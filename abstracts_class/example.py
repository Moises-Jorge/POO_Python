# pylint: disable-all
from abc import ABC, abstractmethod

class	ContaBancaria(ABC):
    def	__init__(self, titular:str = '', saldo:float = 0) -> None:
        self.__titular  = titular.title()
        self.__saldo    = saldo
    
    
    @property
    def titular(self) -> str:
        return  self.__titular
    @titular.setter
    def titutlar(self, novo_titular:str) -> None:
        if isinstance(novo_titular, str):
            self.__titular = novo_titular.title()
        else:
            print("Valor invalido!")
    
    
    @property
    def saldo(self) -> float:
        return self.__saldo
    @saldo.setter
    def saldo(self, novo_saldo:float) -> None:
        if isinstance(novo_saldo, (float, int)) and novo_saldo > 0:
            self.__saldo = novo_saldo
        else:
            print("Valor invalido!")
    
    
    @abstractmethod
    def calc_juros(self) -> float:
        """Metodo abstrato que sera implementado nas subclasses"""
        pass


class   ContaPoupanca(ContaBancaria):
    def calc_juros(self) -> float:
        return self.saldo * 0.05 # juros de 5%


class   ContaCorrente(ContaBancaria):
    def calc_juros(self):
        return self.saldo * 0.02 # juros de 2%


# Teste
poup = ContaPoupanca("Moises", 1000)
corr = ContaCorrente("Margareth", 1000)

print(f"Juros da poupanca: {poup.calc_juros()} Kz")
print(f"Juros da corrente: {corr.calc_juros()} Kz")
    