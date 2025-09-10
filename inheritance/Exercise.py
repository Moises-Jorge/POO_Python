# pylint: disable-all
class	Veiculo:
    def __init__(self, marca:str = '', modelo:str = '') -> None:
        self.__marca = marca.title()
        self.__modelo = modelo.title()
        
        
    def exibir_info(self) -> str:
        print(f'Veiculo: {self.__marca} {self.__modelo}')
        
        
    def __str__(self) -> str:
        return (f'Veiculo: {self.__marca} {self.__modelo}')
        
        
class   Carro(Veiculo):
    def __init__(self, marca:str = '', modelo:str = '', portas:int = 0):
        super().__init__(marca, modelo)
        self.__portas = portas
        
        
    def exibir_info(self) -> str:
        super().exibir_info()
        print(f'Portas: {self.__portas}')
        
        
    def __str__(self) -> str:
        full_str = super().__str__() + f' com {self.__portas} portas'
        return (full_str)
        
        
# Testando a classe
my_car = Carro("toyota", "corolla", 4)
my_car.exibir_info()
#print('\n', my_car)
