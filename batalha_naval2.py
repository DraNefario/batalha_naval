import random

def criar_matriz_5x10():
    return [[0 for _ in range(10)] for _ in range(5)]

def imprimir_matriz(matriz):
    for linha in matriz:
        print("[", end="")
        print(", ".join(str(elemento) for elemento in linha), end="")
        print("]")

def verificar_espaco(matriz, linha, coluna, tamanho, orientacao):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    if orientacao == 'H':
        if coluna + tamanho > colunas:
            return False
        for i in range(tamanho):
            if matriz[linha][coluna + i] != 0:
                return False
        for i in range(-1, tamanho + 1):
            if linha > 0 and 0 <= coluna + i < colunas and matriz[linha - 1][coluna + i] != 0:
                return False
            if linha < linhas - 1 and 0 <= coluna + i < colunas and matriz[linha + 1][coluna + i] != 0:
                return False
        if 0 <= coluna - 1 < colunas and matriz[linha][coluna - 1] != 0:
            return False
        if coluna + tamanho < colunas and matriz[linha][coluna + tamanho] != 0:
            return False
    elif orientacao == 'V':
        if linha + tamanho > linhas:
            return False
        for i in range(tamanho):
            if matriz[linha + i][coluna] != 0:
                return False
        for i in range(-1, tamanho + 1):
            if coluna > 0 and 0 <= linha + i < linhas and matriz[linha + i][coluna - 1] != 0:
                return False
            if coluna < colunas - 1 and 0 <= linha + i < linhas and matriz[linha + i][coluna + 1] != 0:
                return False
        if 0 <= linha - 1 < linhas and matriz[linha - 1][coluna] != 0:
            return False
        if linha + tamanho < linhas and matriz[linha + tamanho][coluna] != 0:
            return False
    return True

def marcar_embarcacao(matriz, linha, coluna, tamanho, orientacao):
    if orientacao == 'H':
        for i in range(tamanho):
            matriz[linha][coluna + i] = 1
    elif orientacao == 'V':
        for i in range(tamanho):
            matriz[linha + i][coluna] = 1

def escolher_posicoes_aleatorias():
    linhas, colunas = 5, 10
    matriz = criar_matriz_5x10()
    
    embarcacoes = [(3, 1), (2, 2), (1, 3)]  # (tamanho, quantidade)
    for tamanho, quantidade in embarcacoes:
        for _ in range(quantidade):
            while True:
                linha = random.randint(0, linhas - 1)
                coluna = random.randint(0, colunas - 1)
                orientacao = random.choice(['H', 'V'])
                if verificar_espaco(matriz, linha, coluna, tamanho, orientacao):
                    marcar_embarcacao(matriz, linha, coluna, tamanho, orientacao)
                    break

    return matriz

def validar_entrada(matriz, linha, coluna, tamanho, orientacao):
    if not (0 <= linha < 5 and 0 <= coluna < 10):
        print("Posição fora dos limites. Digite valores válidos.")
        return False
    if orientacao not in ['H', 'V']:
        print("Orientação inválida. Escolha 'H' para horizontal ou 'V' para vertical.")
        return False
    if (linha == 0 or linha == 4) and orientacao == 'V' and tamanho == 3:
        print("Embarcação de 3 posições deve ser horizontal nas bordas superior e inferior.")
        return False
    if (coluna == 0 or coluna == 9) and orientacao == 'H' and tamanho == 3:
        print("Embarcação de 3 posições deve ser vertical nas bordas esquerda e direita.")
        return False
    if not verificar_espaco(matriz, linha, coluna, tamanho, orientacao):
        print("Uma ou mais posições já estão ocupadas ou fora dos limites. Escolha outras.")
        return False
    return True

def pedir_posicoes():
    posicoes = []
    matriz = criar_matriz_5x10()

    embarcacoes = [(3, 1), (2, 2), (1, 3)]  # (tamanho, quantidade)
    for tamanho, quantidade in embarcacoes:
        for _ in range(quantidade):
            while True:
                try:
                    linha = int(input(f"Posicione sua embarcação de {tamanho} posições:\nLinha (de 0 a 4): "))
                    coluna = int(input("Coluna (de 0 a 9): "))
                    orientacao = 'H' if tamanho == 1 else input("Escolha a orientação (H para horizontal, V para vertical): ").upper()
                    
                    if validar_entrada(matriz, linha, coluna, tamanho, orientacao):
                        marcar_embarcacao(matriz, linha, coluna, tamanho, orientacao)
                        imprimir_matriz(matriz)  # Mostrar o tabuleiro atualizado
                        posicoes.extend((linha, coluna + i) for i in range(tamanho) if orientacao == 'H')
                        posicoes.extend((linha + i, coluna) for i in range(tamanho) if orientacao == 'V')
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira os valores no formato correto.")
    return posicoes

def trocar_valores(matriz, posicoes, valor=1):
    for linha, coluna in posicoes:
        if 0 <= linha < 5 and 0 <= coluna < 10:
            matriz[linha][coluna] = valor
        else:
            print(f"A posição ({linha}, {coluna}) está fora dos limites da matriz.")
    return matriz

def contar_embarcacoes_restantes(matriz):
    return sum(linha.count(1) for linha in matriz)

def ataque_usuario():
    while True:
        try:
            linha = int(input("Qual linha deseja atacar (entre 0 e 4)? "))
            coluna = int(input("Qual coluna deseja atacar (entre 0 e 9)? "))
            
            if 0 <= linha < 5 and 0 <= coluna < 10:
                return (linha, coluna)
            else:
                print(f"Posição fora dos limites: ({linha},{coluna}). Digite valores entre 0 e 4 para linha e 0 e 9 para coluna.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um parâmetro válido.")

def escolher_ataque_aleatorio():
    linha = random.randint(0, 4)
    coluna = random.randint(0, 9)
    return (linha, coluna)

def imprimir_mensagem(texto):
    print("--------------------------------------------------------------------------")
    print(texto)
    print("--------------------------------------------------------------------------\n")

def jogar():
    tabuleiro_jogador = criar_matriz_5x10()
    tabuleiro_computador = criar_matriz_5x10()
    tela_computador = criar_matriz_5x10()
    tela_jogador = criar_matriz_5x10()

    posicoes_jogador = pedir_posicoes()
    tabuleiro_jogador = trocar_valores(tabuleiro_jogador, posicoes_jogador)

    tabuleiro_computador = escolher_posicoes_aleatorias()

    print("\n")
    imprimir_mensagem("                           Bem vindo ao nosso \n                           -->BATALHA NAVAL<--\n                       vc provavelmente vai perder\n                              UAHAHAHHAHAHA")
    print("\n")

    print("Tabuleiro do Computador após definir embarcações:")
    imprimir_matriz(tabuleiro_computador)
    print("\n")

    print("Tabuleiro do Jogador após definir embarcações:")
    imprimir_matriz(tabuleiro_jogador)
    print("\n")

    while True:
        imprimir_mensagem("Tabuleiro do Computador")
        imprimir_matriz(tela_computador)
        print("--------------------------------------------------------------------------")
        print("Embarcações restantes:", contar_embarcacoes_restantes(tabuleiro_computador))
        print("\n")
        imprimir_mensagem("Tabuleiro do Jogador")
        imprimir_matriz(tabuleiro_jogador)
        print("--------------------------------------------------------------------------")
        print("Embarcações restantes:", contar_embarcacoes_restantes(tabuleiro_jogador))
        print("\n")

        while True:
            ataque_jogador = ataque_usuario()
            if tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] in ["X", "O"]:
                print("Você já atacou esta posição. Escolha outra.")
                continue
            
            if tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] == 1:
                tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] = "X"
                tela_computador[ataque_jogador[0]][ataque_jogador[1]] = "X"
                imprimir_mensagem("Você acertou!")

                if contar_embarcacoes_restantes(tabuleiro_computador) == 0:
                    imprimir_mensagem("Parabéns! Você afundou todas as embarcações do inimigo!")
                    imprimir_mensagem(f"Jogo desenvolvido por: André Luís, Danillo, Samuel e Thomas.\nObrigado por jogar nosso jogo!")
                    return
            else:
                tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] = "O"
                tela_computador[ataque_jogador[0]][ataque_jogador[1]] = "O"
                imprimir_mensagem("Você errou!")
                break

        while True:
            ataque_computador = escolher_ataque_aleatorio()
            if tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] not in ["X", "O"]:
                break

        print(f"O computador escolheu a linha: {ataque_computador[0]}")
        print(f"O computador escolheu a coluna: {ataque_computador[1]}")
        if tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] == 1:
            tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] = "X"
            tela_jogador[ataque_computador[0]][ataque_computador[1]] = "X"
            imprimir_mensagem("Computador acertou!")

            if contar_embarcacoes_restantes(tabuleiro_jogador) == 0:
                imprimir_mensagem("Você perdeu! O computador destruiu todas as suas embarcações.")
                imprimir_mensagem(f"Jogo desenvolvido por: André Luís, Danillo, Samuel e Thomas.\nObrigado por jogar nosso jogo!")
                return
        else:
            tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] = "O"
            tela_jogador[ataque_computador[0]][ataque_computador[1]] = "O"
            imprimir_mensagem("Computador errou!")

# Iniciar o jogo
jogar()
