# import numpy as np
class Tic_Tac_Toe:
    board = None
    moves = 0

    def __init__(self) -> None:
        self.board = [[' ']*3 for i in range(3)]
        self.print_board()
        self.moves = 0

    def clear(self) ->None:
        print("reseting board")
        self.board = [[' ']*3 for i in range(3)]
        self.print_board()
        self.moves=0

    def print_board(self) ->None:
        str = "-------\n|{}|{}|{}|\n-------\n|{}|{}|{}|\n-------\n|{}|{}|{}|\n-------"\
            .format(self.board[0][0],self.board[0][1],self.board[0][2],\
                    self.board[1][0],self.board[1][1],self.board[1][2],\
                    self.board[2][0],self.board[2][1],self.board[2][2])
        print(str)
    
    def check_routes(self, pos, symbol):
        if((pos[0] == 0 and pos[1] == 0) or (pos[0] == 2 and pos[1] == 2) or (pos[0] == 1 and pos[1] == 1)):
            if self.board[(pos[0]+1)%3][(pos[1]+1)%3]==symbol and self.board[(pos[0]+2)%3][(pos[1]+2)%3] == symbol:
                return True
        if (pos[0] == 1 and pos[1] == 1) or (pos[0] == 0 and pos[1] == 2) or (pos[0] == 2 and pos[1] == 0) :
            if self.board[(pos[0]-1)%3][(pos[1]+1)%3]==symbol and self.board[(pos[0]-2)%3][(pos[1]+2)%3] == symbol:
                return True   
        if self.board[(pos[0]+1)%3][pos[1]] == symbol and self.board[(pos[0]+2)%3][pos[1]] == symbol:
            return True
        if self.board[pos[0]][(pos[1]+1)%3] == symbol and self.board[pos[0]][(pos[1]+2)%3] == symbol:
            return True
        return False
                

    def terminate(self, pos, symbol):
        term = self.check_routes(pos, symbol)
        if term:
            print("player {} win!".format(symbol))
        elif self.moves == 9:
            print("Draw!")
        

    def set_pos(self, pos, symbol):
        if (symbol != 'X' and symbol != 'O'):
            print("invalid symbol")
            return 
        if (len(pos) != 2 or pos[0]<0 or pos[0]>=3 or pos[1]<0 or pos[1]>=3 or self.board[pos[0]][pos[1]]!=' '):
            print("invalid pos")
            return
        self.board[pos[0]][pos[1]] = symbol
        self.moves+=1
        self.print_board()
        self.terminate(pos, symbol)
        