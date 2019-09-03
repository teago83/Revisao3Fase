n = int(input("Defina o número de termos a ser mostrado:"))

n1 = 1
n2 = 1
count = 0

if n <= 0:
   print("Digite um número positivo.")
elif n == 1:
   print("Sequência de Fibonacci até o dígito número %d:" %(n))
   print(n1)
else:
   print("Sequência de Fibonacci até o dígito número %d:" %(n))
   while count < n:
       print(n1)
       nth = n1 + n2

       n1 = n2
       n2 = nth
       count += 1
       if count == 15 :
           print("\nO programa alcançou um valor acima de 500. Processo encerrado.")
           break