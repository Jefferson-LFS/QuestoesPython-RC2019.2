class Estacinamento:
    def __init__ (self):
        self.dados = []

    def getFila(self):
        return self.dados

    def inserirDado(self, novoValor):
        self.dados.append(novoValor)

    def removerPosicao(self, valor):
        pos = self.dados.index(valor)
        for i in range(0, pos):
            self.dados.append(self.dados[i])
        for i in range(0, pos + 1):
            self.dados.pop(0)

    def tamanhoFila(self):
        return len(self.dados)