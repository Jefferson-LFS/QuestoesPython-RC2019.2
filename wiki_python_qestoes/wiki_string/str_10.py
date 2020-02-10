'''Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
'''
numeros_1_9 = [('1', 'um'), ('2', 'dois'), ('3', 'três'), ('4', 'quatro'), ('5','cinco'), ('6','seis'), ('7','sete'), ('8','oito'), ('9','nove')]

numeros_10_90 = [('10','dez'), ('11','onze'), ('12','doze'), ('13','treze'), ('14','quatorze'), ('15','quinze'), ('16','dezesseis'), ('17','dezessete'), ('18','dezoito'), ('19','dezenove'), ('20', 'vinte'), ('30', 'trinta'), ('40', 'quarenta'), ('50', 'cinquenta'), ('60','sessenta'), ('70','setenta'), ('80','oitenta'), ('90','noventa')]

num = input("Digite um número até 99: ")

if len(num) % 2 != 0: # Se digitar somente um digito, busca na primeira lista
  for i in range(9):
    if num == numeros_1_9[i][0]:
      print(numeros_1_9[i][1])

elif ((float(num) / 10)) > 2 and (float(num) % 10 != 0): # Para valores como: 21, 34, 58...99 buscas nas duas listas
  for i in range(10, 18):
    for j in range(9):
      if int(numeros_10_90[i][0]) + j == int(num):
        print(numeros_10_90[i][1] + " e " + numeros_1_9[j-1][1])

else: # Se digitar dois digitos, busca na segunda lista 
  for i in range(len(numeros_10_90)):
    if num == numeros_10_90[i][0]:
      print(numeros_10_90[i][1])

type(numeros_10_90)

