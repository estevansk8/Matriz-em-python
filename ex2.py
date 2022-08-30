
#Criar lista de matriz para ser preenchida
matriz = []
matriz_inversa = []

#solicitar o valor de linhas e colunas(matriz quadrada)
N = int(input("Digite a quantidade de linhas e colunas da matriz quadrada: "))

#Criar uma estrutura que vai desde o primeiro elemento da lista(uma linha)até o último e vai preenchendo-os
i = 0
while i < N:

#Criar uma lista para cada linha
    lista = []
    print(f"Informe os elementos da linha {i}")

#Preencher cada 'coluna' desssa lista
    j = 0
    while j < N:
        elem = int(input(f"Digite o número da coluna {j} da linha {i}: "))
        lista.append(elem)
        j = j + 1

    matriz.append(lista)
    i = i + 1

#Mostrar a matriz
i = 0
while i < len(matriz):
    print(matriz[i])

    i = i + 1
print("***********************")

#Fazer a matriz inversa
i = 0
while i < N:
    
#Criar uma lista para cada linha
    lista2 = []
    j = 0
    while j < N:
        lista2.append(matriz[j][i])
        j = j + 1

    matriz_inversa.append(lista2)
    i = i + 1


#Mostrar a matriz inversa
i = 0
while i < len(matriz_inversa):
    print(matriz_inversa[i])

    i = i + 1
print("***********************")


