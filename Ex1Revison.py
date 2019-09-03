#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja
#inválido e continue pedindo até que o usuário informe um valor válido.

nota=-1
while (nota>10 or nota<0) :
    nota=float(input("ae fei, manda a nota"))
    if(nota>10 or nota<0) :
        print("manin, digita denovo ae")
    else :
        print ("rapaz, tu digito certo memo ein, nota %d pra ti" %(nota))
        break