
import numpy as np

from config import NUM_GERACOES
from populacao import criar_populacao
from ambiente import avaliar
from evolucao import nova_geracao


def executar_evolucao():

    populacao = criar_populacao()

    historico = []

    melhor_agente_geral = None
    melhor_fitness_geral = float("-inf")

    for geracao in range(NUM_GERACOES):

        print(f"\nGERAÇÃO {geracao + 1}/{NUM_GERACOES}")
        print("-" * 40)

        # Avaliar todos os agentes
        for i, agente in enumerate(populacao):

            agente.fitness = avaliar(agente)

            print(
                f"Agente {i + 1:02d} | "
                f"Fitness: {agente.fitness:.2f}"
            )

        # Calcular estatísticas
        valores = [agente.fitness for agente in populacao]

        melhor = max(valores)
        media = float(np.mean(valores))
        pior = min(valores)

        # Encontrar o melhor agente da geração
        melhor_agente = max(
            populacao,
            key=lambda agente: agente.fitness
        )

        # Guardar o melhor agente encontrado
        if melhor > melhor_fitness_geral:

            import copy

            melhor_fitness_geral = melhor
            melhor_agente_geral = copy.deepcopy(melhor_agente)

        # Registrar histórico
        historico.append({
            "geracao": geracao + 1,
            "melhor": melhor,
            "media": media,
            "pior": pior
        })

        print("\nRESULTADOS DA GERAÇÃO")
        print(f"Melhor: {melhor:.2f}")
        print(f"Média: {media:.2f}")
        print(f"Pior: {pior:.2f}")

        # Criar próxima geração, exceto na última
        if geracao < NUM_GERACOES - 1:

            populacao = nova_geracao(populacao)

    print("\n" + "=" * 40)
    print("EVOLUÇÃO FINALIZADA")
    print("=" * 40)

    print(f"Melhor fitness encontrado: {melhor_fitness_geral:.2f}")

    return historico, melhor_agente_geral


if __name__ == "__main__":

    historico, melhor_agente = executar_evolucao()
