#18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor
#e a soma dos valores.

menorNumero = 999999999
maiorNumero = 0
n = -1
numero = -1
i = 0
soma = 0
while(n<0):
    n = int(input("Digite a quantidade de números que será digitada:"))
while i < n :
    numero = float(input("Número %d:" % (i+1)))
    if numero >1000 or numero <0 :
        print("Valor inválido.")
    if numero > maiorNumero:
        maiorNumero = numero
    if numero < menorNumero:
        menorNumero = numero
    soma = soma + numero
    i = i + 1
print("Menor valor: %.2f"%(menorNumero))
print("Maior valor: %.2f"%(maiorNumero))
print("Soma: %.2f"%(soma))
