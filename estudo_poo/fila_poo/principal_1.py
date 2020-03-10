from fila_1 import Fila

def main():
    filaTeste = Fila()

    filaTeste.inserirDado("IFPB")
    filaTeste.inserirDado("ED")
    filaTeste.inserirDado(2020.1)
    filaTeste.inserirDado("João Pessoa")
    filaTeste.inserirDado("Estágio 1")
    print(filaTeste.getFila())
    filaTeste.removerPosicao(2020.1)
    print(filaTeste.getFila())
    print(filaTeste.tamanhoFila())

main()
