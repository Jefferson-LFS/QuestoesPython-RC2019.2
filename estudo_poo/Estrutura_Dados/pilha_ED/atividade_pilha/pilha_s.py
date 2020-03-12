from pilha import Pilha

def main():
    pilha_1 = Pilha()
    pilha_2 = Pilha()



    nome  = input("insira o texto: ")
    for n in nome:
        pilha_1.push(n)
    print(pilha_1.getPilha())

    pilha_2 = pilha_1[::-1]
    print(pilha_2.getPilha())


main()
