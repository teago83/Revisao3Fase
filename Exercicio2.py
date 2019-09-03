#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2-
#Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

while True:

    numero=int(input("Digite um número:"))

    if numero > 7 or numero < 1 :
        print("Erro: valor inválido")
        break

    if numero == 1 :
        dia="domingo"
        a="um"
    if numero == 2 :
        dia="segunda-feira"
        a="uma"
    if numero == 3 :
        dia="terça-feira"
        a="uma"
    if numero == 4 :
        dia="quarta-feira"
        a="uma"
    if numero == 5 :
        dia="quinta-feira"
        a="uma"
    if numero == 6 :
        dia="sexta-feira"
        a="uma"
    if numero == 7 :
        dia="sábado"
        a="um"

    print("O dia de hoje é", a, dia)
    break