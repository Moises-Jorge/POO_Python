# pylint: disable-all
class	Animal:
    def	fazer_som(self) -> None:
        pass


class	Cachorro(Animal):
    def	fazer_som(self) -> str:
        return ("Au Au!")


class   Gato(Animal):
    def fazer_som(self) -> str:
        return ("Miau!")


# Testando
animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.fazer_som())