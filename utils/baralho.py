import random

# Dicionário que representa o baralho, onde cada chave é o valor da carta e o valor é a representação da carta
baralho = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

def gerar_maos(n=10):
    """
    Gera duas mãos de cartas aleatórias para dois jogadores.
    :param n: Número de cartas para cada jogador (padrão é 10)
    :return: Duas tuplas representando as mãos dos jogadores
    """
    cartas = list(baralho.keys())
    mao_a = random.sample(cartas, n)
    mao_b = random.sample(cartas, n)
    return tuple(mao_a), tuple(mao_b)

def exibir_cartas(mao):
    """
    Converte os índices das cartas em suas respectivas descrições.
    :param mao: Tupla de índices das cartas
    :return: Lista de descrições das cartas
    """
    return [baralho[carta] for carta in mao]

def comparar_maos(mao_a, mao_b):
    """
    Compara as cartas das mãos dos jogadores e retorna o resultado.
    :param mao_a: Tupla de índices das cartas do Jogador A
    :param mao_b: Tupla de índices das cartas do Jogador B
    :return: Pontos de cada jogador
    """
    pontos_a = 0
    pontos_b = 0
    for carta_a, carta_b in zip(mao_a, mao_b):
        if carta_a > carta_b:
            pontos_a += 1
        elif carta_b > carta_a:
            pontos_b += 1
    return pontos_a, pontos_b

def determinar_vencedor(pontos_a, pontos_b):
    """
    Determina o vencedor com base nos pontos.
    :param pontos_a: Pontos do Jogador A
    :param pontos_b: Pontos do Jogador B
    :return: String com o resultado do jogo
    """
    if pontos_a > pontos_b:
        return f"Jogador A venceu: {pontos_a} x {pontos_b}!"
    elif pontos_b > pontos_a:
        return f"Jogador B venceu: {pontos_b} x {pontos_a}!"
    else:
        return "Empate!"
