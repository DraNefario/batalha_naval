import random
from colorama import Fore, Style, init

init(autoreset=True)  # Inicializa o Colorama para redefinir automaticamente as cores após o uso

def criar_matriz_5x10():
    """Cria e retorna uma matriz 5x10 preenchida com zeros."""
    return [[0 for _ in range(10)] for _ in range(5)]

def imprimir_matriz(matriz):
    """Imprime a matriz na tela com formatação de cores para diferentes elementos."""
    for linha in matriz:
        print("[", end="")
        for elemento in linha:
            if elemento == "X":
                print(f"{Fore.RED}{elemento}", end=", ")  # Elemento "X" em vermelho
            elif elemento == "O":
                print(f"{Fore.YELLOW}{elemento}", end=", ")  # Elemento "O" em amarelo
            elif elemento == 1:
                print(f"{Fore.GREEN}{elemento}", end=", ")  # Elemento "1" em verde
            else:
                print(f"{elemento}", end=", ")  # Outros elementos sem formatação especial
        print("\b\b]")  # Remove vírgula extra no final e fecha colchetes

def verificar_espaco(matriz, linha, coluna, tamanho, orientacao):
    """Verifica se é possível posicionar uma embarcação na matriz nas coordenadas especificadas."""
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    if orientacao == 'H':  # Orientação horizontal
        if coluna + tamanho > colunas:
            return False  # Fora dos limites à direita
        for i in range(tamanho):
            if matriz[linha][coluna + i] != 0:
                return False  # Espaço ocupado
        # Verifica se há espaço ao redor da embarcação
        for i in range(-1, tamanho + 1):
            if linha > 0 and 0 <= coluna + i < colunas and matriz[linha - 1][coluna + i] != 0:
                return False  # Acima da embarcação
            if linha < linhas - 1 and 0 <= coluna + i < colunas and matriz[linha + 1][coluna + i] != 0:
                return False  # Abaixo da embarcação
        if 0 <= coluna - 1 < colunas and matriz[linha][coluna - 1] != 0:
            return False  # À esquerda da embarcação
        if coluna + tamanho < colunas and matriz[linha][coluna + tamanho] != 0:
            return False  # À direita da embarcação
    elif orientacao == 'V':  # Orientação vertical
        if linha + tamanho > linhas:
            return False  # Fora dos limites abaixo
        for i in range(tamanho):
            if matriz[linha + i][coluna] != 0:
                return False  # Espaço ocupado
        # Verifica se há espaço ao redor da embarcação
        for i in range(-1, tamanho + 1):
            if coluna > 0 and 0 <= linha + i < linhas and matriz[linha + i][coluna - 1] != 0:
                return False  # À esquerda da embarcação
            if coluna < colunas - 1 and 0 <= linha + i < linhas and matriz[linha + i][coluna + 1] != 0:
                return False  # À direita da embarcação
        if 0 <= linha - 1 < linhas and matriz[linha - 1][coluna] != 0:
            return False  # Acima da embarcação
        if linha + tamanho < linhas and matriz[linha + tamanho][coluna] != 0:
            return False  # Abaixo da embarcação
    return True  # Pode posicionar a embarcação

def marcar_embarcacao(matriz, linha, coluna, tamanho, orientacao):
    """Marca a posição da embarcação na matriz."""
    if orientacao == 'H':  # Orientação horizontal
        for i in range(tamanho):
            matriz[linha][coluna + i] = 1  # Marca com 1 na posição horizontal
    elif orientacao == 'V':  # Orientação vertical
        for i in range(tamanho):
            matriz[linha + i][coluna] = 1  # Marca com 1 na posição vertical

def escolher_posicoes_aleatorias():
    """Escolhe aleatoriamente as posições das embarcações no tabuleiro."""
    linhas, colunas = 5, 10
    matriz = criar_matriz_5x10()
    
    embarcacoes = [(3, 1), (2, 2), (1, 3)]  # Define as embarcações disponíveis
    for tamanho, quantidade in embarcacoes:
        for _ in range(quantidade):
            while True:
                linha = random.randint(0, linhas - 1)
                coluna = random.randint(0, colunas - 1)
                orientacao = random.choice(['H', 'V'])
                if verificar_espaco(matriz, linha, coluna, tamanho, orientacao):
                    marcar_embarcacao(matriz, linha, coluna, tamanho, orientacao)
                    break

    return matriz  # Retorna o tabuleiro com as embarcações posicionadas aleatoriamente

# Funções relacionadas ao jogador

def validar_entrada(matriz, linha, coluna, tamanho, orientacao):
    """Valida se a entrada do jogador para posicionar a embarcação é válida."""
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
    return True  # Entrada válida

def pedir_posicoes():
    """Solicita as posições das embarcações ao jogador."""
    posicoes = []  # Lista para armazenar as posições escolhidas pelo jogador
    matriz = criar_matriz_5x10()  # Cria um novo tabuleiro vazio
    
    # Define as embarcações que o jogador deve posicionar
    embarcacoes = [(3, 1), (2, 2), (1, 3)]
    for tamanho, quantidade in embarcacoes:
        for _ in range(quantidade):
            while True:
                try:
                    linha = int(input(f"Posicione sua embarcação de {tamanho} posições:\nLinha (de 0 a 4): "))
                    coluna = int(input("Coluna (de 0 a 9): "))
                    orientacao = 'H' if tamanho == 1 else input("Escolha a orientação (H para horizontal, V para vertical): ").upper()
                    
                    if validar_entrada(matriz, linha, coluna, tamanho, orientacao):
                        marcar_embarcacao(matriz, linha, coluna, tamanho, orientacao)
                        imprimir_matriz(matriz)  # Mostra o tabuleiro atualizado
                        # Adiciona as posições ao vetor de posições
                        posicoes.extend((linha, coluna + i) for i in range(tamanho) if orientacao == 'H')
                        posicoes.extend((linha + i, coluna) for i in range(tamanho) if orientacao == 'V')
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira os valores no formato correto.")
    return posicoes  # Retorna as posições escolhidas pelo jogador

def trocar_valores(matriz, posicoes, valor=1):
    """Troca os valores na matriz de acordo com as posições fornecidas."""
    for linha, coluna in posicoes:
        if 0 <= linha < 5 and 0 <= coluna < 10:
            matriz[linha][coluna] = valor
        else:
            print(f"A posição ({linha}, {coluna}) está fora dos limites da matriz.")
    return matriz

# Funções relacionadas ao jogo em si

def contar_embarcacoes_restantes(matriz):
    """Conta quantas embarcações ainda estão presentes na matriz."""
    return sum(linha.count(1) for linha in matriz)

def ataque_usuario():
    """Solicita e valida o ataque do jogador."""
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
    """Escolhe aleatoriamente um ataque para o computador."""
    linha = random.randint(0, 4)
    coluna = random.randint(0, 9)
    return (linha, coluna)

def imprimir_mensagem(texto):
    """Imprime uma mensagem formatada na tela."""
    print("--------------------------------------------------------------------------")
    print(texto)
    print("--------------------------------------------------------------------------\n")

def jogar():
    """Função principal que inicia o jogo de batalha naval."""
    tabuleiro_jogador = criar_matriz_5x10()  # Cria o tabuleiro do jogador
    tabuleiro_computador = criar_matriz_5x10()  # Cria o tabuleiro do computador
    tela_computador = criar_matriz_5x10()  # Tabuleiro de visualização do computador
    tela_jogador = criar_matriz_5x10()  # Tabuleiro de visualização do jogador

    posicoes_jogador = pedir_posicoes()  # Solicita as posições das embarcações do jogador
    tabuleiro_jogador = trocar_valores(tabuleiro_jogador, posicoes_jogador)  # Marca as posições no tabuleiro do jogador

    tabuleiro_computador = escolher_posicoes_aleatorias()  # Posiciona aleatoriamente as embarcações do computador

    # Mensagem de boas-vindas e apresentação dos tabuleiros
    imprimir_mensagem("Bem vindo ao nosso jogo de BATALHA NAVAL!")

    print("Tabuleiro do Computador após definir embarcações:")
    imprimir_matriz(tabuleiro_computador)
    print("\n")

    print("Tabuleiro do Jogador após definir embarcações:")
    imprimir_matriz(tabuleiro_jogador)
    print("\n")

    while True:
        # Tabuleiro do Computador e interações do jogador
        imprimir_mensagem("Tabuleiro do Computador")
        imprimir_matriz(tela_computador)
        print("--------------------------------------------------------------------------")
        print("Embarcações restantes:", contar_embarcacoes_restantes(tabuleiro_computador))
        print("\n")
        
        # Tabuleiro do Jogador e interações do computador
        imprimir_mensagem("Tabuleiro do Jogador")
        imprimir_matriz(tabuleiro_jogador)
        print("--------------------------------------------------------------------------")
        print("Embarcações restantes:", contar_embarcacoes_restantes(tabuleiro_jogador))
        print("\n")

        # Ataque do jogador
        while True:
            ataque_jogador = ataque_usuario()
            if tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] in ["X", "O"]:
                print("Você já atacou esta posição. Escolha outra.")
                continue
            
            if tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] == 1:
                tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] = "X"
                tela_computador[ataque_jogador[0]][ataque_jogador[1]] = "X"
                imprimir_mensagem(Fore.GREEN + "Você acertou!")

                if contar_embarcacoes_restantes(tabuleiro_computador) == 0:
                    imprimir_mensagem(Fore.GREEN + "Parabéns! Você afundou todas as embarcações do inimigo!")
                    return  # Jogo termina com vitória do jogador
            else:
                tabuleiro_computador[ataque_jogador[0]][ataque_jogador[1]] = "O"
                tela_computador[ataque_jogador[0]][ataque_jogador[1]] = "O"
                imprimir_mensagem(Fore.RED + "Você errou!")
                break

        # Ataque do computador
        while True:
            ataque_computador = escolher_ataque_aleatorio()
            if tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] not in ["X", "O"]:
                break

        print(f"O computador escolheu a linha: {ataque_computador[0]}")
        print(f"O computador escolheu a coluna: {ataque_computador[1]}")
        if tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] == 1:
            tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] = "X"
            tela_jogador[ataque_computador[0]][ataque_computador[1]] = "X"
            imprimir_mensagem(Fore.RED + "Computador acertou!")

            if contar_embarcacoes_restantes(tabuleiro_jogador) == 0:
                imprimir_mensagem(Fore.RED + "Você perdeu! O computador destruiu todas as suas embarcações.")
                return  # Jogo termina com vitória do computador
        else:
            tabuleiro_jogador[ataque_computador[0]][ataque_computador[1]] = "O"
            tela_jogador[ataque_computador[0]][ataque_computador[1]] = "O"
            imprimir_mensagem(Fore.GREEN + "Computador errou!")

# Iniciar o jogo
jogar()
