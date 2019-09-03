#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual
#de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
#crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários
#para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de
#crescimento.

pop_a = 80000
pop_b = 200000
anus = 0
ano_a = 0.03
ano_b = 0.015

while(pop_b>pop_a) :
    pop_a = pop_a + (pop_a*ano_a)
    pop_b = pop_b + (pop_b*ano_b)
    anus+=1
    if (pop_a<pop_b) :
        print("ihh feio vamo te q tenta dnv"
              "\noia so como ainda ta"
              "\na = %d"
              "\nb = %d" %(pop_a,pop_b))
    if (pop_a>=pop_b) :
        print("aeeee feio as populacao da a ficaru maior ou igual a da b"
              "\na tem agora %d habitanti"
              "\nenquanto a b tem mesmo é %d habts"
              "\nkkkkkkkkkkkkkkjjjj levaru %d anus pra isso acontece" %(pop_a,pop_b,anus))
        break