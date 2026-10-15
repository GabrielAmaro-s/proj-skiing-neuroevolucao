import numpy as np
from config import NUM_ENTRADAS, NUM_OCULTOS, NUM_ACOES


class Agente:

    def __init__(self):

        self.W1 = np.random.randn(
        NUM_ENTRADAS, NUM_OCULTOS
        ) * np.sqrt(1 / NUM_ENTRADAS)

        self.b1 = np.zeros(NUM_OCULTOS)

        self.W2 = np.random.randn(
        NUM_OCULTOS, NUM_ACOES
        ) * np.sqrt(1 / NUM_OCULTOS)

        self.b2 = np.zeros(NUM_ACOES)

        self.fitness = 0.0

    def agir(self, estado):

        estado = estado.astype(np.float32) / 255.0

        oculto = np.tanh(
            estado @ self.W1 + self.b1
        )

        saida = oculto @ self.W2 + self.b2

        return int(np.argmax(saida))