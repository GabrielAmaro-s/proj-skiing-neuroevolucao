
import copy
import numpy as np

from config import NUM_GERACOES
from populacao import criar_populacao
from ambiente import avaliar
from evolucao import nova_geracao
from resultados import salvar_historico, gerar_grafico, salvar_agente


def executar_evolucao():
    populacao = criar_populacao()
    historico = []

    melhor_agente_geral = None
    melhor_fitness_geral = float("-inf")

    for geracao in range(1, NUM_GERACOES + 1):
        print(f"\nGERAÇÃO {geracao}/{NUM_GERACOES}")
        print("-" * 40)

        # Avaliar os agentes da geração
        for i, agente in enumerate(populacao, start=1):
            agente.fitness = avaliar(agente)

            print(
                f"Agente {i:02d} | "
                f"Fitness: {agente.fitness:.2f}"
            )

        # Calcular as estatísticas da geração
        valores = [agente.fitness for agente in populacao]

        melhor_fitness = max(valores)
        media_fitness = float(np.mean(valores))
        pior_fitness = min(valores)

        # Identificar o melhor agente da geração
        melhor_agente = max(
            populacao,
            key=lambda agente: agente.fitness
        )

        # Preservar o melhor agente de todo o treinamento
        if melhor_fitness > melhor_fitness_geral:
            melhor_fitness_geral = melhor_fitness
            melhor_agente_geral = copy.deepcopy(melhor_agente)

        # Registrar os resultados
        historico.append({
            "geracao": geracao,
            "melhor": melhor_fitness,
            "media": media_fitness,
            "pior": pior_fitness
        })

        print("\nRESULTADOS DA GERAÇÃO")
        print(f"Melhor: {melhor_fitness:.2f}")
        print(f"Média: {media_fitness:.2f}")
        print(f"Pior: {pior_fitness:.2f}")

        # Evoluir a população, exceto na última geração
        if geracao < NUM_GERACOES:
            populacao = nova_geracao(populacao)

    print("\n" + "=" * 40)
    print("EVOLUÇÃO FINALIZADA")
    print("=" * 40)
    print(f"Melhor fitness encontrado: {melhor_fitness_geral:.2f}")

    return historico, melhor_agente_geral


def main():
    historico, melhor_agente = executar_evolucao()

    salvar_historico(historico)
    gerar_grafico(historico)
    salvar_agente(melhor_agente)

    print("\nTodos os resultados foram salvos!")


if __name__ == "__main__":
    main()
