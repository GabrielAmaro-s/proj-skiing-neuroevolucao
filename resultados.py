
import csv
import os

import matplotlib.pyplot as plt
import numpy as np


PASTA_RESULTADOS = "resultados"


def salvar_historico(historico):
    os.makedirs(PASTA_RESULTADOS, exist_ok=True)

    with open(
        f"{PASTA_RESULTADOS}/fitness.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=["geracao", "melhor", "media", "pior"]
        )
        escritor.writeheader()
        escritor.writerows(historico)

    print("Histórico CSV salvo com sucesso!")


def gerar_grafico(historico):
    os.makedirs(PASTA_RESULTADOS, exist_ok=True)

    geracoes = [item["geracao"] for item in historico]
    melhores = [item["melhor"] for item in historico]
    medias = [item["media"] for item in historico]

    plt.figure(figsize=(10, 6))

    plt.plot(geracoes, melhores, label="Melhor fitness", linewidth=2)
    plt.plot(geracoes, medias, label="Fitness médio", linewidth=2)

    plt.xlabel("Geração")
    plt.ylabel("Fitness")
    plt.title("Neuroevolução no ALE/Skiing-v5")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(f"{PASTA_RESULTADOS}/fitness.png", dpi=300)
    plt.close()

    print("Gráfico salvo com sucesso!")


def salvar_agente(agente):
    os.makedirs(PASTA_RESULTADOS, exist_ok=True)

    np.savez(
        f"{PASTA_RESULTADOS}/melhor_agente.npz",
        W1=agente.W1,
        b1=agente.b1,
        W2=agente.W2,
        b2=agente.b2
    )

    print("Melhor agente salvo com sucesso!")
