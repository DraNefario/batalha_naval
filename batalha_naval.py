import random

def criar_matriz_10x10():
    return [[0 for _ in range(10)] for _ in range(10)]

def imprimir_matriz(matriz):
    for linha in matriz:
        print("[", end="")
        print(", ".join(str(elemento) for elemento in linha), end="")
        print("]")

def pedir_posicoes():
    posicoes = []

    for i in range(1, 11):
        while True:
            try:
                linha = int(input(f"Posicione sua embarcação {i} - linha (de 0 a 9): "))
                coluna = int(input(f"Posicione sua embarcação {i} - coluna (de 0 a 9): "))
                
                if 0 <= linha < 10 and 0 <= coluna < 10:
                    if (linha, coluna) not in posicoes:
                        posicoes.append((linha, coluna))
                        break
                    else:
                        print("Você já posicionou uma embarcação nessa posição. Escolha outra.")
                else:
                    print(f"Posição fora dos limites: ({linha},{coluna}). Digite valores entre 0 e 9.")
            except ValueError:
                print("Entrada inválida. Por favor, insira os valores no formato correto.")
    
    return posicoes

def escolher_posicoes_aleatorias():
    num_posicoes = 10
    posicoes = set()  
    while len(posicoes) < num_posicoes:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        posicoes.add((linha, coluna))
    return posicoes

def trocar_valores(matriz, posicoes, valor=1):
    for linha, coluna in posicoes:
        matriz[linha][coluna] = valor
    return matriz

def contar_embarcacoes_restantes(matriz):
    return sum(linha.count(1) for linha in matriz)

def comparar_posicoes(posicoes_embarcacoes, ataque):
    return [posicao for posicao in ataque if posicao in posicoes_embarcacoes]

def ataque_usuario():
    while True:
        try:
            linha = int(input("Qual linha deseja atacar (entre 0 e 9)? "))
            coluna = int(input("Qual coluna deseja atacar (entre 0 e 9)? "))
            
            if 0 <= linha < 10 and 0 <= coluna < 10:
                return (linha, coluna)
            else:
                print("Posição fora dos limites. Digite valores entre 0 e 9.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um parâmetro válido.")

def escolher_ataque_aleatorio():
    linha = random.randint(0, 9)
    coluna = random.randint(0, 9)
    return (linha, coluna)

def mostrar_acertos(tabuleiro_inimigo, acertos):
    for linha, coluna in acertos:
        tabuleiro_inimigo[linha][coluna] = "X"

def jogar():
    tabuleiro_jogador = criar_matriz_10x10()
    tabuleiro_computador = criar_matriz_10x10()
    tela_computador = criar_matriz_10x10()

    def imprimir_mensagem(texto):
        print("--------------------------------------------------------------------------")
        print(texto)
        print("--------------------------------------------------------------------------\n")

    posicoes_jogador = pedir_posicoes()
    tabuleiro_jogador = trocar_valores(tabuleiro_jogador, posicoes_jogador)

    posicoes_computador = escolher_posicoes_aleatorias()
    tabuleiro_computador = trocar_valores(tabuleiro_computador, posicoes_computador)

    print("\n")
    imprimir_mensagem("                           Bem vindo ao nosso \n                           -->BATALHA NAVAL<--\n                       vc provavelmente vai perder\n                              UAHAHAHHAHAHA")
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

        ataque_jogador = ataque_usuario()
        posicoes_corretas_usuario = comparar_posicoes(posicoes_computador, [ataque_jogador])
        tela_computador[ataque_jogador[0]][ataque_jogador[1]] = "O"
        tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] = "O"
        if posicoes_corretas_usuario:
            print("\n")
            imprimir_mensagem("Você acertou!")
            tela_computador[ataque_jogador[0]][ataque_jogador[1]] = "X"
            tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] = "X"
            mostrar_acertos(tela_computador, posicoes_corretas_usuario)
            if contar_embarcacoes_restantes(tabuleiro_computador) == 0:
                imprimir_mensagem("Parabéns! Você afundou todas as embarcações do inimigo!")
                print(f"Jogo desenvolvido por: André Luís, Danillo, Samuel e Thomas.")
                print(f"Obrigado por jogar nosso jogo!")
                break
        else:
            print("\n")
            imprimir_mensagem("Você errou!")

        # Ataque do computador
        while True:
            ataque_computador = escolher_ataque_aleatorio()
            if tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] not in ["X", "O"]:
                break

        print(f"O computador escolheu a linha: {ataque_computador[0]}")
        print(f"O computador escolheu a coluna: {ataque_computador[1]}")
        tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] = "O"

        posicoes_corretas_robo = comparar_posicoes(posicoes_jogador, [ataque_computador])
        if posicoes_corretas_robo:
            print("\n")
            imprimir_mensagem("Computador acertou!")
            tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] = "X"
            mostrar_acertos(tabuleiro_jogador, posicoes_corretas_robo)
            if contar_embarcacoes_restantes(tabuleiro_jogador) == 0:
                imprimir_mensagem("Você perdeu! O computador destruiu todas as suas embarcações.")
                print(f"Jogo desenvolvido por: André Luís, Danillo, Samuel e Thomas.")
                print(f"Obrigado por jogar nosso jogo!")
                break
        else:
            print("\n")
            imprimir_mensagem("Computador errou!")

# Iniciar o jogo
jogar()
