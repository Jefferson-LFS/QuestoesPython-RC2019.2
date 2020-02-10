'''Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.'''
qtde_num = 0
cpf = input()
if cpf[3] == "." and cpf[3] == "." and cpf[7] == "." and cpf[11] == "-":
  for letra in cpf:
    if letra != "." or letra != "-":
      if letra >= "0" and letra  <= "9":
        qtde_car +=1 
      

if qtde_num == 11:
  print("CPF VALIDO")
else: 
  print("CPF INVALIDO")