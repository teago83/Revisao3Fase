#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
#nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

u = ""
s = ""
user = input("maninho, taca um nome dusuario")
senha = input("ae fei define a senha pro pai")
while(u!=user and s!=senha) :
    while(u!=user) :
        u = input("usario:")
        if (u!=user) :
            print("fei, manda dnv ae")
    while(s!=senha) :
        s = input("seña:")
        if (s!=senha) :
            print("porra cara, digita otra ves")
print("usaro logado cu suceso")