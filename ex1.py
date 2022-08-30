#Criar matriz para ser preenchida
matriz = []

#Pedir para o usuário digitar a quantidade de linhas e colunas
N = int(input("Informe a quantidade de linhas da matriz: "))
M = int(input("Informe a quantidade de colunas da matriz: "))

print("************************************")

#Criar estrutura de repetição para o usuário digitar os números
i = 0
while i < N:

#Criar uma lista para cada linha 
    linha = []
    print(f"Informe os elementos da linha {i}")
    i = i + 1

#Digitar os números da linha(cada linha terá uma quantidade de números igual a de colunas )
    j = 0
    while j < M:
        elem = int(input(f"Informe o número da coluna {j}: "))
        linha.append(elem)
        j = j + 1
        
    matriz.append(linha)
    print("************************************")


#Verificar qual é o maior elemento
maior = matriz[0][0]
i = 0
while i < N:
    j = 0
    while j < M:
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        j = j + 1
    i = i + 1

print(f"O maior elemento é o {maior}")


#Verificar qual é o menor elemento
menor = matriz[0][0]
i = 0
while i < N:
    j = 0
    while j < M:
        if matriz[i][j] < menor:
            menor = matriz[i][j]
        j = j + 1
    i = i + 1

print(f"O menor elemento é o {menor}")


#Mostrar a matriz
i = 0
while i < len(matriz):
    j = 0
    while j < len(matriz[i]):
        print(matriz[i][j])
        print(" ")
        j = j + 1


    i = i + 1





