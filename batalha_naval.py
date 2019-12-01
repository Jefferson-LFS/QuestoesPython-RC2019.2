
# versão  sem utilizar a biblioteca random do python. Em construção....

#posi = [[0, 0, 2, 4, 5, 3, 0, 3], [1, 2, 3, 5, 3, 0, 4, 2], [5, 1, 3, 2, 0, 1, 4, 3], [1, 5, 2, 3, 1, 0, 3, 4]]
tabu = []
matriz_usr = []
posi = [0, 1, 2, 3, 4, 5]
letras = ['IFPB'] * 4
tentativas = 10
acertos = 0
for i in range(6):
    linha = ['X'] * 6
    tabu.append(linha)

for i in range(6):
    linha = ['X'] * 6
    matriz_usr.append(linha)

for i in range(4):
    posi.reverse()
    tabu[posi[i]][posi[i]] = letras[i]
    posi.reverse()



# Se quiser verifar as posicões do nome
for i in range(6):
  for j in range(6):
    print(tabu[i][j], end=' ')
  print()


while (tentativas > 0 and acertos != 4):
    row, column = (input("Digeite o valor da posição:")).split(' ')
    row = int(row)
    column = int(column)
    print()
    if tabu[row][column] == 'IFPB':
        matriz_usr[row][column] = 'IFPB'
        acertos += 1
        print(f"Posição correta! você tem mais {tentativas} tentativas")
        print()
        for i in range(6):
            for j in range(6):
                print(matriz_usr[i][j], end=' ')
            print()

    else:
        print(f"Posição incorreta! você tem mais {tentativas} tentativas")
        print()
        for i in range(6):
            for j in range(6):
                print(matriz_usr[i][j], end=' ')
            print()

    tentativas -= 1
print(f"Você acertou {acertos} posicões")



'''
#Utlizando a biblioteca random
import random

tabu = []
matriz_usr = []
posi = [0, 1, 2, 3, 4, 5]
letras = ['IFPB'] * 4
tentativas = 10
acertos = 0
for i in range(6):
    linha = ['X'] * 6
    tabu.append(linha)

for i in range(6):
    linha = ['X'] * 6
    matriz_usr.append(linha)

for i in range(4):
    tabu[random.choice(posi)][random.choice(posi)] = letras[i]
    
# Se quiser verifar as posicões do nome
for i in range(6):
  for j in range(6):
    print(tabu[i][j], end=' ')
  print()

while (tentativas > 0 and acertos != 4):
    row, column = (input("Digeite o valor da posição:")).split(' ')
    row = int(row)
    column = int(column)
    print()
    if tabu[row][column] == 'IFPB':
        matriz_usr[row][column] = 'IFPB'
        acertos += 1
        print(f"Posição correta! você tem mais {tentativas} tentativas")
        print()
        for i in range(6):
            for j in range(6):
                print(matriz_usr[i][j], end=' ')
            print()

    else:
        print(f"Posição incorreta! você tem mais {tentativas} tentativas")
        print()
        for i in range(6):
            for j in range(6):
                print(matriz_usr[i][j], end=' ')
            print()

    tentativas -= 1
print(f"Você acertou {acertos} posicões")'''
