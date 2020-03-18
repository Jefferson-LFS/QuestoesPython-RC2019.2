from stack import Stack
from queue import Queue


def usestack(value,stack1, stack2):
    for v in value:
        stack1.push(v)

    while not stack1.isEmpty():
        stack2.push(stack1.pop())
    return stack2.getStack()


def usequeue(value,stack, queue):
    for v in value:
        stack.push(v)

    while not stack.isEmpty():
        queue.inData(stack.pop())
    return queue.getQueue()


def main():
    stack_1 = Stack()
    stack_2 = Stack()
    queue_1 = Queue()


    value  = input("Insira 4 valores: ")

    print("2.a - Usando pilha:")
    print(usestack(value, stack_1, stack_2))
    print("2.b - Usando fila:")
    print(usequeue(value, stack_1, queue_1))
main()
