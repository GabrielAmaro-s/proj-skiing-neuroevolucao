
import numpy as np

from populacao import criar_populacao
from ambiente import avaliar
from evolucao import nova_geracao

# Criar a população inicial
populacao = criar_populacao()

# Avaliar todos os agentes
for agente in populacao:
    agente.fitness = avaliar(agente)

# Identificar o melhor agente
melhor = max(
    populacao,
    key=lambda agente: agente.fitness
)

# Criar nova geração
nova_populacao = nova_geracao(populacao)

# Conferir se o melhor agente foi preservado
elite_preservada = all(
    np.array_equal(
        getattr(melhor, parametro),
        getattr(nova_populacao[0], parametro)
    )
    for parametro in ["W1", "b1", "W2", "b2"]
)

print("\nTESTE DE NOVA GERAÇÃO")
print(f"População original: {len(populacao)}")
print(f"Nova população: {len(nova_populacao)}")
print(f"Melhor fitness original: {melhor.fitness:.2f}")
print(f"Elite preservada: {elite_preservada}")
