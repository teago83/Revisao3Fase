#19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

menorNumero = 1000
maiorNumero = 0
n = -1
numero = -1
i = 0
soma = 0

def main():
    if n < 1:
        definir_numero_de_valores()
    while i < n :
        registrar_valores()
    print("Menor valor: %.2f" % (menorNumero))
    print("Maior valor: %.2f" % (maiorNumero))
    print("Soma: %.2f" % (soma))

def  definir_numero_de_valores():
    while n < 0:
        n = int(input("Digite a quantidade de números que será digitada:"))
        return
def registrar_valores():
    while i < n:
        numero = float(input("Número %d:" % (i + 1)))
        if numero > 1000 or numero < 0:
            print("Valor inválido.")
            registrar_valores()
        if numero > maiorNumero:
            maiorNumero = numero
        if numero < menorNumero:
            menorNumero = numero
        soma = soma + numero
        i = i + 1
        if(i==n):
            main()
main()