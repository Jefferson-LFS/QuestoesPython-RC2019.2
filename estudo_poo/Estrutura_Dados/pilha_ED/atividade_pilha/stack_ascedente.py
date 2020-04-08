from stack import Stack

def sorted(list):
    size_l = len(list)
    for i in range(size_l):
        swap = False
        for j in range(1, size_l):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                swap = True
        if not swap:
            break

def main():
    stack = Stack()
    orderList = []

    while stack.size() < 4:
        value = int(input(" Digite um número: "))
        stack.push(value)

    while not stack.isEmpty():
        orderList.append(stack.pop())

    sorted(orderList)

    for i in range(len(orderList)):
        stack.push(orderList[i])

    print('Pilha ordenada:', stack.getStack())

main()


