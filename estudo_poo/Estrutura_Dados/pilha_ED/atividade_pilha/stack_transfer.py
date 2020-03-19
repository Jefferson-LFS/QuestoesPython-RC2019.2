from stack import Stack


def Inserttack(value,stack1):

    for v in value:
        stack1.push(v)
    return stack1.getStack()

def satckTransfer_a(stack1, stack2, stack3):
    while not stack1.isEmpty():
        stack2.push(stack1.pop())
    if not stack2.isEmpty():
        for i in range(stack2.size()):
            stack3.push(stack2.pop())
    return stack3.getStack()

def satckTransfer_b(stack1, stack2,):
    var_str = str()
    while not stack1.isEmpty():
        var_str += stack1.pop()
    for i in range(1, len(var_str)+1):
        stack2.push(var_str[-i])
    return stack2.getStack()


def main():
    stack_1 = Stack()
    stack_2 = Stack()
    stack_3 = Stack()



    value  = input("Insira 4 valores: ")
    Inserttack(value, stack_1)
    modo = input("Digite qual o modo de transfêrencia da pilha, a ou b e q para sair: ")
    if modo == 'a':
        print("4.a - Usando uma pilha: ")
        print(satckTransfer_a(stack_1, stack_2,stack_3))

    elif modo == 'b':
        print("4.b - Usando variáves adicionais: ")
        print(satckTransfer_b(stack_1, stack_2))
    elif modo != 'a' or modo != 'b':
        modo = input("valor inválido! Digiite novamente: ")


main()


