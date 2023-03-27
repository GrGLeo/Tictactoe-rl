import numpy as np

class Game:
    def __init__(self):
        self.board = np.zeros(shape=(3,3))
        self.player = 1
        self.bot = 2

    def move(self,x,y):
        # player move
        if self.board[y,x] == 0:
            self.board[y,x] = self.player
        else:
            return print("Illegal move, try another one")


        # bot move
        count = 0
        while True:
            x = np.random.randint(low=0,high=3)
            y = np.random.randint(low=0,high=3)
            if self.board[y,x] == 0:
                self.board[y,x] = self.bot
                break
            count += 1
            if count >20:
                print("No place left!")
                break


    def game_state(self):
        for row in self.board:
            if (row == 1).all():
                return True
            elif (row == 2).all():
                return True

        for col in self.board.T:
            if (col == 1).all():
                return True
            elif (col == 2).all():
                return True

        if (self.board.diagonal() == 1).all():
            return True
        elif (self.board.diagonal() == 2).all():
            return True

        if (self.board[[0,1,2],[2,1,0]] == 1).all():
            return True
        elif (self.board[[0,1,2],[2,1,0]] == 2).all():
            return True


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
