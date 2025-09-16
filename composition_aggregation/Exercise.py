# pylint: disable-all
class   Jogador:
    def __init__(self, nome_jogador:str = '') -> None:
        self.nome_jogador = nome_jogador.title()
    
    
    def jogar(self) -> None:
        print(f"O jogador {self.nome_jogador} esta jogando")


class   Estadio:
    def __init__(self, nome_estadio:str = '') -> None:
        self.nome_estadio = nome_estadio.title()
    
    
    def exibir_info(self) -> None:
        print(f"Nome do estadio: {self.nome_estadio}")


class   Time:
    def __init__(self, nome_time:str = '', nome_estadio:str = '') -> None:
        self.nome_time = nome_time.title()
        self.estadio = Estadio(nome_estadio)
        self.jogadores = []
    
    
    def add_jogador(self, jogador:Jogador) -> None:
        self.jogadores.append(jogador)
    
    
    def lista_jogadores(self) -> None:
        print(f"Jogadores do {self.nome_time}:")
        if self.jogadores == []:
            print("O time esta sem jogadores!")
            return
        else:
            for pos, jogador in enumerate(self.jogadores, 1):
                print(f"{pos} - {jogador.nome_jogador}")


# Teste
jog1 = Jogador("DeMoka")
jog2 = Jogador("Marcelo")

team = Time("Vivendas FC", "Estadio Pelado")
team.lista_jogadores()
print()
team.estadio.exibir_info()
team.add_jogador(jog1)
team.add_jogador(jog2)
team.lista_jogadores()

jog1.jogar()