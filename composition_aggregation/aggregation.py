# pylint: disable-all
# Na agregacao, a classe exterior continua existir mesmo que a classe principal for destruida
class   Professor:
    def __init__(self, nome:str = '') -> None:
        self.nome = nome.title()
    
    
    def ensinar(self) -> None:
        print(f"O professor {self.nome} esta ensinando.")


class   Escola:
    def __init__(self, nome:str = '') -> None:
        self.__nome = nome.title()
        self.__professores = Professor = [] # Lista de professores
    
    
    def add_professor(self, professor: Professor) -> None:
        self.__professores.append(professor)
    
    
    def listar_professores(self) -> None:
        print(f"Professores da escola {self.__nome}:")
        if self.__professores == []:
            print("A escola ainda esta sem professores!")
            return
        else:
            for prof in self.__professores:
                print(f"- {prof.nome}")


# Teste
p1 = Professor("Carlos")
p2 = Professor("Maria")

e1 = Escola("Futuro do Amanha")
e1.listar_professores()
e1.add_professor(p1)
e1.add_professor(p2)
e1.listar_professores()
p1.ensinar() # O professor continua existindo e ensinando mesmo sem a escola
