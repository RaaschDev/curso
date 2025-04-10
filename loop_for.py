
# Loop for
# 
# O loop é uma estrutura de repetição
# For -> Uma dessas estruturas
# 
# for i in interavel:
#     execução do loop
# 
# Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis
# Exemplos de iteráveis
# Strings
#   nome = "Mauricio da Cunha"
# Listas
#   lista = [1,2,3,4,5,6]
# Range
#   numeros = range(1, 10)

nome = "Joao da Cunha"
lista = [1,2,3,4,5,6,7,8,9]
numeros = range(1,20)


# iterado de string
# for letra in nome:
#     print(letra)


# iterado de lista
# for item in lista:
#     print(item)


# iterado de range
# for i in numeros:
#     print(i)


# for indice, letra in enumerate(nome):
#     print(f"Indice: {indice}, Letra: {letra}")

# for i,v in enumerate(lista):
#     print(f"Indice: {i}, Letra: {v}")


# quantidade = int(input("Digite a quantidade de vezes q o loop deve rodar: "))

# for n in range(1, quantidade+1):
#     print(f"Imprimindo: {n}")

outro_nome = "Mauricio"
for num in range(1,10):
    print(f"{outro_nome * num}")
    
outro_nome = "Mauricio"
for num in range(1,10):
    print(f"{outro_nome * num}")

outro_nome = "Mauricio"
for num in range(1,10):
    print(f"{outro_nome * num}")