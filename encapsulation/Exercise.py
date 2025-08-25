class Carro:
    def __init__(self, marca:str = '', modelo:str = '', vel_max:int = 0):
        self.__marca = marca
        self.__modelo = modelo
        self.__vel_max = vel_max


    def get_marca(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.__marca
    def get_modelo(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.__modelo
    def get_vel_max(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return self.__vel_max


    def set_marca(self, nova_marca:str) -> None:
        """_summary_

        Args:
            nova_marca (str): _description_
        """
        self.__marca = nova_marca

    def set_modelo(self, novo_modelo:str) -> None:
        """_summary_

        Args:
            novo_modelo (str): _description_
        """
        self.__modelo = novo_modelo

    def set_vel_max(self, nova_velocidade:int) -> None:
        """_summary_

        Args:
            nova_velocidade (int): _description_
        """
        if nova_velocidade < 0:
            print ('Velocidade invalida!')
        else:
            self.__vel_max = nova_velocidade

    def __str__(self) -> str:
        return f'Carro: {self.__marca} {self.__modelo} com velocidade ate {self.__vel_max} Km/h'


# Programa principal
carro1 = Carro("Hyundai", "i10", 200)
carro1.set_vel_max(100)
print(carro1.get_vel_max())
