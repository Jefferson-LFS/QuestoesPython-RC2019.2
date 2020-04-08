from estacionamento import Estacinamento

carros = Estacinamento()

def testecmd (comando):
    thisdict = {
        "R":"Remover",
        "I":"Inserir",
        "S":"Mostrar estacinamento",
        "Q":"sair"
    }
    teste = True
    while teste:
        if comando in thisdict:
            teste = False
            return comando
        else:
            comando = input("Valor inválido, digite novamente: ")


def metodos(cmd, carros):
    while cmd != 'Q':
        cmd = input("Informe qual o método: ")
        cmd = testecmd(cmd)
        if cmd == "I":
            carros.inserirDado(input("Informe o número da placa (INSERÇÃO): "))
        elif cmd == 'S':
            print(carros.getFila())

        elif cmd == 'R':
            if carros.tamanhoFila() != 0:
                carros.removerPosicao(input("Informe o número da placa (REMOÇÃO): "))
            else:
                print("Operação inválida! Não existe carros para remover")
                print("Digite  o método 'I' se deseja inserir um novo carro, se não digite 'Q' para sair")


def main():

    print("(Métodos) Digite 'I'-Inserir ,'R'- Remover, 'S'- Mostrar estacinamento, 'Q'- para sair:")
    cmd = ' '
    placa = (input("Informe o número da primeira placa:  "))
    carros.inserirDado(placa)
    metodos(cmd, carros)


main()