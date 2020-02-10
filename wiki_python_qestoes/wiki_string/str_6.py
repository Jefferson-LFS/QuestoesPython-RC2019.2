"Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso."

lista_mes = ['01','janeiro', '02', 'fevereiro', '03', 'Março', '04', 'Abril', '05', 'Maio', '06', 'Junho', '07',  'Julho', '08', 'Agosto', '09', 'Setembro', '10', 'outubro', '11', 'Novembro', '12', 'Dezembro']
dia,mes,ano = input("Data de nascimento: ").split("/")
dia = int(dia)
ano= int(ano)
for i in range(len(lista_mes)):
  if mes == lista_mes[i]:
    print(f"Você nasceu em  {dia} de {lista_mes[i+1]} de {ano}.")


    