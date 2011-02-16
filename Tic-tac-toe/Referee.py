from Tic_Tac_Toe import Tic_Tac_Toe
from TTT_Agent import AIAgent, HumanAgent
class Referee:
    board = None
    def __init__(self) -> None:
        print("Game start, X first O next")
        self.board = Tic_Tac_Toe()
    
    def play(self):
        while(True):
            p1 = input("P1 type:")
            p2 = input("P2 type:")
            if(p1 == "AI"):
                p1 = AIAgent( self.board, 'X')
            else:
                p1 = HumanAgent("P1",self.board, 'X')
            if(p2 == "AI"):
                p2 = AIAgent(self.board, 'O')
            else:
                p2 = HumanAgent("P2", self.board, 'O')    
            while(True):
                input("press any key to start")
                next_p = p1
                while(not self.board.terminate):
                    next_p.move()
                    if(next_p == p1):
                        next_p = p2
                    else:
                        next_p = p1
                cont = input("Game end, press c to restart, press x to select players, else to exit")
                
                if(cont == "c"):
                    self.board.clear()
                elif(cont == "x"):
                    del p1
                    del p2 
                    self.board.clear()
                    break
                else:
                    exit()
            
            

    