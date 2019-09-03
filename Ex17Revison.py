#17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.:
#5!=5.4.3.2.1=120

fator = -1
while(fator<0) :
    fator = int(input("Forneça o valor desejado para fazer a magia:"))
count = fator
n = fator
print(fator, end="! = ")
while count > 1:
    n = n * (count - 1)
    print(count, end=" * ")
    count = count - 1
print("1 = ", n)
