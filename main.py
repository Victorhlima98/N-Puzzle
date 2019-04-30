from npuzzle import NPuzzle
from solver import Solver

if __name__ == '__main__':
    npuzzle = NPuzzle(5)
    npuzzle.embaralhar(35)
    npuzzle.print_puzzle()
    Solver(npuzzle, 'BFS').solve()
    Solver(npuzzle, 'IDFS').solve()
    Solver(npuzzle, 'UCS').solve()
    Solver(npuzzle, 'A* 0').solve()  # full_manhattan
    Solver(npuzzle, 'A* 1').solve()  # manhattan