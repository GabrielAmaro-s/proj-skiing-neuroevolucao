
from agente import Agente
from config import TAMANHO_POPULACAO


def criar_populacao():
    return [Agente() for _ in range(TAMANHO_POPULACAO)]
