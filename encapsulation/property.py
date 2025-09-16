# pylint: disable-all
class   Pessoa:
    def __init__(self, nome:str = '', idade:int = 0) -> None:
        self.__nome     = nome.title()
        self.__iadde    = idade
    
    
    
    @property
    def nome(self) -> str:
        """Getter para obter o nome"""
        return self.__nome
    @nome.setter
    def nome(self, novo_nome:str) -> None:
        """Setter para definir novo nome"""
        if isinstance(novo_nome, str) and novo_nome:
            self.__nome = novo_nome.title()
        else:
            print("Nome invalido!")
    
    
    @property
    def idade(self) -> int:
        """Getter para obter a idade"""
        return self.__iadde
    @idade.setter
    def idade(self, nova_idade:int) -> None:
        """Setter para validar a idade"""
        if isinstance(nova_idade, int) and nova_idade > 0:
            self.__iadde = nova_idade
        else:
            print("Idade invalida!")


# Teste
p1 = Pessoa("Carlos", 30)
print(p1.nome)
print(p1.idade)
p1.nome = 5
p1.idade = "35"
print(p1.nome)
print(p1.idade)
