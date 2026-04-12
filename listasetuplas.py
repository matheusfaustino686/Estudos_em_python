#frutas = ["maça", "banana", "laranja", "uva"]
#frutas.remove("banana")
#print(frutas)

#frutas.pop(0)
#print(frutas)

#frutas.pop()
#print(frutas)

#Tuplas 
#Tuplas são como listas, mas imutáveis. Elas são criadas com parênteses ().

#cores = ("vermelho", "azul", "verde")
#numeros = (1, 2, 3, 4, 5)

#Acessando elementos 
#print(cores[0]) #"vermelho"
#print(cores[-1]) #"verde"

#Tentando modificar uma tupla (Erro!)
#cores[1] = "amarelo" # X Isso gera erro, pois tuplas são imutáveis!

# Convertendo entre listas e tuplas
# Podemos converter uma tupla para uma lista e modificar os elementos.

tupla = (1, 2, 3)
lista = list(tupla) #Converte para lista
lista.append(4)
tupla = tuple(lista) #Converte de. volta para lista
print(tupla) # (1, 2, 3, 4)

# Quando usar tuplas
# Quando queremos garantir que os vlores não sejam alterados.