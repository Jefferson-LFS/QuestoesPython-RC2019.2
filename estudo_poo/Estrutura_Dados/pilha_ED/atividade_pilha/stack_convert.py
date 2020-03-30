from stack import Stack


def satckBin(value, stack1, stack2):
    while value != 0:
        modulu = value % 2
        stack1.push(modulu)
        value //= 2

    while not stack1.isEmpty():
        stack2.push(stack1.pop())
    return stack2.getStack()

def satckHex(value, stack1, stack2, dict):
    while value != 0:
        modulu = value % 16
        if modulu in dict:
            stack1.push(dict[modulu])
        else:
         stack1.push(modulu)
        value //= 16

    while not stack1.isEmpty():
        stack2.push(stack1.pop())
    return stack2.getStack()


def main():
    stack1 = Stack()
    stack2 = Stack()
    dict = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'}
    num_dec = int(input("Insira um valor em decimal de (2-9) ou (11-27): "))

    while (num_dec == 10) or (num_dec < 2 or num_dec > 27):
        print("Voce digitou errado!")
        num_dec = int(input("Insira um valor em decimal de (2-9) ou (11-27): "));
    print()
    if num_dec >= 2  and num_dec <= 9:
        print(f"Valor em binário: {satckBin(num_dec, stack1, stack2)}")
    elif num_dec >= 11  and num_dec <= 27:
        print(f"Valor em hexadecimal: {satckHex(num_dec, stack1, stack2, dict)}")

main()


