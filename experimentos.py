
import copy
import csv
import os
import random

import matplotlib.pyplot as plt
import numpy as np

from ambiente import avaliar
from config import NUM_GERACOES
from evolucao import nova_geracao
from populacao import criar_populacao


EXPERIMENTOS = {
    "A": (0.01, 0.05),
    "B": (0.10, 0.20),
    "C": (0.40, 0.50)
}

PASTA = "resultados/experimentos"


def executar_experimento(nome, taxa, intensidade):
    random.seed(42)
    np.random.seed(42)

    populacao = criar_populacao()
    historico = []

    melhor_geral = None
    melhor_fitness = float("-inf")

    print(f"\nEXPERIMENTO {nome}")
    print(f"Taxa de mutação: {taxa}")
    print(f"Intensidade: {intensidade}")
    print("=" * 45)

    for geracao in range(1, NUM_GERACOES + 1):
        for agente in populacao:
            agente.fitness = avaliar(agente)

        valores = [agente.fitness for agente in populacao]

        melhor = max(valores)
        media = float(np.mean(valores))
        pior = min(valores)

        agente_melhor = max(
            populacao,
            key=lambda agente: agente.fitness
        )

        if melhor > melhor_fitness:
            melhor_fitness = melhor
            melhor_geral = copy.deepcopy(agente_melhor)

        historico.append({
            "geracao": geracao,
            "melhor": melhor,
            "media": media,
            "pior": pior
        })

        print(
            f"Geração {geracao:02d} | "
            f"Melhor: {melhor:.2f} | "
            f"Média: {media:.2f} | "
            f"Pior: {pior:.2f}"
        )

        if geracao < NUM_GERACOES:
            populacao = nova_geracao(
                populacao,
                taxa_mutacao=taxa,
                intensidade_mutacao=intensidade
            )

    with open(
        f"{PASTA}/fitness_{nome}.csv",
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

    np.savez(
        f"{PASTA}/melhor_agente_{nome}.npz",
        W1=melhor_geral.W1,
        b1=melhor_geral.b1,
        W2=melhor_geral.W2,
        b2=melhor_geral.b2
    )

    print(
        f"\nExperimento {nome} concluído! "
        f"Melhor fitness: {melhor_fitness:.2f}"
    )

    return historico


def gerar_grafico_comparativo(resultados):
    plt.figure(figsize=(11, 6))

    for nome, historico in resultados.items():
        geracoes = [item["geracao"] for item in historico]
        melhores = np.maximum.accumulate(
            [item["melhor"] for item in historico]
        )

        plt.plot(
            geracoes,
            melhores,
            label=f"Experimento {nome}",
            linewidth=2
        )

    plt.title("Comparação dos experimentos - Skiing")
    plt.xlabel("Geração")
    plt.ylabel("Melhor fitness acumulado")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(f"{PASTA}/comparacao.png", dpi=300)
    plt.close()


def salvar_resumo(resultados):
    with open(
        f"{PASTA}/resumo.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow([
            "experimento",
            "taxa_mutacao",
            "intensidade",
            "melhor_fitness",
            "media_final"
        ])

        for nome, historico in resultados.items():
            taxa, intensidade = EXPERIMENTOS[nome]

            melhor_fitness = max(
                item["melhor"] for item in historico
            )
            media_final = historico[-1]["media"]

            escritor.writerow([
                nome,
                taxa,
                intensidade,
                melhor_fitness,
                media_final
            ])


def main():
    os.makedirs(PASTA, exist_ok=True)
    resultados = {}

    for nome, (taxa, intensidade) in EXPERIMENTOS.items():
        resultados[nome] = executar_experimento(
            nome,
            taxa,
            intensidade
        )

    gerar_grafico_comparativo(resultados)
    salvar_resumo(resultados)

    print("\n" + "=" * 45)
    print("TODOS OS EXPERIMENTOS FINALIZADOS")
    print("=" * 45)

    for nome, historico in resultados.items():
        melhor = max(item["melhor"] for item in historico)
        print(f"Experimento {nome}: {melhor:.2f}")

    print(f"\nArquivos salvos em: {PASTA}")


if __name__ == "__main__":
    main()
