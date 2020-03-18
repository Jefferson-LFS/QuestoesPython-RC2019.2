class Queue:
    def __init__ (self):
        self.data = []

    def getQueue(self):
        return self.data

    def inData(self, newValue):
        self.data.append(newValue)

    def deQueue(self):
        self.data.pop(0)

    def dePosicion(self, value):
        pos = self.data.index(value)
        for i in range(0, pos+1):
            self.data.pop(0)

    def sizeQueue(self):
        return len(self.dados)
