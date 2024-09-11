# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)

idade = int(input("Digite sua idade "))

if (idade<=12):
    print("Você é uma criança")
elif (idade>12) and (idade<18):
    print("Você é um adolescente")

if (idade>17) and (idade<60):
    print("Você é um adulto")
elif (idade>59):
    print("Você é um idoso")