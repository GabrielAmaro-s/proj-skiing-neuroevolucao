from agente import Agente
from config import TAMANHO_POPULACAO


def criar_populacao():

    populacao = []

    for i in range(TAMANHO_POPULACAO):

        agente = Agente()

        populacao.append(agente)

    return populacao