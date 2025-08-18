# Exemplo: Gerenciador de Tarefas

## 📌 Descrição
Este mini-projeto implementa uma classe `Tarefa` e um `GerenciadorTarefas` para praticar conceitos básicos de POO em Python.

## 🧰 Conceitos aplicados
- Definição de classes
- Atributos de instância
- Métodos de instância
- Encapsulamento básico
- Composição (Gerenciador contendo várias tarefas)

## ▶️ Execução
```bash
python3 tarefa.py
```

## 📎 Exemplo de uso
```python
from tarefa import Tarefa, GerenciadorTarefas

t1 = Tarefa("Estudar POO", "Revisar classes e objetos em Python")
t2 = Tarefa("Praticar", "Fazer mini-projeto de tarefas")

ger = GerenciadorTarefas()
ger.adicionar_tarefa(t1)
ger.adicionar_tarefa(t2)
ger.listar_tarefas()
```
