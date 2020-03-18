from agenciab import Caixa
from random import random

filas = Caixa()

def simulacao(temposimulação):
    while True:
        tempos_espera = []
        for i in range(5):
         filas.inserirCliente([])
         for inst_minuto in range(temposimulação):
          if random() < 0.2: # probabilidadde de chegar quantro cleintes
           for i in range(4):  # Cria quatro clientes para entrar na menor fila
                cliente = [0]
                menor_fila = filas[0].getFila()
                for fila in filas:
                    if len(fila) < len(menor_fila):
                        menor_fila = fila
                menor_fila.append(cliente)
          elif random() <  0.8: # probabilidadde de chegar dezesseis cleintes
            for i in range(16):  # Cria dezesseis clientes para entrar na menor fila
                cliente = [0]
                menor_fila = filas[0].getFila()
                for fila in filas:
                    if len(fila) < len(menor_fila):
                        menor_fila = fila
                menor_fila.append(cliente)

          for i in range(filas.tamanhoFila()):
            fila = filas[i].getFila()
            if not fila[0][0]:
                tempos_espera.append(fila[0][1])
                fila.pop(0)
            if fila:
                fila[0][0] -= 1
                for i in range(1, len(fila)):
                    fila[i][1] += 1

    if len(tempos_espera):
        espera_media = round(sum(tempos_espera)/len(tempos_espera))
    else:
        espera_media = 0
    print(f"Espera média: {espera_media}")

def main():
    tempo_simulacao = int(input("Digite o tempo da simulação em minutos: "))
    simulacao(tempo_simulacao)

main()