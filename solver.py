import time
from Queue import PriorityQueue
import itertools


class Solver:
    def __init__(self, problem, algorithm):
        self.num_visited = 0
        self.algorithm = algorithm
        self.problem = problem
        self.max_mem = -1

    def solve(self):
        result = None
        start = time.time()
        print 'Algoritmo:', self.algorithm

        if self.algorithm == 'BFS':
            result = self.BFS()
        elif self.algorithm == 'IDFS':
            result = self.IDFS()
        elif self.algorithm == 'UCS':
            result = self.UCS()
        elif self.algorithm == 'A* 0':
            result = self.ASTAR(0)
        elif self.algorithm == 'A* 1':
            result = self.ASTAR(1)

        print 'Nodos visitados:', self.num_visited
        print 'Nodos na memoria:', self.max_mem
        print 'Tempo total:', time.time() - start, 'segundos'
        print 'Resultado:', result
        print

    def BFS(self):
        queue = [[self.problem.tabuleiro, ""]]
        visitados = []

        while queue:
            self.num_visited += 1
            if self.max_mem < len(queue):
                self.max_mem = len(queue)

            node, caminho = queue.pop(0)
            visitados.append(node)

            if self.problem.testeObjetivo(node):
                return caminho

            for suc, move in self.problem.sucessores(node):
                if suc not in visitados:
                    queue.append([suc, caminho + move])

    def DLS(self, profundidade_maxima):
        queue = [[self.problem.tabuleiro, ""]]
        visitados = []

        while queue:
            self.num_visited += 1
            if self.max_mem < len(queue):
                self.max_mem = len(queue)

            node, caminho = queue.pop(len(queue) - 1)
            visitados.append(node)

            if self.problem.testeObjetivo(node):
                return caminho

            for suc, move in self.problem.sucessores(node):
                if suc not in visitados:
                    if len(caminho) <= profundidade_maxima:
                        queue.append([suc, caminho + move])

    def IDFS(self):
        for i in itertools.count():
            result = self.DLS(i)
            if result:
                return result

    def UCS(self):
        queue = PriorityQueue()
        queue.put([0, self.problem.tabuleiro, ''])
        visitados = []

        while queue:
            self.num_visited += 1
            if self.max_mem < queue.qsize():
                self.max_mem = queue.qsize()

            custo, node, caminho = queue.get_nowait()
            visitados.append(node)

            if self.problem.testeObjetivo(node):
                return caminho

            for suc, move in self.problem.sucessores(node):
                if suc not in visitados:
                    queue.put([custo + 1, suc, caminho + move])

    def heuristic_manhattan(self, tab):
        tabuleiro = tab[::-1]
        for i in range(0, len(tabuleiro) - 1):
            if tabuleiro[i] == 0:
                x = divmod(i, self.problem.n)
                if x:
                    return int(x[0] + x[1])
        return 0

    def heuristic_full_manhattan(self, tab):
        total = 0
        matriz = []

        for i in range(self.problem.n):
            matriz.append(tab[i * self.problem.n: i * self.problem.n + self.problem.n])

        for f in self.problem.final:
            for i in range(self.problem.n):
                for j in range(self.problem.n):
                    num = i * i + j + i + 1
                    num = num if num != self.problem.n * self.problem.n else 0
                    if f == num:
                        num = matriz[i][j] - 1 if matriz[i][j] != 0 else self.problem.n * self.problem.n - 1
                        x, y = divmod(num, self.problem.n)
                        total += abs(x - i) + abs(y - j)
        return total / 2

    def ASTAR(self, heuristic):
        queue = PriorityQueue()
        queue.put([0, self.problem.tabuleiro, ''])
        visitados = []

        while not queue.empty():
            self.num_visited += 1
            if self.max_mem < queue.qsize():
                self.max_mem = queue.qsize()

            custo, node, caminho = queue.get_nowait()
            visitados.append(node)

            if self.problem.testeObjetivo(node):
                return caminho

            for suc, move in self.problem.sucessores(node):
                if suc not in visitados:
                    if heuristic == 1:
                        queue.put([self.heuristic_manhattan(suc) + custo + 1, suc, caminho + move])
                    else:
                        queue.put([self.heuristic_full_manhattan(suc) + custo + 1, suc, caminho + move])