# 1ºpasso - Criar uma listona de matriz


matriz1 = []

# Fazer o usuário digitar a primeira matriz
m = int(input("Digite o numero de linhas: "))
n = int(input("Digite o numero de colunas: "))

#Fazer preencher essa matriz
i = 0
while i < m:

#Criar uma lista para cada linha
    lista1 = []
    print(f"Digite os números da linha {i} ")

    j = 0
    while j < n:
        elem = int(input(f"Digite um número para linha {i} e coluna {j}: "))
        lista1.append(elem)
        j += 1

    matriz1.append(lista1)
    i += 1


# 2º passo - Criar uma listona para matriz2
matriz2 = []


#Fazer o usuario digitar o valor da coluna
p = int(input("Digite o numero de colunas da matriz 2: "))

#Fazer preencher essa matriz2
i = 0
while i < n:

#Criar uma lista para cada linha
    lista2 = []
    print(f"Digite os números da linha {i} ")

    j = 0
    while j < p:
        elem2 = int(input(f"Digite um número para linha {i} e coluna {j}: "))
        lista2.append(elem2)
        j += 1

    matriz2.append(lista2)
    i += 1

# 3º passo - Fazer a multiplicação de matriz
#Para multiplicar uma matriz é necessário multiplicar todos elementos de uma linha por todos de uma coluna
matriz_mult = []

#Criar contador para percorrer a matriz1 por linha (As quais são a base da multiplicação de matriz )
k = 0 
while k < m: #Enquanto o k for menor que as linhas da matriz1 vai ocorrer multiplicação

    linha_matriz_mult = [] #Criar uma linha a ser preenchida para cada linha de matriz1


#Criar contador para percorrer a matriz 2 por coluna (As quais são os elementos que formarão a matriz_mult)
    r = 0 
    while r < p: #Enquanto o R for menor que o numero de linhas de matriz_2 vai ocorrer multiplicação


#Criar contadores para preencher a linha criada
        q = 0 #Contador de linhas da matriz2
        l = 0 #Contador de colunas da matriz1
        soma = 0 

#Vai preencher o elemento até o numero de elementos da linha (ou seja: o numero de colunas)
        while l < n:
            mult = matriz1[k][l] * matriz2[q][r]
            soma = soma + mult
            q = q + 1
            l = l + 1

#Após chegar até o ultimo elemento de uma coluna, colocar elemento na linha e começar outra em uma nova coluna
        linha_matriz_mult.append(soma)
        
        r = r + 1 #Atualizar coluna
        
#Começar a multiplicar uma nova linha da matriz1
    matriz_mult.append(linha_matriz_mult) #Adcionar a linha completa na matriz
    k = k + 1 #Trocar de linha da matriz1
    

#Printar matriz
i = 0
while i < k:
    print(matriz_mult[i])
    i = i + 1
