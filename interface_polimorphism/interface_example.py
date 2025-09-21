# pylint: disable-all
from abc import ABC, abstractmethod
class   Forma(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class   Quadrado(Forma):
    def __init__(self, lado:float = 0):
        self.lado = lado
    
    
    def area(self):
        return self.lado ** 2


class   Circulo(Forma):
    def __init__(self, raio:float = 0) -> None:
        self.raio = raio
    
    
    def area(self):
        return 3.14 * (self.raio ** 2)
    
    
# Teste
formas = [Quadrado(4), Circulo(3)]
for forma in formas:
    print(f"Area:{forma.area()}")
