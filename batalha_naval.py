import random

def criar_matriz_10x10():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)  # Inicializa com 0
        matriz.append(linha)
    return matriz

def pedir_posicoes():
    posicoes = []
    while len(posicoes) < 5 or len(posicoes) > 10:
        posicoes = []
        print("Digite entre 5 e 10 posições como uma sequência de dígitos (ex: 0102030405 para as posições (0,1), (0,2), (0,3), (0,4), (0,5)):")
        entrada = input("Digite as posições (ou 'sair' para terminar): ")
        if entrada.lower() == 'sair' and len(posicoes) >= 5:
            break
        try:
            if len(entrada) % 2 != 0:
                print("Número ímpar de dígitos. Certifique-se de digitar pares de coordenadas.")
                continue
            for i in range(0, len(entrada), 2):
                linha = int(entrada[i])
                coluna = int(entrada[i + 1])
                if 0 <= linha < 10 and 0 <= coluna < 10:
                    posicoes.append((linha, coluna))
                else:
                    print(f"Posição fora dos limites: ({linha},{coluna}). Digite valores entre 0 e 9.")
            if len(posicoes) < 5:
                print("Você deve inserir no mínimo 5 posições.")
        except ValueError:
            print("Entrada inválida. Por favor, insira os valores no formato correto.")
    return posicoes


def escolher_posicoes_aleatorias():
    num_posicoes = random.randint(5, 10)
    posicoes = []
    for i in range(num_posicoes):
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        posicoes.append((linha, coluna))
    return posicoes


def trocar_valores(matriz, posicoes, valor=3):
    for linha, coluna in posicoes:
        matriz[linha][coluna] = valor
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(elemento) for elemento in linha))

tabuleiro_jogador_1 = criar_matriz_10x10()
tabuleiro_computador = criar_matriz_10x10()

# Escolher posições aleatórias pelo computador
posicoes_computador = escolher_posicoes_aleatorias()

# Pedir posições ao usuário
posicoes_jogador_1 = pedir_posicoes()

# Trocando os valores na matriz
tabuleiro_modificado_jogador_1 = trocar_valores(tabuleiro_jogador_1, posicoes_jogador_1)

# Imprimindo a matriz do jogador 1
print("Tabuleiro do Jogador 1:")
imprimir_matriz(tabuleiro_modificado_jogador_1)

# Matriz do computador
tabuleiro_modificado_computador = trocar_valores(tabuleiro_computador, posicoes_computador)

# Imprimindo a matriz do computador
print("\nTabuleiro do Computador:")
imprimir_matriz(tabuleiro_modificado_computador)

def comparar_posicoes(posicoes_computador, ataque_usuario1):
    posicoes_corretas = []
    for posicao in ataque_usuario1:
        if posicao in posicoes_computador:
            posicoes_corretas.append(posicao)
    return posicoes_corretas

def ataque_usuario():
    while True:
        try:
            entrada = input("Digite a posição como uma sequência de dois dígitos (ex: 01 para a posição (0,1)): ")
            if len(entrada) != 2:
                print("Número incorreto de dígitos. Certifique-se de digitar duas coordenadas.")
                continue
            linha = int(entrada[0])
            coluna = int(entrada[1])
            if 0 <= linha < 10 and 0 <= coluna < 10:
                return (linha, coluna)
            else:
                print(f"Posição fora dos limites: ({linha},{coluna}). Digite valores entre 0 e 9.")
        except ValueError:
            print("Entrada inválida. Por favor, insira os valores no formato correto.")


def escolher_ataque_aleatorio():
    posicoes = []
    for i in range(1):
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        posicoes.append((linha, coluna))
    return posicoes

ataque_robo = escolher_ataque_aleatorio()

print(posicoes_computador)

ataque_usuario1 = ataque_usuario()

posicoes_corretas_usuario = comparar_posicoes(posicoes_computador, ataque_usuario1)

posicoes_corretas_robo = comparar_posicoes(posicoes_jogador_1, ataque_robo)

print("Posições corretas encontradas:", posicoes_corretas_usuario)

print("Posições corretas encontradas:", posicoes_corretas_robo)
