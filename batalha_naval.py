import random

#Função para criar uma matriz 10x10 preenchida com zeros
def criar_matriz_10x10():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)  #Inicializa com 0
        matriz.append(linha)
    return matriz

#Função para pedir as posições das embarcações ao jogador
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

#Função para escolher posições aleatórias para o computador
def escolher_posicoes_aleatorias():
    num_posicoes = random.randint(5, 10)
    posicoes = []
    for i in range(num_posicoes):
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        posicoes.append((linha, coluna))
    return posicoes

#Função para trocar os valores da matriz nas posições indicadas
def trocar_valores(matriz, posicoes, valor=3):
    for linha, coluna in posicoes:
        matriz[linha][coluna] = valor
    return matriz

#Função para imprimir a matriz no console
def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(elemento) for elemento in linha))

#Função para imprimir o tabuleiro sem revelar as posições das embarcações
def imprimir_tabuleiro(matriz):
    for linha in matriz:
        linha_formatada = []
        for elemento in linha:
            if elemento == 1:
                linha_formatada.append("O")
            elif elemento == 0:
                linha_formatada.append("-")
            elif elemento == "X":
                linha_formatada.append("X")
            elif elemento == "A":
                linha_formatada.append("A")
        print(" ".join(linha_formatada))

#Criação dos tabuleiros do jogador e do computador
tabuleiro_jogador_1 = criar_matriz_10x10()
tabuleiro_computador = criar_matriz_10x10()

#Pedir posições ao usuário
posicoes_jogador_1 = pedir_posicoes()

#Trocar os valores na matriz do jogador
tabuleiro_modificado_jogador_1 = trocar_valores(tabuleiro_jogador_1, posicoes_jogador_1)

#Imprimir a matriz do jogador 1
print("Tabuleiro do Jogador 1:")
imprimir_tabuleiro(tabuleiro_modificado_jogador_1)

#Escolher posições aleatórias para o computador
posicoes_computador = escolher_posicoes_aleatorias()

#Trocar os valores na matriz do computador
tabuleiro_modificado_computador = trocar_valores(tabuleiro_computador, posicoes_computador)

#Imprimir a matriz do computador
print("\nTabuleiro do Computador:")
imprimir_tabuleiro(tabuleiro_modificado_computador)

#Função para comparar as posições de ataque com as posições das embarcações
def comparar_posicoes(posicoes_computador, ataque_usuario1):
    posicoes_corretas = []
    for posicao in ataque_usuario1:
        if posicao in posicoes_computador:
            posicoes_corretas.append(posicao)
    return posicoes_corretas

#Função para realizar o ataque do jogador
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

#Função para escolher um ataque aleatório para o computador
def escolher_ataque_aleatorio():
    linha = random.randint(0, 9)
    coluna = random.randint(0, 9)
    return (linha, coluna)

#Escolha do ataque aleatório do computador
ataque_robo = escolher_ataque_aleatorio()

#Realização do ataque do jogador
ataque_usuario1 = ataque_usuario()

#Comparação das posições corretas do ataque do jogador
posicoes_corretas_usuario = comparar_posicoes(posicoes_computador, [ataque_usuario1])

#Comparação das posições corretas do ataque do computador
posicoes_corretas_robo = comparar_posicoes(posicoes_jogador_1, [ataque_robo])

#Impressão das posições corretas encontradas
print("Posições corretas encontradas pelo jogador:", posicoes_corretas_usuario)

print("Posições corretas encontradas pelo computador:", posicoes_corretas_robo)
