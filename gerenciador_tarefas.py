"""
Modulo que implementa um gerenciador de tarefas
"""


from typing import NoReturn


lista_de_tarefas: list[dict[str]] = [
    {"prioridade": True, "tarefa": "Estudar Python"},
    {"prioridade": False, "tarefa": "Tomar banho"},
    {"prioridade": False, "tarefa": "Assistir série"},
]


def adicionar_tarefa(prioridade: bool, tarefa: str):
    """
    Adiciona uma tarefa na lista de tarefas
    Lança exceções caso a prioridade seja inválida ou a tarefa já exista

    Args:
        prioridade (bool): True se a tarefa tem prioridade alta, False caso contrário
        tarefa (str): string que representa a tarefa
    """
    if isinstance(prioridade, bool) :
        try:
            if isinstance(encontra_tarefa(tarefa), int):
                raise ValueError("Tarefa já existe")
        except ValueError as error:
            if error.args[0] == "Tarefa não existe":
                lista_de_tarefas.append({"prioridade": prioridade, "tarefa": tarefa})
                return
            else:
                raise
    else:
        raise ValueError("Prioridade inválida")

def remove_tarefas(índices: tuple[int]):
    """
    Remove várias tarefas da lista de tarefas de uma vez, dado uma tupla de índices
    Lança exceções caso a tarefa não exista

    Args:
        índices (tuple[int]): tupla de inteiros que representam os índices das tarefas
                             que devem ser removidas da lista.
    """
    índices = list(índices)
    índices.sort(reverse=True)
    for i in índices:
        if 0 <= i < len(lista_de_tarefas):
            lista_de_tarefas.pop(i)
        else:
            raise ValueError("Tarefa não existe")

def encontra_tarefa(tarefa: str) -> int:
    """
    Encontra o índice de uma tarefa na lista de tarefas
    Lança exceções caso a tarefa não exista

    Args:
        tarefa (str): string que representa a tarefa
    """
    for index,dict in enumerate(lista_de_tarefas):
        if tarefa == dict["tarefa"]:
            return index
    raise ValueError("Tarefa não existe")

def ordena_por_prioridade():
    """
    Ordena a lista de tarefas por prioridade com as tarefas prioritárias no
    início da lista, seguidas pelas tarefas não prioritárias.
    As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    """
    global lista_de_tarefas
    tarefas_prioritarias = []
    tarefas_nao_prioritarias = []
    for tarefa in lista_de_tarefas:
        if tarefa.get('prioridade'):
            tarefas_prioritarias.append(tarefa)
        else :
            tarefas_nao_prioritarias.append(tarefa)
    tarefas_prioritarias.sort(key=lambda x: x["tarefa"])
    tarefas_nao_prioritarias.sort(key=lambda x: x["tarefa"])
    lista_de_tarefas = tarefas_prioritarias + tarefas_nao_prioritarias

def get_lista_de_tarefas():
    """
    Retorna somente o texto das tarefas da lista de tarefas
    """
    texts = []
    for tarefa in lista_de_tarefas:
        texto = tarefa["tarefa"]
        prioridade = tarefa["prioridade"]
        texts.append(f"{'*' if prioridade else ''} {texto}")
    return tuple(texts)

    textos: list[str] = []
    for tarefa in lista_de_tarefas:
        texto = tarefa["texto"]
        prioridade = tarefa["prioridade"]
        textos.append(f"{'*' if prioridade else ' '} {texto}")
    return tuple(textos)
