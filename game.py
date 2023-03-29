import numpy as np

class Game:
    def __init__(self):
        self.board = np.zeros(shape=(3,3),dtype=np.uint8)
        self.player = 1
        self.bot = 2

    def move(self,x,y):
        """Take in, placement with x and y on the game board. \n
        Return if move was illegal, and state of the board after the move"""
        # player move
        if self.board[y,x] == 0:
            self.board[y,x] = self.player
        else:
            return True,tuple(self.board.flatten())


        # bot move randomly
        x_pos,y_pos = np.where(self.board == 0)
        if len(x_pos) > 0:
            pos = np.random.randint(len(x_pos))
            x = x_pos[pos]
            y = y_pos[pos]
            self.board[x,y] = self.bot

        return False,tuple(self.board.flatten())

    def game_state(self):
        """Check if the game is won or lost. \n
        Return if game is done, the reward +10 if won, -10 if lost, -1 if game continues \n
        And if game is won or not"""
        for row in self.board:
            if (row == 1).all():
                return (True, 10, True)
            elif (row == 2).all():
                return (True, -10, False)

        for col in self.board.T:
            if (col == 1).all():
                return (True, 10, True)
            elif (col == 2).all():
                return (True, -10, False)

        if (self.board.diagonal() == 1).all():
            return (True, 10, True)
        elif (self.board.diagonal() == 2).all():
            return (True, -10, False)

        if (self.board[[0,1,2],[2,1,0]] == 1).all():
            return (True, 10, True )
        elif (self.board[[0,1,2],[2,1,0]] == 2).all():
            return (True, -10, False)

        if (self.board != 0).all():
            return (True, -10, False)

        return (False,-1, False)

if __name__ == "__main__":
    game = Game()

    done = False
    while not done:
        x = int(input())
        y = int(input())

        game.move(x,y)
        done = game.game_state()
        print(game.board)
    print("Game done")
