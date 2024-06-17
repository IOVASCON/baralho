# Jogo de Cartas com Tkinter

Este projeto é uma simulação de um jogo de cartas entre dois jogadores, onde cada jogador recebe uma mão de cartas aleatórias e disputa para ver quem tem a maior carta em cada rodada. O jogo é implementado em Python com uma interface gráfica usando Tkinter.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

baralho/
│
├── utils/
│ ├── init.py
│ ├── baralho.py
│
├── main.py
├── README.md

### Arquivos

- `utils/baralho.py`: Contém a lógica do jogo, incluindo a geração das mãos, comparação das cartas e determinação do vencedor.
- `main.py`: Implementa a interface gráfica usando Tkinter e interage com a lógica do jogo definida em `utils/baralho.py`.
- `README.md`: Este arquivo, que descreve o projeto.

#### Instalação

1. Clone o repositório:
  
    git clone [https://github.com/SEU_USUARIO/baralho.git]

2. Navegue até o diretório do projeto:

    cd baralho

3. Certifique-se de que você tem o Python instalado (versão 3.x). Você pode verificar a instalação do Python usando:

    python --version

##### Execução

Para executar o projeto, basta rodar o arquivo `main.py`:

python main.py

### Funcionalidades

    Gerar Mãos de Cartas: Gera aleatoriamente uma mão de 10 cartas para cada jogador.
    Exibir Cartas: Converte os índices das cartas para suas representações (e.g., 11 para J).
    Comparar Cartas: Compara as cartas das mãos dos jogadores e conta os pontos para cada um.
    Determinar Vencedor: Determina o vencedor com base nos pontos de cada jogador.
    Interface Gráfica: Interface gráfica simples usando Tkinter que permite aos usuários jogar o jogo com um clique de botão.

### Exemplo de Saída

Ao clicar no botão "Jogar", as mãos dos jogadores são geradas e comparadas, e o resultado é exibido em uma caixa de mensagem. Aqui está um exemplo de saída:

Jogador A: ['6', '2', '9', '4', '10', 'Q', '8', '5', '7', 'A']
Jogador B: ['Q', '9', '4', 'A', '5', '8', '6', '3', '10', 'J']
Jogador A venceu: 6 x 4!

## Explicação dos Códigos

utils/baralho.py

    baralho: Um dicionário que mapeia valores numéricos para suas representações de carta.
    gerar_maos(n=10): Gera duas mãos de cartas aleatórias, cada uma com n cartas, e retorna como tuplas.
    exibir_cartas(mao): Converte os índices das cartas para suas representações (e.g., 11 para J).
    comparar_maos(mao_a, mao_b): Compara as cartas das duas mãos carta a carta e conta os pontos para cada jogador.
    determinar_vencedor(pontos_a, pontos_b): Determina o vencedor com base nos pontos de cada jogador e retorna uma string com o resultado.

main.py

    jogar(): Função que é chamada quando o botão "Jogar" é clicado. Gera mãos de cartas para os jogadores, compara e exibe o resultado em uma caixa de mensagem.
    Configuração do Tkinter: Define a janela principal, um título e um botão "Jogar". Quando o botão é clicado, a função jogar é chamada para executar a lógica do jogo.
