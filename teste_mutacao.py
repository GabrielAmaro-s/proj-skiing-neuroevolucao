
import copy
import numpy as np

from agente import Agente
from evolucao import mutar


# Criar o agente original
pai = Agente()

# Salvar os pesos originais do pai
pesos_originais = pai.W1.copy()

# Criar uma cópia independente do pai
filho = copy.deepcopy(pai)

# Aplicar mutação somente no filho
mutar(filho)

# Comparar os pesos do pai e do filho
pesos_alterados = np.sum(
    pai.W1 != filho.W1
)

total_pesos = pai.W1.size

# Verificar se os pesos do pai foram preservados
pai_preservado = np.array_equal(
    pai.W1,
    pesos_originais
)

# Exibir resultados
print("RESULTADO DA MUTAÇÃO")
print(f"Pesos W1 alterados: {pesos_alterados}")
print(f"Total de pesos W1: {total_pesos}")
print(f"Pai preservado: {pai_preservado}")
