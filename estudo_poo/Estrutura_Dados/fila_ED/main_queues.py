from queue import Queue

import random











def main():

    tempo_simulacao = int(input("Digite o tempo da simulação em minutos: "))

    fila_caixa_1 = Queue()
    fila_caixa_2 = Queue()
    fila_caixa_3 = Queue()
    fila_caixa_4 = Queue()
    fila_caixa_5 = Queue()
    caixa = [fila_caixa_1, fila_caixa_2, fila_caixa_3, fila_caixa_4, fila_caixa_5]
    tempo_espera = [0] * 5
    qtde_clientes = [0] * 5
    count = 0
    tempo_entrada = 0
    temp_esp = tempo_simulacao - tempo_entrada
    cliente = [tempo_entrada, temp_esp]
    while count != tempo_simulacao:
        menor_fila = 1
        random.randrange(4, 17)
        for i in range(7):
            if ((caixa[i]).isEmpty()) and (i != 5):
                (caixa[i]).inData(cliente)
            else:
                for fila in caixa:
                    if fila.sizeQueue() == menor_fila:
                        menor_fila = fila.sizeQueue()
                    elif fila.sizeQueue() < menor_fila:
                    else:
                        caixa[i].inData(cliente)



        count += 1

    for i in range(5):
        print((caixa[i]).getQueue())


    ''''(caixa[0]).inData(cliente)
    (caixa[1]).inData(cliente)
    (caixa[2]).inData(cliente)
    (caixa[3]).inData(cliente)
    (caixa[4]).inData(cliente)

    for i in range(5):
        if i == 1:
            (caixa[i]).inData(cliente)
        print((caixa[i]).getQueue())


    QueueTest.inData("IFPB")
    QueueTest.inData("ED")
    QueueTest.inData(2020.1)
    QueueTest.inData("João Pessoa")
    QueueTest.inData("Estágio 1")
    print(QueueTest.getQueue())
    QueueTest.dePosicion(2020.1)
    print(QueueTest.getQueue())'''





main()
