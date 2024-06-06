#Tópico 1 - Importar a biblioteca random
import random

#Tópico 2 - Função para criar uma matriz 10x10 preenchida com zeros
def criar_matriz_10x10():
    return [[0 for _ in range(10)] for _ in range(10)]

#Tópico 3 - Função para imprimir a matriz
def imprimir_matriz(matriz):
    for linha in matriz:
        print("[", end="")
        print(", ".join(str(elemento) for elemento in linha), end="")
        print("]")

#Tópico 4 - Função para pedir as posições das embarcações para o jogador
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

#Tópico 5 - Função para o computador escolher as posições aleatórias de suas embarcações
def escolher_posicoes_aleatorias():
    num_posicoes = 10
    posicoes = set()  
    while len(posicoes) < num_posicoes:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        posicoes.add((linha, coluna))
    return posicoes

#Tópico 6 - Função para trocar os valores da matriz de acordo com as posições das embarcações escolhidas
def trocar_valores(matriz, posicoes, valor=1):
    for linha, coluna in posicoes:
        matriz[linha][coluna] = valor
    return matriz

#Tópico 7 - Função para contar as embarcações restantes na matriz
def contar_embarcacoes_restantes(matriz):
    return sum(linha.count(1) for linha in matriz)

#Tópico 8 - Função para comparar as posições do ataque com as posições das embarcações
def comparar_posicoes(posicoes_embarcacoes, ataque):
    return [posicao for posicao in ataque if posicao in posicoes_embarcacoes]

#Tópico 9 - Função para o jogador realizar um ataque
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

#Tópico 10 - Função para o computador escolher um ataque de embarcação aleatório
def escolher_ataque_aleatorio():
    linha = random.randint(0, 9)
    coluna = random.randint(0, 9)
    return (linha, coluna)

#Tópico 11 - Função para mostrar os acertos no tabuleiro do computador
def mostrar_acertos(tela_computador, tabuleiro_computador, acertos):
    for linha, coluna in acertos:
        tabuleiro_computador[linha][coluna] = "X"
        tela_computador[linha][coluna] = "X"

#Tópico 12 - Função para imprimir uma mensagem com formatação
def imprimir_mensagem(texto):
    print("--------------------------------------------------------------------------")
    print(texto)
    print("--------------------------------------------------------------------------\n")

#Tópico 13 - Função PRINCIPAL do jogo
def jogar():
    #Cria os tabuleiros do jogador, do computador e as matrizes
    tabuleiro_jogador = criar_matriz_10x10()
    tabuleiro_computador = criar_matriz_10x10()
    tela_computador = criar_matriz_10x10()
    tela_jogador = criar_matriz_10x10()

    #Pede as posições das embarcações para o jogador
    posicoes_jogador = pedir_posicoes()
    tabuleiro_jogador = trocar_valores(tabuleiro_jogador, posicoes_jogador)

    #Escolhe posições aleatórias das embarcações do computador
    posicoes_computador = escolher_posicoes_aleatorias()
    tabuleiro_computador = trocar_valores(tabuleiro_computador, posicoes_computador)

    #Printa uma mensagem de boas-vindas
    print("\n")
    imprimir_mensagem("                           Bem vindo ao nosso \n                           -->BATALHA NAVAL<--\n                       vc provavelmente vai perder\n                              UAHAHAHHAHAHA")
    print("\n")

    #Loop PRINCIPAL do jogo
    while True:
        #Mostra o tabuleiro do computador e do jogador
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

        #Ataque do jogador
        ataque_jogador = ataque_usuario()
        if tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] in ["X", "O"]:
                print("Você já posicionou uma embarcação nessa posição. Escolha outra.")
                continue
        
        posicoes_corretas_usuario = comparar_posicoes(posicoes_computador, [ataque_jogador])
        tela_computador[ataque_jogador[0]][ataque_jogador[1]] = "O"
        tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] = "O"

        if posicoes_corretas_usuario:
            print("\n")
            imprimir_mensagem("Você acertou!")
            #tela_computador[ataque_jogador[0]][ataque_jogador[1]] = "X"
            #tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] = "X"
            mostrar_acertos(tabuleiro_computador, tela_computador, posicoes_corretas_usuario)

            #Verifica se o jogador afundou todas as embarcações do computador
            if contar_embarcacoes_restantes(tabuleiro_computador) == 0:
                imprimir_mensagem("Parabéns! Você afundou todas as embarcações do inimigo!")
                imprimir_mensagem(f"Jogo desenvolvido por: André Luís, Danillo, Samuel e Thomas.\nObrigado por jogar nosso jogo!")
                break
        else:
            print("\n")
            imprimir_mensagem("Você errou!")

        #Ataque do computador
        while True:
            ataque_computador = escolher_ataque_aleatorio()
            if tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] not in ["X", "O"]:
                break

        print(f"O computador escolheu a linha: {ataque_computador[0]}")
        print(f"O computador escolheu a coluna: {ataque_computador[1]}")
        tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] = "O"

        #Verifica se o computador acertou alguma embarcação do jogador
        posicoes_corretas_robo = comparar_posicoes(posicoes_jogador, [ataque_computador])
        if posicoes_corretas_robo:
            print("\n")
            imprimir_mensagem("Computador acertou!")
            #tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] = "X"
            mostrar_acertos(tela_jogador, tabuleiro_jogador, posicoes_corretas_robo)
            
            #Verifica se o computador acertou todas as embarcações do jogador
            if contar_embarcacoes_restantes(tabuleiro_jogador) == 0:
                imprimir_mensagem("Você perdeu! O computador destruiu todas as suas embarcações.")
                imprimir_mensagem(f"Jogo desenvolvido por: André Luís, Danillo, Samuel e Thomas.\nObrigado por jogar nosso jogo!")
                break
        else:
            print("\n")
            imprimir_mensagem("Computador errou!")

#Tópico 14 - Inicia o jogo
jogar()
