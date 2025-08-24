class Pessoa:
    def __init__(self, nome: str = '', idade: int = 0, profissao: str = ''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def apresentar(self):
        print(f'Ola, meu nome eh {self.nome}, tenho {self.idade} anos e sou {self.profissao}.')

# Testando
# Criando os objectos:
p1 = Pessoa("Moises", 27, "Programador")
p2 = Pessoa("Margareth", 22, "Programadora")

p1.apresentar()
p2.apresentar()
