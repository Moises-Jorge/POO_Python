# pylint: disable-all
class   Calculadora:
    @staticmethod
    def somar(a:int = 0, b:int = 0) -> int:
        return a + b
    
    
    @staticmethod
    def subtrair(a:int = 0, b:int = 0) -> int:
        return a - b


# Testando: Os metodos estaticos servem apenas como metodos auxiliares dentro das classe, nao dependem de atributos da classe e nem de instancia
c1 = Calculadora()
print(c1.somar(5, 3))
print(c1.subtrair(5, 3))