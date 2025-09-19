# pylint: disable-all
from abc import ABC, abstractmethod

class	Veiculo(ABC):
    def __init__(self, marca:str = '', modelo:str = '', ano:int = 0) -> None:
        self.__marca    = marca.title()
        self.__modelo   = modelo.title()
        self.__ano      = ano
    
    
    @property
    def marca(self) -> str:
        return self.__marca
    @marca.setter
    def marca(self, nova_marca:str) -> None:
        if isinstance(nova_marca, str) and len(nova_marca) > 2:
            self.__marca = nova_marca.title()
        else:
            print("Marca invalida!")
            
            
    @property
    def modelo(self) -> str:
        return self.__modelo
    @modelo.setter
    def modelo(self, novo_modelo:str) -> None:
        if isinstance(novo_modelo, str) and len(novo_modelo) > 2:
            self.__modelo = novo_modelo.title()
        else:
            print("Modelo invalido!")
            
            
    @property
    def ano(self) -> int:
        return self.__ano
    @ano.setter
    def ano(self, novo_ano:int) -> None:
        if isinstance(novo_ano, int) and novo_ano > 0:
            self.__ano = novo_ano
        else:
            print("Ano invalido")
    
    
    @abstractmethod
    def tipo_combustivel(self) -> str:
        pass


class   Carro(Veiculo):
    def tipo_combustivel(self) -> str:
        return "Gasolina/Diesel"


class   Moto(Veiculo):
    def tipo_combustivel(self) -> str:
        return  "Gasolina"


#Teste
carro = Carro("Toyota", "Corolla", 1980)
moto = Moto("Honda", "H7", 2025)
print(f"Combustivel do carro: {carro.tipo_combustivel()}")
print(f"Combustivel da Moto: {moto.tipo_combustivel()}")
