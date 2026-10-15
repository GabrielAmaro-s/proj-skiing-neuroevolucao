
import random
import numpy as np
import copy
from config import TAMANHO_POPULACAO, NUM_ELITE
from config import TAXA_MUTACAO, INTENSIDADE_MUTACAO


def selecionar(populacao, tamanho_torneio=3):

    # Escolhe três agentes aleatórios da população
    candidatos = random.sample(
        populacao,
        tamanho_torneio
    )

    # Retorna o agente com maior fitness
    vencedor = max(
        candidatos,
        key=lambda agente: agente.fitness
    )

    return vencedor



def mutar(agente):

    # Percorre os parâmetros da rede neural
    for parametro in ["W1", "b1", "W2", "b2"]:

        pesos = getattr(agente, parametro)

        # Define quais pesos sofrerão mutação
        mascara = np.random.random(
            pesos.shape
        ) < TAXA_MUTACAO

        # Gera alterações aleatórias
        alteracoes = np.random.normal(
            0,
            INTENSIDADE_MUTACAO,
            pesos.shape
        )

        # Aplica mutação somente nos pesos selecionados
        pesos[mascara] += alteracoes[mascara]

    return agente

def nova_geracao(populacao):

    # Ordenar agentes do melhor para o pior
    populacao_ordenada = sorted(
        populacao,
        key=lambda agente: agente.fitness,
        reverse=True
    )

    nova_populacao = []

    # ELITISMO: preservar os melhores agentes
    for agente in populacao_ordenada[:NUM_ELITE]:

        elite = copy.deepcopy(agente)

        nova_populacao.append(elite)

    # REPRODUÇÃO: completar a nova população
    while len(nova_populacao) < TAMANHO_POPULACAO:

        # Selecionar um pai por torneio
        pai = selecionar(populacao)

        # Criar uma cópia independente
        filho = copy.deepcopy(pai)

        # Aplicar mutação no filho
        mutar(filho)

        # O filho ainda não foi avaliado
        filho.fitness = 0.0

        nova_populacao.append(filho)

    return nova_populacao