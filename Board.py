class Board(object):
    __player = ''
    __board = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
               [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
               [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
               [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
               [1, 3, 1, 0, 0, 0, 1, 0, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
               [1, 3, 0, 0, 1, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def __init__(self):
        self.__height = len(self.__board)
        self.__width = len(self.__board[0])
        self.__direction = ''
        self.__gameState = 0

    def getDirection(self):
        return self.__direction

    def directionState(self, enter):
        lst = ['N', 'S', 'E', 'W']
        if enter in lst:
            return True
        else:
            print('error')
            self.move()

    def getPlayer(self):
        return self.__player

    def initialBoard(self):
        return self.__board

    def getBoard(self):
        partial = []
        for i in self.__board:
            lst = []
            for j in i:
                if j == 1:
                    lst.append('X')
                elif j == 0:
                    lst.append('.')
                elif j == 3:
                    lst.append('#')
                elif j == 4:
                    lst.append('P')
            partial.append(lst)
        for i in partial:
            print(' '.join(i))

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def userPosition(self):
        userPosition = []
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__board[i][j] == 4:
                    userPosition.append(i)
                    userPosition.append(j)
        return userPosition

    def setPlayer(self, other):
        self.__player = other

    def setHeight(self, other):
        self.__height = other

    def setBoard(self, x, y):
        self.__board[x][y] = 4

    def setWidth(self, other):
        self.__width = other

    def move(self):
       self.__direction = input('Direction:')

       if self.directionState(self.__direction):
            self.canPlay(self.__direction, self.userPosition())

    def changeBoard(self, newBoard):
        self.__board=newBoard

    def getGameState(self):
        return self.__gameState

    def setGameState(self, position):
        if position == 3:
            self.__gameState += 1
        else:
            return False

    def reload(self):
        self.__gameState=0

    def canPlay(self, position, userPosition):

        if position == 'N':
            if self.__board[userPosition[0] - 1][userPosition[1]] != 1:
                self.setGameState(self.__board[userPosition[0] - 1][userPosition[1]])

                self.__board[userPosition[0]][userPosition[1]] = 0
                self.__board[userPosition[0] - 1][userPosition[1]] = 4
            else:
                return False

        if position == 'S':
            if self.__board[userPosition[0] + 1][userPosition[1]] != 1:
                self.setGameState(self.__board[userPosition[0] + 1][userPosition[1]])

                self.__board[userPosition[0]][userPosition[1]] = 0
                self.__board[userPosition[0] + 1][userPosition[1]] = 4

            else:
                return False
        if position == 'E':
            if self.__board[userPosition[0]][userPosition[1] + 1] != 1:
                self.setGameState(self.__board[userPosition[0]][userPosition[1] + 1])

                self.__board[userPosition[0]][userPosition[1]] = 0
                self.__board[userPosition[0]][userPosition[1] + 1] = 4
            else:
                return False

        if position == 'W':
            if self.__board[userPosition[0]][userPosition[1] - 1] != 1:
                self.setGameState(self.__board[userPosition[0]][userPosition[1] - 1])

                self.__board[userPosition[0]][userPosition[1]] = 0
                self.__board[userPosition[0]][userPosition[1] - 1] = 4

            else:
                return False
