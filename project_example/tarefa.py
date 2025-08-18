class Tarefa:
    def __init__(self, titulo: str, descricao: str):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "✅" if self.concluida else "❌"
        return f"{status} {self.titulo} - {self.descricao}"


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa: Tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        for t in self.tarefas:
            print(t)


if __name__ == "__main__":
    # Exemplo prático
    t1 = Tarefa("Estudar POO", "Revisar classes e objetos em Python")
    t2 = Tarefa("Praticar", "Fazer mini-projeto de tarefas")

    ger = GerenciadorTarefas()
    ger.adicionar_tarefa(t1)
    ger.adicionar_tarefa(t2)

    print("📋 Lista de Tarefas:")
    ger.listar_tarefas()
    t1.concluir()
    print("\n📋 Após concluir uma tarefa:")
    ger.listar_tarefas()
