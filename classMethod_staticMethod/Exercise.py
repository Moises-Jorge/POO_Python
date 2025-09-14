# pylint: disable-all
class   Banco:
    taxa_juros = 0.05
    
    @classmethod
    def mudar_taxa(cls, nova_taxa:float) -> None:
        cls.taxa_juros = nova_taxa
    
    
    @staticmethod
    def calc_juros(valor:int) -> float:
        return valor * Banco.taxa_juros # Acedendo o atributo da classe com o nme da propria classe pq o metodo eh estatico, se fosse da classe, seria com o cls