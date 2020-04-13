from hospital import Hospital


paciente = Hospital()


def main():
    menu = ' '
    while menu != 'F':
       menu = input("Digite 'C' - casdastro, 'O' - Operar, 'V'- Ver fila e 'F'- Finalizar :  ").upper()
       print()
       if menu == 'C':
           nome = input("Digite o nome: ")
           telefone= int(input("Digite o telefone: "))
           gu = int(input("Digite o grau de Urgência: "))

           paciente.inserirPaciente(
               {
                   "name": nome,
                   "phone": telefone,
                   "du": gu
               })
           if paciente.tamanhoFila() > 1:
                paciente.sorted()

       elif menu == 'V':
        print(paciente.getFila())

       elif menu == 'O':
           print("Próximo paciente: ", paciente.pacienteOp())
           paciente.operarPaciente()
           print('Paciente operado com sucesso!')

main()


