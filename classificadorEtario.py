dia_hoje = 29
mes_hoje = 10
ano_hoje = 2025

dia_nasc = int(input("Digite o dia de nascimento: "))
mes_nasc = int(input("Digite o mês de nascimento: "))
ano_nasc = int(input("Digite o ano de nascimento: "))

idade = ano_hoje - ano_nasc

if (mes_hoje < mes_nasc) or (mes_hoje == mes_nasc and dia_hoje < dia_nasc):
    idade -= 1

if idade <= 3:
    classificacao = "bebê"
elif idade <= 12:
    classificacao = "criança"
elif idade <= 17:
    classificacao = "adolescente"
elif idade <= 59:
    classificacao = "adulto"
else:
    classificacao = "idoso"

print(f"Idade: {idade} anos")
print(f"Classificação: {classificacao}")
