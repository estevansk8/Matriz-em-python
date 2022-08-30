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
N = n
p = int(input("Digite o numero de colunas da matriz 2: "))

#Fazer preencher essa matriz2
i = 0
while i < N:

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
matriz_mult = []

#Criar linhas até M(ja que esse é o numero de linhas da matriz)
i = 0
while i < m: #Enquanto i for menor que m, vai criando linha para matriz_mult
    linha_mult = []

    
    #Preencher essa lista até o número de colunas ser igual a p
    j = 0
    while j < p: #Enquanto i for menor que p, vai criando coluna para a linha
        
        #Preencher uma coluna até o indice de linha da matriz2 for menor que seu valor(que é igual o de n)
        while N < n:

            #Percorrer a matriz1 e matriz2

        
            mult = matriz1[m][n] * matriz2[N][p]
            soma = soma + mult
        
            n = n + 1
            N = N + 1

        elem3 = soma
        linha_mult.append(elem3)
        p = p + 1
        j = j + 1

    matriz_mult.append(linha_mult)
    i = i + 1

#Printar matriz
print(matriz_mult)

    

            





