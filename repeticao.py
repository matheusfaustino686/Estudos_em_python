#Comando de 1 a 5 com o FOR

#for numero in range(1, 6):
    #print(numero)

#Percorendo uma lista de compras

#compras = ["leite", "pão", "ovos", "frutas"]

#for item in compras:
    #print(f"Eu preciso comprar {item}.")

#Percorrendo as letras de uma palavra

#palavra = "Python"

#for letra in palavra:
    #print(letra)

# Usando o while para contagem regressiva

#contador = 5

#while contador > 0:
    #print(contador)
    #contador -= 1 # Decrementa o contador em 1 a cada iteração

#print("Feliz Ano Novo!")

senha_correta = "12345"
senha_usuario = ""
tentativas = 3

while senha_usuario != senha_correta:
    senha_usuario = input("Digite a senha: ")
    if senha_usuario != senha_correta:
        tentativas -= 1
        print(f"Senha incorreta! Você tem {tentativas} tentativas restantes.")
        if tentativas == 0:
            print("Número máximo de tentativas atingido. Acesso negado.")
            break #Encerra o loop se o número máximo de tentativas for atingido
else:    print("Senha correta! Acesso concedido.")


