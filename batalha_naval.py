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

    for _ in range(10):
        while True:
            entrada = input("Digite a posição das embarcaçoes (ou 'sair' para terminar): ")
            if entrada.lower() == 'sair':
                quit()

            try:
                if len(entrada) != 2:
                    print("Número incorreto de dígitos. Certifique-se de digitar duas coordenadas.")
                    continue

                linha = int(entrada[0])
                coluna = int(entrada[1])
                if 0 <= linha < 10 and 0 <= coluna < 10:
                    posicoes.append((linha, coluna))
                    break
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


def mostrar_acertos(tabuleiro_usuario, tabuleiro_inimigo, acertos):
    for linha in range(10):
        for coluna in range(10):
            if (linha, coluna) in acertos:
                tabuleiro_inimigo[linha][coluna] = "X"
    for posicao in acertos:
        linha, coluna = posicao
        print ("Parabéns! Você acertou!")

def jogar():
    tabuleiro_jogador = criar_matriz_10x10()
    tabuleiro_computador = criar_matriz_10x10()
    tela_jogador = criar_matriz_10x10()
    tela_computador = criar_matriz_10x10()

    def imprimir_mensagem(texto):
        print("--------------------------------------------------------------------------")
        print(texto)
        print("--------------------------------------------------------------------------\n")

    posicoes_jogador = pedir_posicoes()
    tabuleiro_jogador = trocar_valores(tabuleiro_jogador, posicoes_jogador)

    posicoes_computador = escolher_posicoes_aleatorias()
    tabuleiro_computador = trocar_valores(tabuleiro_computador, posicoes_computador)

    while True:
        imprimir_mensagem("Tabuleiro do Computador")
        imprimir_matriz(tela_computador)
        print("Embarcações restantes:", contar_embarcacoes_restantes(tabuleiro_computador))

        imprimir_mensagem("Tabuleiro do Jogador")
        imprimir_matriz(tabuleiro_jogador)
        print("Embarcações restantes:", contar_embarcacoes_restantes(tabuleiro_jogador))
        print("\n")

        ataque_jogador = ataque_usuario()
        posicoes_corretas_usuario = comparar_posicoes(posicoes_computador, [ataque_jogador])
        if posicoes_corretas_usuario:
            imprimir_mensagem("Acertou!")
            tela_computador[ataque_jogador[0]][ataque_jogador[1]] = "X"
            tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] = "X"
            mostrar_acertos(tela_jogador, tela_computador, posicoes_corretas_usuario)
            if contar_embarcacoes_restantes(tabuleiro_computador) == 0:
                imprimir_mensagem("Parabéns! Você afundou todas as embarcações do inimigo!")
                print(f"Jogo deselvolvido por: André Luís, Danillo, Samuel e Thomas.")
                print(f"Obrigado por jogar nosso jogo!")
                break
        else:
            imprimir_mensagem("Não foi dessa vez!")

        # Ataque do computador
        ataque_computador = escolher_ataque_aleatorio()
        linha_computador, coluna_computador = escolher_ataque_aleatorio()
        print("O computador escolheu a linha:", linha_computador)
        print("O computador escolheu a coluna:", coluna_computador)
        posicoes_corretas_robo = comparar_posicoes(posicoes_jogador, [ataque_computador])
        if posicoes_corretas_robo:
            imprimir_mensagem("Computador acertou!")
            tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] = "X"
            mostrar_acertos(tela_jogador, tela_computador, posicoes_corretas_robo)
            if contar_embarcacoes_restantes(tabuleiro_jogador) == 0:
                imprimir_mensagem("Você perdeu! O computador destruiu todas as suas embarcações.")
                print(f"Jogo deselvolvido por: André Luís, Danillo, Samuel e Thomas.")
                print(f"Obrigado por jogar nosso jogo!")
                break
        else:
            imprimir_mensagem("O computador errou o ataque.")

# Iniciar o jogo
jogar()
