#Criar uma listona que será a matriz
matriz = []
matriz_transposta = []

#Solicitar do usuário 
n = int(input("Digite o valor da matriz quadrada: "))

#Solicitar os elementos da matriz
i = 0
while i < n:

#Criar uma lista para cada linha
    lista = []
    print(f"Informe os elementos da linha {i}")

#Preencher essa linha
    j = 0
    while j < n:
        elem = int(input(f"Digite o elemento da coluna {j} e linha {i}: "))
        lista.append(elem)
        j = j + 1

    matriz.append(lista)
    i = i + 1




#Criar matriz transposta
igual = True
i = 0
while i < n:

#Criar uma lista para cada linha
    lista2 = []
    j = 0
    while j < n:
        lista2.append(matriz[j][i])
        j = j + 1

    matriz_transposta.append(lista2)
    
    if matriz_transposta[i] != matriz[i]:
        igual = False
    i = i + 1

#Verificar se a matriz normal é igual a matriz transposta
if igual == False:
    print("As matrizes não são simetricas")

else:
    print("As matrizes são simetricas")







