from Tic_Tac_Toe import Tic_Tac_Toe

class HumanAgent():
    symbol = None
    board = None
    name = None
    def __init__(self, name, board, symbol) -> None:
        self.name = name
        self.symbol = symbol 
        self.board = board

    def move(self):
        valid = False
        while(not valid):
            pos = input("{} enter valid position (x y): ".format(self.name))
            pos = pos.split(" ")
            if(len(pos) != 2):
                print("invalid input!")
                continue
            try:
                pos[0], pos[1] = int(pos[0]),int(pos[1])
            except ValueError:
                print("input not integer!")
                continue
            if(pos[0] < 0 or pos[0]>2 or pos[1] < 0 or pos[1]>2 or (not self.board.empty(pos))):
                print("invalid input!")
                continue
            valid = True
        self.board.set_pos(pos, self.symbol)
    
class AIAgent():
    symbol = None
    board = None
    o_symbol = None
    free = None # 1,2,3,4,5,6,7,8 # 3rows 3cols 2diag
    prev = None

    def __init__(self, board, symbol) -> None:
        self.symbol = symbol 
        self.board = board
        if symbol == 'X':
            self.o_symbol = 'O'
        else:
            self.o_symbol = 'X'
        self.free = [1,2,3,4,5,6,7,8]

    def check(self, index, symbol):
        opp = 0
        pos = [-1,-1]
        if(index in [1,2,3] ):
            for i in range(3):
                if(self.board.board[index-1][i]==symbol):
                    opp+=1
                elif(self.board.board[index-1][i]==' '):
                    pos = [index-1, i]
                else:
                    opp = 0
                    break
        
        elif(index in [4,5,6]):
            for i in range(3):
                if(self.board.board[i][index-4]==symbol):
                    opp+=1
                elif(self.board.board[i][index-4]==' '):
                    pos = [i, index-4]
                    print("in check loop", pos)
                else:
                    opp = 0
                    break
                       
        elif(index ==7):
            for i in range(3):
                if(self.board.board[i][i]==symbol):
                    opp+=1
                elif(self.board.board[i][i]==' '):
                    pos = [i, i]
                else:
                    opp = 0
                    break                 
        else:
            for i in range(3):
                if(self.board.board[2-i][i]==symbol):
                    opp+=1
                elif(self.board.board[2-i][i]==' '):
                    pos = [2-i, i] 
                else:
                    opp = 0
                    break
        if opp == 2:
            print("check pos: ", pos, index)
            return True, pos
        else:
            return False, pos

    def remove(self, pos):
        if(pos == [0,0]):
            rm = [1,4,7]
        elif(pos == [0,1]):
            rm = [1,5]
        elif(pos == [0,2]):
            rm = [1,6,8]
        elif(pos == [1,0]):
            rm = [2,4]
        elif(pos == [1,1]):
            rm = [2,5,7,8]
        elif(pos == [1,2]):
            rm = [2,6]
        elif(pos == [2,0]):
            rm = [3,4,8]
        elif(pos == [2,1]):
            rm = [3,5]
        else:
            rm = [3,6,7]
        self.free = [ele for ele in self.free if ele not in rm]

    def check_win(self):
        for i in range(1,9):
            if i not in self.free:
                win, _pos = self.check(i,self.symbol)
                if win :
                    return win, _pos
        return False, [-1,-1]
    
    def check_loss(self):
        for f in self.free:
            loss, _pos = self.check(f, self.o_symbol)
            if loss:
                return loss, _pos
        return False, [-1,-1]


    def move(self):
        if(self.board.moves == 0): # done
            pos = [0,0]
            
        elif(self.board.moves == 1): #done
            choice = [[1,1], [0,0]]
            for c in choice:
                    if(self.board.empty(c)):
                        pos = c
                        break
        elif(self.board.moves == 2): #done
            if(self.board.empty([2,2])):
                pos = [2,2]
            else:
                pos = [0,2]
        elif(self.board.moves == 3):
            loss, _pos = self.check_loss()
            if loss:
                pos = _pos
            else:
                if self.prev == [1, 1]:
                    choice = [[1,0], [0,1], [2,1],[1,2]]
                else:
                    choice = [[2,2], [2,0], [0,2]]
                for c in choice:
                    if(self.board.empty(c)):
                        pos = c
                        break
        elif(self.board.moves == 4):
            win, _pos = self.check_win()
            if win:
                pos = _pos
            else:
                loss, _pos = self.check_loss()
                if loss:
                    pos = _pos
                else:
                    choice = [[2,0],[0,2],[1,1]] # case [0, 2] should [2, 0] to win # case [2, 2] no need to check
                    for c in choice:
                        if(self.board.empty(c)):
                            pos = c
                            break
        
        else:
            win, _pos = self.check_win()
            if win:
                pos = _pos
            else:
                loss, _pos = self.check_loss()
                if loss:
                    pos = _pos
                else:
                    found = False
                    for i in range(3):
                        if found:
                            break
                        for j in range(3):
                            if self.board.empty([i,j]):
                                pos = [i,j]
                                found = True
                                break
        self.prev = pos
        self.remove(pos)
        print(self.free)
        self.board.set_pos(pos, self.symbol)