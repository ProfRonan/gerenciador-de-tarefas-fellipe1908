"""
Modulo que implementa um gerenciador de tarefas
"""

Tarefa = dict[str, bool | str]

lista_de_tarefas: list[Tarefa] = [
    {"prioridade": True, "texto": "Estudar Python"},
    {"prioridade": False, "texto": "Tomar banho"},
    {"prioridade": False, "texto": "Assistir série"},
]


def adicionar_tarefa(prioridade: bool, texto: str):
    tarefa = {'prioridade': prioridade, 'texto': texto}
    if prioridade != True and prioridade != False:
        raise ValueError("Prioridade inválida.")
    if encontra_tarefa(tarefa) == True:
        raise ValueError("Tarefa já existe.")    
    lista_de_tarefas.append(tarefa)
    return lista_de_tarefas

def remove_tarefas(indices: tuple[int, ...]):
    """
    Remove várias tarefas da lista de tarefas de uma vez, dado uma tupla de índices
    Lança exceções caso a tarefa não exista

    Args:
        indices (tuple[int, ...]): tupla de inteiros que representam
            os índices das tarefas que devem ser removidas da lista.
    """
    # TODO: coloque o código aqui para remover um tarefa na lista
    # Caso a tarefa não exista na lista, levante uma exceção do tipo ValueError
    # com a mensagem "Tarefa não existe"

    if len(indices) >len(lista_de_tarefas) -1:
        raise ValueError('Ìndice fora da lista.')
    else: 
        if len(lista_de_tarefas)> 0:
            for i in range(len(indices)-1,-1,-1):
                lista_de_tarefas.pop(indices[i])
        else:
            raise ValueError("Tarefa não existe.")
    

def encontra_tarefa(tarefa: str) -> int:
    for i in lista_de_tarefas:
        if i['texto'] == tarefa['texto']:
            return True
    return False

def ordena_por_prioridade():
    """
    Ordena a lista de tarefas por prioridade com as tarefas prioritárias no
    início da lista, seguidas pelas tarefas não prioritárias.
    As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    """
    # TODO: coloque o código aqui para ordenar a lista de tarefas por prioridade
    # com as tarefas prioritárias no início da lista, seguidas pelas tarefas
    # não prioritárias.
    # As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    # tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    com_prioridade = []
    sem_prioridade = []
    global lista_de_tarefas
    for i in lista_de_tarefas:
        if i['prioridade'] == True:
            com_prioridade.append(i)    
        elif i['prioridade'] == False: 
            sem_prioridade.append(i)
    a = sorted(com_prioridade, key = lambda d: d['texto'])
    b = sorted(sem_prioridade, key = lambda d: d['texto'])
    lista_de_tarefas = a + b

def get_lista_de_tarefas():
    """
    Retorna somente o texto das tarefas da lista de tarefas
    """
    textos: list[str] = []
    for tarefa in lista_de_tarefas:
        texto = tarefa["texto"]
        prioridade = tarefa["prioridade"]
        textos.append(f"{'*' if prioridade else ' '} {texto}")
    return tuple(textos)