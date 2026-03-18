print('ola mundo')

print(7 + 4)
print("7 + 4")
print("7" + "4") # CONCATENANDO STRINGS

# Comentário de 1 linha
'''
    Comentários de
    múltiplas
    linhas
'''

# VARIÁVEIS
nome = "Rodrigo" # str
idade = 26 # int
peso = 70.2 # float

print("Oiii", nome, idade, peso)
print(f"Oiiii {nome}!!!")

# INPUT - SIMULAÇÃO DE UM FORMS NO CMD
nome = input("Digite seu nome: ") # str
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print(nome, idade, peso)
print(idade + 1)

ano_nascimento = 1999
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(idade)