"Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo."
palavra_1, palavra_2 = input().split()
print(f"Tamanho de {palavra_1}: {len(palavra_1)} caracteres")
print(f"Tamanho de {palavra_2}: {len(palavra_2)} caracteres")
if (len(palavra_1) != len(palavra_2)):
  print("As duas strings são de tamanhos diferentes.")
else:
  print("As duas strings têm o mesmo tamanho")
if (palavra_1 != palavra_2):
  print("As duas strings possuem conteúdo diferente.")
else:
  print("As duas strings têm o mesmo conteúdo")