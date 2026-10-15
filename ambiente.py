
import gymnasium as gym
import ale_py

from config import ENV_ID

gym.register_envs(ale_py)


def avaliar(agente):

    env = gym.make(
        ENV_ID,
        obs_type="ram"
    )

    estado, info = env.reset()

    terminado = False
    recompensa_total = 0.0
    passos = 0

    # Contador de ações
    acoes = {
        0: 0,  # NOOP
        1: 0,  # RIGHT
        2: 0   # LEFT
    }

    while not terminado:

        acao = agente.agir(estado)

        acoes[acao] += 1

        estado, reward, terminated, truncated, info = env.step(acao)

        recompensa_total += reward
        passos += 1

        terminado = terminated or truncated

    env.close()
    return recompensa_total
