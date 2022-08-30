#Criar matriz para ser preenchida
matriz = []

#Pedir para o usuário digitar a quantidade de linhas e colunas
N = int(input("Informe a quantidade de linhas da matriz: "))
M = int(input("Informe a quantidade de colunas da matriz: "))

#Criar estrutura de repetição para percorrer a matriz por completo
#for não precisa atualizar
for i in range(N):
    Linha = []
    print(f"Informe os elementos da linha {i}")
    for j in range(M):
        elem = int(input(f"Entre com o elemento da coluna {j}: "))
        Linha.append(elem)
    matriz.append(Linha)


for i in range(N):
    for j in range(M):
        print(matriz[i][j], end = "")
    print("\n")

