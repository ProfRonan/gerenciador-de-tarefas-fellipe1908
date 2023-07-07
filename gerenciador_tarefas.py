"""
Modulo que implementa um gerenciador de tarefas
"""

Tarefa = dict[str, bool | str]  # dicionário que representa uma tarefa

lista_de_tarefas: list[Tarefa] = [
    {"prioridade": True, "texto": "Estudar Python"},
    {"prioridade": False, "texto": "Tomar banho"},
    {"prioridade": False, "texto": "Assistir série"},
]

def adicionar_tarefa(prioridade: bool, texto: str):

    texto = {'prioridade': prioridade, 'texto': texto}
    if prioridade != True and prioridade != False:
        raise ValueError("Prioridade inválida.")
    if encontra_tarefa(texto) == True:
        raise ValueError("Tarefa já existe.")    
    lista_de_tarefas.append(texto)
    return lista_de_tarefas


def remove_tarefas(indices: tuple[int, ...]):
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
  com_prioridade =[]
  sem_prioridade = []
  global lista_de_tarefas
  for i in lista_de_tarefas:
    if i['prioridade'] == True:
        com_prioridade.append(i)
    elif i['prioridade']== False:
        sem_prioridade.append(i)
    
    a = sorted(com_prioridade, key=lambda d:d['texto'])
    b = sorted(sem_prioridade, key=lambda d:d['texto'])
    lista_de_tarefas= a+b
    

def ordenar_tarefas(lista_tarefas):
    tarefas_prioritarias = [tarefa for tarefa in lista_tarefas if tarefa[1] == True]
    tarefas_nao_prioritarias = [tarefa for tarefa in lista_tarefas if tarefa[1] == False]

    tarefas_prioritarias.sort(key=lambda texto: texto [0])
    tarefas_nao_prioritarias.sort(key=lambda texto:texto [0])

    lista_ordenada = tarefas_prioritarias + tarefas_nao_prioritarias

    return lista_ordenada

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