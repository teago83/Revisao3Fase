#20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
#limitando o fatorial a números inteiros positivos e menores que 16.

op = 1
while op == 1:
    fator = -1
    while (fator < 0 or fator > 16):
        fator = int(input("Forneça o valor desejado para fazer a magia:"))
    count = fator
    n = fator
    print(fator, end="! = ")
    while count > 1:
        n = n * (count - 1)
        print(count, end=" * ")
        count = count - 1
    print("1 = ", n)
    while op != 1 and op != 2:
        print("\nDeseja repetir o processo?")
        print("1 - Sim")
        print("2 - Não")
        op = int(input)
