from stack import Stack

def main():
    satck_editor = Stack()
    comando = 'i'

    while comando != 'q':
        nome  = input("insira o texto: ")
        for n in nome:
            satck_editor.push(n)
        comando = input("Digite o comando: ")
        if '#' == comando:
            satck_editor.pop()

        if '@' == comando:
           satck_editor.size()
        print(satck_editor.getStack())
        print("Digite 'q' para sair!")


main()
