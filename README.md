## N-Puzzle
 Neste repositório encontra-se os códigos de buscas(BFS, DLS, IDFS, A*), desenvolvidos na cadeira de inteligência artificial com linguagem de programação Python.

## n-puzzle. py 
Esta classe é responsável por conter todos os mecanismos do jogo, como movimentos, sucessores, estado objetivo, embaralhamento e entre outras funções responsáveis pelo o funcionamento do jogo

## solver. py
Classe que contém todos os algoritmos de busca, responsáveis pela escolha da melhor solução para chegar no estado objetivo. Obviamente que cada algoritmo possuiu suas limitações.

## main. py
Esta classe é responsável por disparar os métodos das classes solver e n-puzzle, onde chamamos o método NPuzzle() que retrata o tamanho do tabuleiro bastando passar um número (3) como parâmetro de entrada e os métodos da classe Solver, responsáveis por utilizar todos os algoritmos de buscas contidos nela.

