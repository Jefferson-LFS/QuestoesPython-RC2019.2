""""Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não."""
frase_reverse = ""
cont = 0
frase = input()
frase_sem_space = ""
for letra in frase:
  if letra != " ":
    frase_sem_space += letra
print(frase_sem_space)
for i in range(1,len(frase_sem_space)+1):
  frase_reverse += frase_sem_space[-i]

if frase_reverse == frase_sem_space:
  print(frase_reverse)
  print("A frase é um palíndromo")
else:
  print(frase_reverse)
  print("A frase não é um palíndromo")

