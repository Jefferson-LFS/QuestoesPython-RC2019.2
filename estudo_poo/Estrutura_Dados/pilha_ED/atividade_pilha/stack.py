class Stack:
    def __init__ (self):
        self.__data = []

    def getStack(self):
        return self.__data

    def push(self, newValue):
        self.__data.append(newValue)

    def pop(self):
        return self.__data.pop()

    def isEmpty(self):
        return self.__data == []

    def peek(self):
        return self.__data[len(self.__data) - 1]

    def size(self):
        while (len(self.__data) != 0):
            self.__data.pop()

