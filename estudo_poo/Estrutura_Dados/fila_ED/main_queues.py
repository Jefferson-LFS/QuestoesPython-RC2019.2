from queue import Queue

def main():
    QueueTest = Queue()

    QueueTest.inData("IFPB")
    QueueTest.inData("ED")
    QueueTest.inData(2020.1)
    QueueTest.inData("João Pessoa")
    QueueTest.inData("Estágio 1")
    print(QueueTest.getQueue())
    QueueTest.dePosicion("IFPB")
    print(QueueTest.getQueue())


main()
