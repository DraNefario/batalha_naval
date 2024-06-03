import random

# Função para criar uma matriz 10x10 preenchida com zeros
def criar_matriz_10x10():
    return [[0 for _ in range(10)] for _ in range(10)]

# Função para pedir as posições das embarcações ao jogador
def pedir_posicoes():
    posicoes = []
    print("Digite as posições das embarcações. Você precisa inserir entre 5 e 10 posições.")
    for i in range(1, 11):
        if i > 5:
            continuar = input("Deseja inserir outra embarcação? (s/n): ").strip().lower()
            if continuar != 's':
                break
        while True:
            try:
                linha = int(input(f"Embarcação {i} - Linha (0-9): "))
                coluna = int(input(f"Embarcação {i} - Coluna (0-9): "))
                if 0 <= linha < 10 and 0 <= coluna < 10:
                    if (linha, coluna) not in posicoes:
                        posicoes.append((linha, coluna))
                        break
                    else:
                        print("Essa posição já foi escolhida. Escolha outra posição.")
                else:
                    print("Posição fora dos limites. Digite valores entre 0 e 9.")
            except ValueError:
                print("Entrada inválida. Por favor, insira os valores no formato correto.")
    return posicoes

# Função para escolher posições aleatórias para o computador
def escolher_posicoes_aleatorias():
    num_posicoes = random.randint(5, 10)
    posicoes = set()
    while len(posicoes) < num_posicoes:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        posicoes.add((linha, coluna))
    return list(posicoes)

# Função para trocar os valores da matriz nas posições indicadas
def trocar_valores(matriz, posicoes, valor=3):
    for linha, coluna in posicoes:
        matriz[linha][coluna] = valor
    return matriz

# Função para imprimir a matriz no console
def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(elemento) for elemento in linha))

# Função para imprimir o tabuleiro sem revelar as posições das embarcações
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

# Função para comparar as posições de ataque com as posições das embarcações
def comparar_posicoes(posicoes_embarcacoes, ataque):
    return [posicao for posicao in ataque if posicao in posicoes_embarcacoes]

# Função para realizar o ataque do jogador
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

# Função para escolher um ataque aleatório para o computador
def escolher_ataque_aleatorio():
    linha = random.randint(0, 9)
    coluna = random.randint(0, 9)
    return (linha, coluna)

def mostrar_acertos(tabuleiro_usuario, tabuleiro_inimigo, acertos):
    print("Tabuleiro do Inimigo:")
    for linha in range(10):
        for coluna in range(10):
            if (linha, coluna) in acertos:
                tabuleiro_inimigo[linha][coluna] = "X"
    imprimir_tabuleiro(tabuleiro_inimigo)
    print("Tabuleiro do Usuário:")
    imprimir_tabuleiro(tabuleiro_usuario)
    for posicao in acertos:
        linha, coluna = posicao
        print(f"Você acertou o inimigo na posição ({linha}, {coluna})!")

# Função para iniciar o jogo
def jogar():
    # Criação dos tabuleiros do jogador e do computador
    tabuleiro_jogador = criar_matriz_10x10()
    tabuleiro_computador = criar_matriz_10x10()

    # Pedir posições ao usuário
    posicoes_jogador = pedir_posicoes()

    # Trocar os valores na matriz do jogador
    tabuleiro_modificado_jogador = trocar_valores(tabuleiro_jogador, posicoes_jogador)

    # Escolher posições aleatórias para o computador
    posicoes_computador = escolher_posicoes_aleatorias()

    # Trocar os valores na matriz do computador
    tabuleiro_modificado_computador = trocar_valores(tabuleiro_computador, posicoes_computador)

    while True:
        # Ataque do jogador
        print("Tabuleiro do Computador:")
        imprimir_tabuleiro(tabuleiro_modificado_computador)
        ataque_jogador = ataque_usuario()
        posicoes_corretas_usuario = comparar_posicoes(posicoes_computador, [ataque_jogador])
        if posicoes_corretas_usuario:
            print("Acertou!")
            tabuleiro_modificado_computador[ataque_jogador[0]][ataque_jogador[1]] = "X"
            mostrar_acertos(tabuleiro_modificado_jogador, tabuleiro_modificado_computador, posicoes_corretas_usuario)
            if not any(tabuleiro_modificado_computador[i][j] == 3 for i in range(10) for j in range(10)):
                print("Você destruiu todas as embarcações do computador. Você venceu!")
                break
        else:
            print("Errou!")

        # Ataque do computador
        ataque_computador = escolher_ataque_aleatorio()
        print("Tabuleiro do Jogador:")
        imprimir_tabuleiro(tabuleiro_modificado_jogador)
        posicoes_corretas_robo = comparar_posicoes(posicoes_jogador, [ataque_computador])
        if posicoes_corretas_robo:
            print("O computador acertou um de seus navios!")
            tabuleiro_modificado_jogador[ataque_computador[0]][ataque_computador[1]] = "X"
            mostrar_acertos(tabuleiro_modificado_jogador, tabuleiro_modificado_computador, posicoes_corretas_robo)
            if not any(tabuleiro_modificado_jogador[i][j] == 3 for i in range(10) for j in range(10)):
                print("O computador destruiu todas as suas embarcações. Você perdeu!")
                break
        else:
            print("O computador errou o ataque.")

# Iniciar o jogo
jogar()
