import Board
import Player
import Square
import LevelTwo
import LevelThree


class Labyrinth(object):
    __board = []
    play = 1

    def __init__(self):
        self.__name = input("Player's name:")

    def play(self):
        current_level=0
        level=[LevelTwo.two(),LevelThree.three()]
        player = Player.Player(self.__name, 1, 1)

        board = Board.Board()

        board.setPlayer(player)
        board.setBoard(1, 1)
        board.getBoard()

        while self.play:
            board.move()
            board.getBoard()
            if board.getGameState() == 2:
                current_level+=1
                print("félicitations level "+str(current_level)+" terminé")
                if len(level) == current_level - 1:
                    print("Vous avez terminé le jeu. A bientôt pour de nouvelles aventures")
                    break

                else:
                    board.changeBoard(level[current_level-1])
                    print("Level "+ str(current_level+1))
                    board.getBoard()
                    board.reload()



a = Labyrinth()
a.play()
