from stack import Stack


def stack_without_space(phrase, stack1,stack2):
    for p in phrase:
        if p != " ":
            stack1.push(p)
            stack2.push(p)

    return stack1.getStack()

def stackReverse(stack1, stack3):
    while not stack1.isEmpty():
        stack3.push(stack1.pop())
    return stack3.getStack()

def testPalindroma(stack2, stack3):
    var_1 = stack3.getStack()
    var_2 = stack2.getStack()

    return var_1 == var_2

def main():
    stack_1 = Stack()
    stack_2 = Stack()
    stack_3 = Stack()

    phrase = input("Digite uma  frase: ")

    print(f"Frase sem espaço: {stack_without_space(phrase, stack_1, stack_2)}")
    print(f"Frase invertida: {stackReverse(stack_1, stack_3)}")
    print()
    if testPalindroma(stack_2, stack_3):
        print("A frase é um palíndroma")
    else:
        print("A frase não é um palíndroma")

main()


