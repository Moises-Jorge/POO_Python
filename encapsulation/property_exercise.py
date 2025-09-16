# pylint: disable-all
class   Produto:
    def __init__(self, nome:str = '', preco:float = 0, estoque:int = 0) -> None:
        self.nome       = nome.title()
        self.__preco    = preco
        self.__estoque  = estoque
    
    
    @property
    def preco(self) -> float:
        return self.__preco
    @preco.setter
    def preco(self, novo_preco:float) -> None:
        if isinstance(novo_preco, (int, float)) and novo_preco > 0:
            self.__preco = novo_preco
        else:
            print("Preco invalido!")
    
    
    @property
    def estoque(self) -> int:
        return self.__estoque
    @estoque.setter
    def estoque(self, novo_estoque:int) -> None:
        if isinstance(novo_estoque, int) and novo_estoque >= 0:
            self.__estoque = novo_estoque
        else:
            print("Estoque invalido!")
    