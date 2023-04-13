

from unittest import TestCase
from typing import List
from minesweeper import Board, Game

class TestGame(TestCase):
    #1. Given N = 3, R = [2, 1, 0, 2] and C = [0, 2, 1, 2]
    #  your function should print: 1B2 24B B3B 
    def test_case_1(self):
        n = 3
        r = [2, 1, 0, 2]
        c = [0, 2, 1, 2]
        game = Game(N=n, R=r, C=c)
        game.play()
        self.assertEqual(str(game.board), '1B2\n24B\nB3B')
    
    #2. Given N = 5, R = [2, 3, 2, 3, 1, 1, 3, 1] and C = [3, 3, 1, 1, 1, 2, 2, 3],
    #  your function should print: 12321 2BBB2 3B8B3 2BBB2 12321 
    def test_case_2(self):
        n = 5
        r = [2, 3, 2, 3, 1, 1, 3, 1]
        c = [3, 3, 1, 1, 1, 2, 2, 3]
        game = Game(N=n, R=r, C=c)
        game.play()
        self.assertEqual(str(game.board), '12321\n2BBB2\n3B8B3\n2BBB2\n12321')

    #3. Given N = 2, R = [] and C = [], your function should print: 
    #00 00 
    #There are no bombs. 
    def test_case_2(self):
        n = 2
        r = []
        c = []
        game = Game(N=n, R=r, C=c)
        game.play()
        self.assertEqual(str(game.board), '00\n00')

    #some more test cases of my own
    def test_case_3(self):
        game = Game(3, [0, 1], [1, 0])
        game.play()
        self.assertEqual(str(game.board), '2B1\nB21\n110')

    def test_case_3(self):
        game = Game(2, [0, 1], [1, 0])
        game.play()

class TestValidations(TestCase):   
    #N is an integer within the range [1..20]; 
    #N in this case is not int 
    def test_game_validations_N_type(self):
        with self.assertRaises(TypeError):
            game = Game("abc", [], [])
            game.game_validations()
            
    #N is an integer within the range [1..20]; 
    #N in this case is both lower than 1 and bigger than 20
    def test_game_validations_N_value(self):
        with self.assertRaises(ValueError):
            game = Game(0, [], [])
            game.game_validations()
    
        with self.assertRaises(ValueError):
            game = Game(21, [], [])
            game.game_validations()

    #M is an integer within the range [0..N*N]
    #coordinates of M are not int
    def test_game_validations_C_and_R_type(self):
        with self.assertRaises(TypeError):
            game = Game(5, [], "abc")
            game.game_validations()
            
        with self.assertRaises(TypeError):
            game = Game(5, "abc", [])
            game.game_validations()

    #M is an integer within the range [0..N*N]
    #coordinates of M are not same length     
    def test_game_validations_R_C_length(self):
        with self.assertRaises(ValueError):
            game = Game(5, [0, 1, 2], [0, 1])
            game.game_validations()

    #M is an integer within the range [0..N*N]
    #coordinates of M are not in the range [0..N*N]    
    def test_game_validations_R_C_value(self):
        with self.assertRaises(ValueError):
            game = Game(2, [6, 1, 2, 7, 8], [0, 1, 2, 4, 5, 6])
            game.game_validations()
            
    #each element of arrays R, C is an integer within the range [0..N-1]
    #R, C is an not an integer within the range [0..N-1]
    def test_game_validations_R_C_value2(self):
        with self.assertRaises(ValueError):
            game = Game(5, [0, 1, 2], [6, 1, 2])
            game.game_validations()
            
        with self.assertRaises(ValueError):
            game = Game(5, [0, 1, 6], [0, 1, 2])
            game.placing_bombs()

    #locations of the bombs are unique.
    #in this case bombs repeat
    def test_add_bomb(self):
        board = Board(3)
        board.add_bomb(1, 1)
        with self.assertRaises(ValueError):
            board.add_bomb(1, 1)

class TestBoard(TestCase):
    def test_init(self):
        board = Board(3)
        self.assertEqual(board.size, 3)
        self.assertEqual(board.board, [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']])

    def test_add_bomb(self):
        board = Board(3)
        board.add_bomb(1, 1)
        self.assertEqual(board.board, [['0', '0', '0'], ['0', 'B', '0'], ['0', '0', '0']])

    def test_calculate_neighbors(self):
        board = Board(3)
        board.add_bomb(0, 1)
        board.add_bomb(1, 0)
        board.calculate_neighbors()
        self.assertEqual(board.board, [['2', 'B', '1'], ['B', '2', '1'], ['1', '1', '0']])
