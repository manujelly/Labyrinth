class Player(object):

    def __init__(self, name, Llocation, Clocation):
        self.__name = name
        self.__Llocation = Llocation
        self.__Clocation = Clocation

    def getName(self):
        return self.__name

    def setName(self, other):
        self.__name = other

    def getLlocation(self):
        return self.__Llocation

    def setLlocation(self, other):
        self.__Llocation = other

    def getClocation(self):
        return self.__Clocation

    def setClocation(self, other):
        self.__Clocation=other

