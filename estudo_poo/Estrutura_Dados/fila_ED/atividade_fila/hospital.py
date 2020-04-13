class Hospital:
    def __init__ (self):
        self.dados = []

    def getFila(self):
        return self.dados

    def inserirPaciente(self, novoValor):
        self.dados.append(novoValor)


    def operarPaciente(self):
        self.dados.pop(0)

    def removerPosicao(self, valor):
        pos = self.dados.index(valor)
        for i in range(0, pos+1):
            self.dados.pop(0)


    def pacienteOp(self):
        return (self.dados[0]["name"]), (self.dados[0]["phone"])

    def tamanhoFila(self):
        return len(self.dados)

    def sorted(self):
        size_f = len(self.dados)
        for i in range(size_f):
            swap = False
            for j in range(1, size_f):
                if self.dados[j]["du"] > self.dados[j -1]["du"]:
                    self.dados[j], self.dados[j -1] = self.dados[j -1],  self.dados[j]
                    swap = True
            if not swap:
                break