class Carro:
    def __init__(self, marca: str = '', modelo: str = '', ano: int = 0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


    def mostrar_dados(self):
        """mostrar_dados(): metodo que mostra os detalhes do carro
		"""
        print(f'Carro: {self.marca} {self.modelo}, Ano: {self.ano}')

# criando um objecto (instancia) da classe Carro
carro1 = Carro("Toyota", "Corolla", 2020)

# Chamando um metodo do objecto
carro1.mostrar_dados()
