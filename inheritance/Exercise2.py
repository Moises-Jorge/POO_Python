# pylint: disable-all
class	Funcionario:
    def	__init__(self, nome:str = '', salario:float = 0) -> None:
        self.__nome = nome.title()
        self.__salario = salario
        
        
    def exibir_dados(self) -> None:
        print(f'Funcionario: {self.__nome}\nSalario: {self.__salario:.2f} Kz')
        
        
    def __str__(self) -> str:
        return f'Nome do funcionario: {self.__nome}\nSalario: {self.__salario:.2f} Kz'


class   Gerente(Funcionario):
    def __init__(self, nome:str = '', salario:float = 0, bonus:float = 0) -> None:
        super().__init__(nome, salario)
        self.__bonus = bonus
        
        
    def exibir_dados(self) -> None:
        super().exibir_dados()
        print(f'Bonus: {self.__bonus:.2f} Kz')
        
        
    def __str__(self) -> str:
        all_data = super().__str__() + f'\nBonus: {self.__bonus:.2f} Kz'
        return (all_data)


class   Estagiario(Funcionario):
    def __init__(self, nome:str = '', salario:float = 0, horas_trabalhadas:int = 0) -> None:
        super().__init__(nome, salario)
        self.__horas_trabalhadas = horas_trabalhadas
    
    
    def exibir_dados(self) -> None:
        super().exibir_dados()
        print(f'Horas Trabalhadas: {self.__horas_trabalhadas} horas')
    
    
    def __str__(self) -> str:
        all_data = super().__str__() + f'\nHoras Trabalhadas: {self.__horas_trabalhadas}'


# Testando
f1 = Funcionario("Carlos", 15000)
f1.exibir_dados()
print()
g1 = Gerente("Ana", 25000, 5000)
g1.exibir_dados()
print()
e1 = Estagiario("Martins", 5000, 8)
e1.exibir_dados()
