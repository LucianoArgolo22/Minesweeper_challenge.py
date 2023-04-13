#%%
from typing import List
import sys

class Board:
    """
    Represents a Minesweeper board of a given size.

    Attributes:
    - size (int): the size of the board
    - board (list): a 2D list representing the cells of the board
    """

    def __init__(self, size: int) -> None:
        """
        Initializes a new Board object with a given size.
        All cells are initialized with the value '0'.

        Args:
        - size (int): the size of the board
        """
        self.size = size
        self.board = self.generate_board()
        
    def generate_board(self) -> list:
        """
        Initializes the dashboard, leaving everything in 0.
        
        Returns:
        - A list of lists, that represent the dashboard.
        """
        return [['0' for j in range(self.size)] for i in range(self.size)]

    def __str__(self) -> str:
        """
        Returns a string representation of the board.

        Returns:
        - A string representing the board, with each row separated by a newline character.
        """
        return '\n'.join([''.join(row) for row in self.board])
    
    def add_bomb(self, row: int, col: int) -> None:
        """
        Adds a bomb to the board at a given position.

        Args:
        - row (int): the row index of the cell to add a bomb
        - col (int): the column index of the cell to add a bomb
        """
        if self.board[row][col] != '0':
            raise ValueError("Cell already contains a bomb, locations of the bombs must be unique")
        self.board[row][col] = 'B'
    
    def calculate_neighbors(self) -> None:
        """
        iterates through each cell on the board.
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != 'B':
                    self.count_bombs_in_surroundings(i=i, j=j)
    
    def count_bombs_in_surroundings(self, i:int, j:int) -> None:
        """
        Calculates the bombs in the (i, j) coordinates surroundings
        it just does a sweep looking for bombs, and saves the total bombs found in (i, j) position
        """
        count:int = 0
        for r in range(max(0, i-1), min(self.size, i+2)):
            for c in range(max(0, j-1), min(self.size, j+2)):
                if (i, j) != (r, c):
                    if self.board[r][c] == 'B':
                        count += 1
        self.board[i][j] = str(count)


class Game:
    """
    Minesweeper game.
    """
    def __init__(self, N: int, R: List[int], C: List[int]):
        """
        Constructs all the necessary attributes for the Game object.

        N : int - this is the size of the board.
        R : List[int] - a list of the rows coordinates of bombs.
        C : List[int] - a list of the columns coordinates of bombs.
        """
        self.N = N
        self.R = R
        self.C = C
        self.board = self.creating_board()
        self.placing_bombs()

    def creating_board(self) -> list:
        """
        Generates board if validations are ok
        """
        if self.game_validations():
            return Board(self.N)
        return None

    def game_validations(self) -> bool:
        """
        Validations or conditions for the game
        """
        if not isinstance(self.N, int):
            raise TypeError("N must be an integer")
        elif not isinstance(self.C, list):
            raise TypeError("C (columns) must be a list")
        elif not isinstance(self.R, list):
            raise TypeError("R (rows) must be a list")
        elif self.N <= 0 or self.N > 20:
            raise ValueError("N must be an integer within the range [1..20]")
        elif len(self.R) != len(self.C):
            raise ValueError("Coordinates of bombs must be equal length")   
        elif len(self.R) > self.N**2 or len(self.C) > self.N**2:    
            raise ValueError(f"Bombs must be within the range of [0..{self.N**2}]")
        return True

    def placing_bombs(self) -> None:
        """
        Setter for bombs in dashboard.
        """
        for i in range(len(self.R)):
            row, col = self.R[i], self.C[i]
            if not (0 <= row < self.N) or not (0 <= col < self.N):
                raise ValueError(f"Invalid cell coordinates, each element of arrays R, C should be an integer within the range [0..{self.N-1}]")
            self.board.add_bomb(row, col)
            
    def play(self) -> None:
        """
        Calculates the number of bomb neighbors for each cell in the board and prints it.
        """
        self.board.calculate_neighbors()
        for row in self.board.board:
            row = ''.join(row)
            sys.stdout.write(f'{row}\n')

def solution(N:int, R:int, C:int) -> None:
    game = Game(N=N, R=R, C=C)
    game.play()


if __name__ == '__main__':
    #Given 
    n = 5
    r = [2, 3, 2, 3, 1, 1, 3, 1] 
    c = [3, 3, 1, 1, 1, 2, 2, 3] 
    #function should print: 12321 2BBB2 3B8B3 2BBB2 12321 
    solution(N=n, R=r, C=c)