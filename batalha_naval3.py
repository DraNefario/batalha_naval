import random
from colorama import Fore, Style, init

init(autoreset=True)

def criar_matriz_5x10():
    return [[0 for _ in range(10)] for _ in range(5)]

def imprimir_matriz(matriz, esconder=False):
    for linha in matriz:
        print("[", end="")
        for elemento in linha:
            if elemento == "X":
                print(f"{Fore.RED}{elemento}", end=", ")
            elif elemento == "O":
                print(f"{Fore.YELLOW}{elemento}", end=", ")
            elif elemento == 1 and not esconder:
                print(f"{Fore.GREEN}{elemento}", end=", ")
            else:
                print(f"{elemento}", end=", ")
        print("\b\b]")

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
    
    embarcacoes = [(3, 1), (2, 2), (1, 3)]
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

def pedir_posicoes(nome_jogador):
    matriz = criar_matriz_5x10()

    embarcacoes = [(3, 1), (2, 2), (1, 3)]
    for tamanho, quantidade in embarcacoes:
        for _ in range(quantidade):
            while True:
                try:
                    print(f"{nome_jogador}, posicione sua embarcação de {tamanho} posições:")
                    linha = int(input("Linha (de 0 a 4): "))
                    coluna = int(input("Coluna (de 0 a 9): "))
                    orientacao = 'H' if tamanho == 1 else input("Escolha a orientação (H para horizontal, V para vertical): ").upper()
                    
                    if validar_entrada(matriz, linha, coluna, tamanho, orientacao):
                        marcar_embarcacao(matriz, linha, coluna, tamanho, orientacao)
                        imprimir_matriz(matriz)
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira os valores no formato correto.")
    return matriz

def contar_embarcacoes_restantes(matriz):
    return sum(linha.count(1) for linha in matriz)

def ataque_usuario(nome_jogador):
    while True:
        try:
            print(f"{nome_jogador}, escolha sua posição de ataque:")
            linha = int(input("Linha (de 0 a 4): "))
            coluna = int(input("Coluna (de 0 a 9): "))

            if 0 <= linha < 5 and 0 <= coluna < 10:
                return (linha, coluna)
            else:
                print("Posição fora dos limites. Digite valores válidos.")
        except ValueError:
            print("Entrada inválida. Por favor, insira os valores no formato correto.")

def imprimir_mensagem(texto):
    print("--------------------------------------------------------------------------")
    print(texto)
    print("--------------------------------------------------------------------------\n")

def pve_posicionamento():
    return escolher_posicoes_aleatorias()

def pve_ataque(matriz_jogador, tela_computador):
    while True:
        linha = random.randint(0, 4)
        coluna = random.randint(0, 9)
        if matriz_jogador[linha][coluna] not in ["X", "O"]:
            if matriz_jogador[linha][coluna] == 1:
                matriz_jogador[linha][coluna] = "X"
                tela_computador[linha][coluna] = "X"
                imprimir_mensagem(Fore.GREEN + "Computador acertou!")
            else:
                matriz_jogador[linha][coluna] = "O"
                tela_computador[linha][coluna] = "O"
                imprimir_mensagem(Fore.RED + "Computador errou!")
            break

def jogar():
    print("Escolha o modo de jogo: (1) PvP (2) PvE")
    modo = int(input("Modo: "))

    tabuleiro_jogador1 = criar_matriz_5x10()
    tabuleiro_jogador2 = criar_matriz_5x10()
    tela_jogador1 = criar_matriz_5x10()
    tela_jogador2 = criar_matriz_5x10()

    tabuleiro_jogador1 = pedir_posicoes("Jogador 1")

    imprimir_mensagem("Posicionamento do Jogador 1 completo. Por favor, passe para o Jogador 2.")

    if modo == 1:  # PvP
        tabuleiro_jogador2 = pedir_posicoes("Jogador 2")
    else:  # PvE
        tabuleiro_jogador2 = pve_posicionamento()
    print("\n\n")
    imprimir_mensagem("                           Bem vindo ao nosso \n                           -->BATALHA NAVAL<--")

    while True:
        imprimir_mensagem("Tabuleiro do Jogador 2")
        imprimir_matriz(tela_jogador2, esconder=True)
        print("--------------------------------------------------------------------------")
        print("Embarcações restantes do Jogador 2:", contar_embarcacoes_restantes(tabuleiro_jogador2))
        print("\n")
        imprimir_mensagem("Tabuleiro do Jogador 1")
        imprimir_matriz(tabuleiro_jogador1)
        print("--------------------------------------------------------------------------")
        print("Embarcações restantes do Jogador 1:", contar_embarcacoes_restantes(tabuleiro_jogador1))
        print("\n")

        while True:
            ataque_jogador1 = ataque_usuario("Jogador 1")
            if tabuleiro_jogador2[ataque_jogador1[0]][ataque_jogador1[1]] in ["X", "O"]:
                print("Você já atacou esta posição. Escolha outra.")
                continue
            
            if tabuleiro_jogador2[ataque_jogador1[0]][ataque_jogador1[1]] == 1:
                tabuleiro_jogador2[ataque_jogador1[0]][ataque_jogador1[1]] = "X"
                tela_jogador2[ataque_jogador1[0]][ataque_jogador1[1]] = "X"
                imprimir_mensagem(Fore.GREEN + "Jogador 1 acertou!")

                if contar_embarcacoes_restantes(tabuleiro_jogador2) == 0:
                    imprimir_mensagem(Fore.GREEN + "Parabéns, Jogador 1! Você afundou todas as embarcações do Jogador 2!")
                    imprimir_mensagem(f"Jogo desenvolvido por: André Luís, Danillo, Samuel e Thomas.\nObrigado por jogar nosso jogo!")
                    return
            else:
                tabuleiro_jogador2[ataque_jogador1[0]][ataque_jogador1[1]] = "O"
                tela_jogador2[ataque_jogador1[0]][ataque_jogador1[1]] = "O"
                imprimir_mensagem(Fore.RED + "Jogador 1 errou!")
                break

        if modo == 1:  # PvP
            imprimir_mensagem("Tabuleiro do Jogador 1")
            imprimir_matriz(tela_jogador1, esconder=True)
            print("--------------------------------------------------------------------------")
            print("Embarcações restantes do Jogador 1:", contar_embarcacoes_restantes(tabuleiro_jogador1))
            print("\n")
            imprimir_mensagem("Tabuleiro do Jogador 2")
            imprimir_matriz(tabuleiro_jogador2)
            print("--------------------------------------------------------------------------")
            print("Embarcações restantes do Jogador 2:", contar_embarcacoes_restantes(tabuleiro_jogador2))
            print("\n")

            while True:
                ataque_jogador2 = ataque_usuario("Jogador 2")
                if tabuleiro_jogador1[ataque_jogador2[0]][ataque_jogador2[1]] in ["X", "O"]:
                    print("Você já atacou esta posição. Escolha outra.")
                    continue
                
                if tabuleiro_jogador1[ataque_jogador2[0]][ataque_jogador2[1]] == 1:
                    tabuleiro_jogador1[ataque_jogador2[0]][ataque_jogador2[1]] = "X"
                    tela_jogador1[ataque_jogador2[0]][ataque_jogador2[1]] = "X"
                    imprimir_mensagem(Fore.GREEN + "Jogador 2 acertou!")

                    if contar_embarcacoes_restantes(tabuleiro_jogador1) == 0:
                        imprimir_mensagem(Fore.GREEN + "Parabéns, Jogador 2! Você afundou todas as embarcações do Jogador 1!")
                        imprimir_mensagem(f"Jogo desenvolvido por: André Luís, Danillo, Samuel e Thomas.\nObrigado por jogar nosso jogo!")
                        return
                else:
                    tabuleiro_jogador1[ataque_jogador2[0]][ataque_jogador2[1]] = "O"
                    tela_jogador1[ataque_jogador2[0]][ataque_jogador2[1]] = "O"
                    imprimir_mensagem(Fore.RED + "Jogador 2 errou!")
                    break
        else:  # PvE
            pve_ataque(tabuleiro_jogador1, tela_jogador1)
            if contar_embarcacoes_restantes(tabuleiro_jogador1) == 0:
                imprimir_mensagem(Fore.GREEN + "Parabéns, Computador! Você afundou todas as embarcações do Jogador 1!")
                imprimir_mensagem(f"Jogo desenvolvido por: André Luís, Danillo, Samuel e Thomas.\nObrigado por jogar nosso jogo!")
                return

# Iniciar o jogo
jogar()
