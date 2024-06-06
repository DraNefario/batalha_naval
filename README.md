# Batalha Naval (Grupo 1)

Desenvolvimento de um jogo (Batalha Naval) programado em Python utilizando os conceitos aprendidos em sala.

Orientadora: Marina de Lara

Projeto: PjBL 2

# O que é Batalha Naval?

A Batalha Naval é um clássico jogo de tabuleiro de estratégia para dois jogadores, frequentemente jogado tanto em versões físicas quanto digitais. A essência do jogo está na habilidade dos jogadores em ocultar seus navios e ao mesmo tempo descobrir as posições dos navios adversários, criando uma emocionante combinação de sorte e estratégia.

# Requisitos principais necessários solicitados para o funcionamento do jogo
1. Modo Humano vS. Computador.
2. Matriz 10x10.
3. Feedbacks in-game impressos no console.
4. Matriz com valores escondidos.
5. Embarcações devem ocupar um único espaço na matriz.
6. No mínimo 5 embarcações devem ser inseridas.
7. Ao iniciar o jogo, o programa deve solicitar ao jogador a coordenada de suas embarcações.
8. As coordenadas do computador devem ser definidas de maneira randômica.
9. Coordenadas devem ser armazenadas em uma matriz escondida.
10. Mostrar os tabuleiros do jogador e do computador sem revelar a posição do computador.
11. Solicitar ataque do jogador através de linhas e colunas.
12. As matrizes deverão ser atualizadas após cada ataque (jogador e computador).
13. Não é permitido atacar uma mesma posição.
14. Caso o ataque de uma embarcação seja bem-sucedido, o espaço acertado deve ser preenchido com 'X'
15. Caso o ataque de uma embarcação não seja bem-sucedido, o espaço acertado deve ser preenchido com 'O' para indicar o local que foi atacado.
16. Mostrar as embarcações restantes de cada jogador e suas atualizações a cada ataque.
17. Quando um dos jogadores conseguir afundar toda a tropa do adversário, o programa deve informar a vitória do jogador vencedor, exibir agradecimentos ao jogador humano, os nomes dos integrantes da equipe e finalizar o programa.


# Estruturação do Código


# Conceitos utilizados
1. Estruturas de repetição (for, while)
   - Foram usadas para iterar sobre as posições do tabuleiro durante a configuração das embarcações e durante o jogo, permitindo que os jogadores posicionem suas embarcações e façam ataques.
2. Biblioteca random
   - Utilizada para escolher posições aleatórias no tabuleiro durante a configuração das embarcações do computador e durante os ataques aleatórios.
3. Funções
   - Foram usadas para dividir o código em blocos reutilizáveis que executa todo o jogo, e outras funções auxiliares para pedir posições, fazer ataques, etc.
4. Matrizes
   - Representam os tabuleiros do jogo, permitindo armazenar e manipular as posições das embarcações e os resultados dos ataques.
5. Blocos "try" e "Except"
   - Foram usados para lidar com exceções durante a entrada de dados, garantindo que o programa não quebre se o usuário fornecer uma entrada inválida.
6. Estruturas condicionais (if, elif, else)
    - Controlam o fluxo do jogo com base nas ações dos jogadores e nos resultados dos ataques, determinando se um ataque acertou uma embarcação, se o jogo acabou, etc.
7. Exceção "ValueError"
    - Procura erros de entrada quando os jogadores fornecem valores inválidos para as posições das embarcações ou para os ataques.
8. Operadores (not, and, not in, ...)
    - Foram usados em expressões lógicas para verificar se uma posição já foi atacada, se uma embarcação foi atingida, etc.
9. Variáveis Booleanas
    - Foram usadas para controlar o estado do jogo, como determinar se uma embarcação foi afundada ou se o jogo terminou.
10. Instrução "break"
    - Utilizada para sair dos loops de forma controlada, como quando o jogo termina ou quando uma condição específica é encontrada durante o jogo.

# Autores:
André Luís Scharaiber Alves

Danillo Gonçalves Camargo da Silva

Samuel Bottesini Lot

Thomas Manussadjian Steinhausser
