from queue import Queue

import random



def main():

    temp = int(input("tempo em minutos: "))

    fila_caixa_1 = Queue()
    fila_caixa_2 = Queue()
    fila_caixa_3 = Queue()
    fila_caixa_4 = Queue()
    fila_caixa_5 = Queue()
    caixa = [fila_caixa_1, fila_caixa_2, fila_caixa_3, fila_caixa_4, fila_caixa_5]
    menor_fila = 1
    count = 0
    teste = False
    teste_like = 0
    while count != temp:
        for i in range(4):
            if i < 6 and (caixa[i]).isEmpty():
                (caixa[i]).inData([])
            else:
                for j in range(5):
                    if (caixa[j]).sizeQueue() <= menor_fila:
                        teste = True
                        menor_fila = (caixa[j]).sizeQueue()
                        (caixa[j]).inData([])


                if teste:
                    for k in range(5):
                        if ((caixa[0]).sizeQueue()) == ((caixa[k]).sizeQueue()):
                            teste_like += 1
                    if teste_like == 5:
                        (caixa[0]).inData([])
                        menor_fila =  (caixa[0]).sizeQueue()

                teste_like = 0
        count += 1

    print(menor_fila)
    print(teste_like)
    for i in range(5):

        print(caixa[i].getQueue(), end=' | ')

main()