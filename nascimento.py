import datetime

def ano_de_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento entre 1922 e 2024: "))
            if 1922 <= ano <= 2024:
                return ano
            else:
                print("Por favor, insira um ano válido entre 1922 e 2024.")
        except ValueError:
            print("Por favor, insira um número válido.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    return ano_atual - ano_nascimento

nome_completo = input("Digite seu nome completo: ")
ano_nascimento = ano_de_nascimento()
idade = calcular_idade(ano_nascimento)

print(f"Nome: {nome_completo} \nIdade: {idade} anos")

