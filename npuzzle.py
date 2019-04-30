from random import randint


class NPuzzle:
    tabuleiro = []
    final = []

    def __init__(self, n):
        self.n = n
        self.tabuleiro = range(1, self.n * self.n)
        self.tabuleiro.append(0)
        self.final = self.tabuleiro

    def print_puzzle(self):
        for i in range(self.n):
            print (self.tabuleiro[i * self.n:i * self.n + self.n])

    def embaralhar(self, x):
        seq = ''
        anterior = ''
        for _ in range(x):
            suc = self.sucessores(self.tabuleiro)

            for i in range(len(suc) - 1):
                if 'B' in suc[i][1] and anterior == 'C':
                    suc.pop(i)
                if 'C' in suc[i][1] and anterior == 'B':
                    suc.pop(i)
                if 'D' in suc[i][1] and anterior == 'E':
                    suc.pop(i)
                if 'E' in suc[i][1] and anterior == 'D':
                    suc.pop(i)

            i = randint(0, len(suc) - 1)
            self.tabuleiro = suc[i][0]
            seq += suc[i][1]
            anterior = suc[i][1]
        return seq

    def testeObjetivo(self, estado):
        return estado == self.final

    def sucessores(self, estado):
        dir = self.mover(estado, "D")
        esq = self.mover(estado, "E")
        cima = self.mover(estado, "C")
        baixo = self.mover(estado, "B")

        lista_suc = []

        if dir: lista_suc.append([dir, "D"])
        if esq: lista_suc.append([esq, "E"])
        if cima: lista_suc.append([cima, "C"])
        if baixo: lista_suc.append([baixo, "B"])

        return lista_suc

    def mover(self, estado, direcao):
        indice = 0
        count = 0
        N = len(estado)
        novo_estado = estado[:]
        for i in estado:
            if i == 0:
               indice = count
            count += 1

        if direcao == "C":  # Cima
            if indice not in range(0, self.n):
                temp = novo_estado[indice - self.n]
                novo_estado[indice - self.n] = novo_estado[indice]
                novo_estado[indice] = temp
                return novo_estado
            else:
                return False
        if direcao == "B":  # Baixo
            if indice not in range((N-self.n), N):
                temp = novo_estado[indice + self.n]
                novo_estado[indice + self.n] = novo_estado[indice]
                novo_estado[indice] = temp
                return novo_estado
            else:
                return False

        if direcao == "E":  # Esquerda
            if indice not in range(0, N, self.n):
                temp = novo_estado[indice - 1]
                novo_estado[indice - 1] = novo_estado[indice]
                novo_estado[indice] = temp
                return novo_estado
            else:
                return False

        if direcao == "D":  # Direita
            if indice not in range((self.n - 1), N, self.n):
                temp = novo_estado[indice + 1]
                novo_estado[indice + 1] = novo_estado[indice]
                novo_estado[indice] = temp
                return novo_estado
            else:
                return False
