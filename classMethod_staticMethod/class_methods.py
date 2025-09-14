# pylint: disable-all
class	Produto:
    desconto = 0.10	# Atributo da classe (10% de desconto)
    
    def	__init__(self, nome:str = '', preco:float = 0) -> None:
        self.__nome = nome.title()
        self.__preco = preco
    
    
    def calc_preco_com_desconto(self,) -> float:
        return self.__preco * (1 - Produto.desconto)
    
    
    @classmethod
    def mudar_desconto(cls, novo_desconto) -> None:
        cls.desconto = novo_desconto # Modificando o atributo da classe


# Testando
p1 = Produto("Celular", 5000)
print(p1.calc_preco_com_desconto())
Produto.mudar_desconto(0.2)
print(p1.calc_preco_com_desconto())