class Pilha:
    def __init__ (self):
        self.__dados = []

    def getPilha(self):
        return self.__dados

    def push(self, novoValor):
        self.__dados.append(novoValor)

    def pop(self):
        self.__dados.pop()

    def esvaziar(self):
        while (len(self.__dados) != 0):
            self.__dados.pop()

