#Faça um programa que leia e valide as seguintes informações:
#a. Nome: maior que 3 caracteres;
#b. Idade: entre 0 e 150;
#c. Salário: maior que zero;
#d. Sexo: 'f' ou 'm';
#e. Estado Civil: 's', 'c', 'v', 'd';
nome = "a"
idade = 151
salario = -1
sesgo = 'g'
estadocu = 'cu'
count = 2
while(len(nome)<3) :
    nome = input("digitu nomi ae feio")
    if(len(nome)<3) :
        print("ihhhh feiooo digito poco hein")
while(idade>150 or idade<0) :
    idade = int(input("qnts anu tu tem feiooo"))
    if(idade>150 or idade<0) :
        print("haaa para ne")
while(salario<0) :
    salario = float(input("manda ae teu salario fei"))
    if(salario<0) :
        print("ihh feio ta pobre hein kkkj bota o salario pra valer")
while(sesgo!='f' and sesgo!='m') :
    sesgo = input("quale teus reprodutero (f ou m fei)")
    if(sesgo=='f') :
        genru = "muié"
    if(sesgo=='m') :
        genru = "homi"
    if(sesgo!='f' and sesgo!='m') :
        print("foi mau fei, pra mim n exist")
while(estadocu!='s' and estadocu!='c' and estadocu!='v' and estadocu!='d') :
    estadocu = input("ae po teu estado civir (s, c, v ou d)")
    if(estadocu == 's') :
        ec = "sortero"
    if (estadocu == 'c'):
        ec = "casadu"
    if (estadocu == 'v'):
        ec = "viuvis"
    if (estadocu == 'd'):
        ec = "despacito"
    if(estadocu!='s' and estadocu!='c' and estadocu!='v' and estadocu!='d') :
        print("feio, nun reconheco esse nao ein")
print("nomi: %s \nidaji: %d \ndinheru pra compra salada: %.2f \nsesgo: %s \nestadu civir: %s" %(nome,idade,salario,genru,ec))