from pilha import Pilha




def main():
    pilhaTeste = Pilha()
    nome  = input("Digite seu nome completo : ")
    for n in nome.split(" "):
        pilhaTeste.push(n)

   # print(pilhaTeste.getPilha())
    print(pilhaTeste.pop())
    #print(pilhaTeste.getPilha())
    #print(pilhaTeste.push("TESTE"))
    print(pilhaTeste.getPilha())
main()
