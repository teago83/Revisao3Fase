#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
#Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
#e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que
#deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa
#deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#o Desconto do IR:
#o Salário Bruto até 900 (inclusive) - isento
#o Salário Bruto até 1500 (inclusive) - desconto de 5%
#o Salário Bruto até 2500 (inclusive) - desconto de 10%
#o Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
#dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de
#hora é 220.
#o Salário Bruto: (5 * 220) : R$ 1100,00
#o (-) IR (5%) : R$ 55,00
#o (-) INSS ( 10%) : R$ 110,00
#o FGTS (11%) : R$ 121,00
#o Total de descontos : R$ 165,00
# Salário Liquido : R$ 935,00

reais_por_hora=float(input("Digite quantos reais você ganha por hora:"))
horas_por_mes=int(input("Digite quantas horas você trabalha por mês:"))
salario_bruto=reais_por_hora*horas_por_mes

inss=salario_bruto*0.1
fgts=salario_bruto*0.11

if salario_bruto > 2500:
    imposto_de_renda=salario_bruto*0.2
    ir=20

if salario_bruto <= 2500:
    imposto_de_renda=salario_bruto*0.1
    ir=10

if salario_bruto <=1500:
    imposto_de_renda=salario_bruto*0.05
    ir=5
if salario_bruto <=900:
    imposto_de_renda=salario_bruto*0
    ir=0

total_descontos=inss+imposto_de_renda

salario_liquido=salario_bruto-total_descontos

print("Salário Bruto: (", horas_por_mes, " * ", reais_por_hora, ") : R$ ", salario_bruto)
print("(-) IR (",ir,"%) : R$ ", imposto_de_renda)
print("(-) INSS (10%) : R% ", inss)
print("FGTS (11%) : R$ ", fgts)
print("Total de descontos : R$ ", total_descontos)
print("Salário líquido : R$ ", salario_liquido)