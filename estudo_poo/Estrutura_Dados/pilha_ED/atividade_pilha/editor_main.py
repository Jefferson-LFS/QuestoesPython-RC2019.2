from pilha import Pilha

def main():
    pilhaTeste = Pilha()
    comando = 'i'

    while comando != 'q':
        nome  = input("insira o texto: ")
        for n in nome:
            pilhaTeste.push(n)
        comando = input("Digite o comando: ")
        if '#' == comando:
            pilhaTeste.pop()

        if '@' == comando:
           pilhaTeste.esvaziar()
        print(pilhaTeste.getPilha())
        print("Digite 'q' para sair!")


main()
