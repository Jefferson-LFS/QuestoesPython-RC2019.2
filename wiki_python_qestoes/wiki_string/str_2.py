'''Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.'''
nome = input()
novo_nome = ''
nome_final = ''
for i in range(1,len(nome)+1):
  novo_nome += (nome[(len(nome))-i])
for letra in novo_nome:
  if letra >= 'a' and letra  <= 'z':
    nome_final += chr(ord(letra)-32)
  else:
    nome_final += letra
print(nome_final)

#Usando metodos para strings
'''
nome = input()

nome = nome.upper()
resultado = ''

print(nome[::-1])'''