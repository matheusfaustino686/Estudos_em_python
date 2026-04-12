# Variavéis e tipos de dados "Básicos"

# Uma variável é um espaço na memória onde armazenamos um valor.

# <nome da var> = <valor>

nome = "Matheus"
idade = 27
altura = 1.73
dev = True

# print(f"O nome do aluno é {nome}, ele tem {idade} anos, tem {altura}m de altura e é desenvolvedor? {dev}")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
dev = input("Você é desenvolvedor? (s/n): ").lower() == 's'
print(f"O nome do aluno é {nome}, ele tem {idade} anos, tem {altura}m de altura e é desenvolvedor? {dev}")