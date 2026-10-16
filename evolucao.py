
import copy
import random
import numpy as np

from config import (
    TAMANHO_POPULACAO,
    TAXA_MUTACAO,
    INTENSIDADE_MUTACAO,
    NUM_ELITE
)


def selecionar(populacao, tamanho_torneio=3):
    candidatos = random.sample(populacao, tamanho_torneio)
    return max(candidatos, key=lambda agente: agente.fitness)


def mutar(
    agente,
    taxa_mutacao=TAXA_MUTACAO,
    intensidade_mutacao=INTENSIDADE_MUTACAO
):
    for parametro in ("W1", "b1", "W2", "b2"):
        pesos = getattr(agente, parametro)

        mascara = np.random.random(pesos.shape) < taxa_mutacao
        alteracoes = np.random.normal(
            0, intensidade_mutacao, pesos.shape
        )

        pesos[mascara] += alteracoes[mascara]

    return agente


def nova_geracao(
    populacao,
    taxa_mutacao=TAXA_MUTACAO,
    intensidade_mutacao=INTENSIDADE_MUTACAO
):
    populacao_ordenada = sorted(
        populacao,
        key=lambda agente: agente.fitness,
        reverse=True
    )

    nova_populacao = [
        copy.deepcopy(agente)
        for agente in populacao_ordenada[:NUM_ELITE]
    ]

    while len(nova_populacao) < TAMANHO_POPULACAO:
        pai = selecionar(populacao)
        filho = copy.deepcopy(pai)

        mutar(filho, taxa_mutacao, intensidade_mutacao)
        filho.fitness = 0.0

        nova_populacao.append(filho)

    return nova_populacao
