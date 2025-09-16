# pylint: disable-all
class	Motor:
    def	__init__(self, potencia:int = 0) -> None:
        self.potencia = potencia

    
    def ligar(self) -> None:
        print("Motor Ligado!")


class   Carro:
    def __init__(self, marca:str = '', modelo:str = '', potencia_motor: int = 0) -> None:
        self.__marca = marca.title()
        self.__modelo = modelo.title()
        self.motor = Motor(potencia_motor)
    
    
    def exibir_info(self) -> None:
        print(f"Marca: {self.__marca} {self.__modelo}, Motor: {self.motor.potencia} CV")
    
    
    def __str__(self) -> None:
        return f"Marca: {self.__marca} {self.__modelo}, Motor: {self.motor.potencia} CV"


# Teste
my_car = Carro("Toyota", "Corolla", 180)
my_car.exibir_info()
my_car.motor.ligar()
