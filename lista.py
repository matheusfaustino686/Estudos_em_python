frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # Acessa o primeiro elemento da lista
print(frutas[1])  # Acessa o segundo elemento da lista
print(frutas[2])  # Acessa o terceiro elemento da lista

# Modificando um elemento da lista
frutas[1] = "uva"
print(frutas)  # Imprime a lista modificada

# Adicionando um novo elemento à lista
frutas.append("abacaxi")
print(frutas)  # Imprime a lista com o novo elemento

# Inserindo um elemento em uma posição específica
frutas.insert(1, "morango")
print(frutas)  # Imprime a lista após a inserção

# Removendo um elemento da lista
frutas.remove("maçã")
print(frutas)  # Imprime a lista após a remoção

# Verificando o comprimento da lista
print(len(frutas))  # Imprime o número de elementos na lista

# Verificando se um elemento está na lista
if "laranja" in frutas:
    print("A laranja está na lista de frutas.")  # Imprime se a laranja está na lista
else:    print("A laranja não está na lista de frutas.")  # Imprime se a laranja não está na lista