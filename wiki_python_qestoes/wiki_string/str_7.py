"""Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), 
conte. Quantos espaços em branco existem na frase.
Quantas vezes aparecem as vogais a, e, i, o, u."""
frase = input()
qtde_esp = 0
#vogais = ["a","e", "i", "o", "u"]
qtde_vogais = [0] * 5
for i in range(len(frase)):
  if (frase[i]) == " ":
    qtde_esp +=1
  elif frase[i] == "a":
     qtde_vogais[0] +=1
  elif frase[i] == "e":
     qtde_vogais[1] +=1
  elif frase[i] == "i":
     qtde_vogais[2] +=1
  elif frase[i] == "o":
     qtde_vogais[3] +=1
  elif frase[i] == "u":
     qtde_vogais[4] +=1

print(qtde_esp)
print(f"a:{qtde_vogais[0]}, e:{qtde_vogais[1]}, i:{qtde_vogais[2]}, o:{qtde_vogais[3]}, u:{qtde_vogais[4]}")

#outra forma usando a função cont
'''
cont=0

dig = input("informe uma frase: ")
print("Ha '%i' espaços na frase.  "%(dig.count(" ")))

s = dig.count("a")+dig.count("e")+dig.count("i")+dig.count("o")+dig.count("u")
print("Ha '%i' vogais na frase.  "%(s))'''