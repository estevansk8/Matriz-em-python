#Fazer o usuário digitar a quadradicidade da matriz
n = int(input("Digite o numero de linhas da matriz: "))
m = int(input("Digite o numero de colunas da matriz: "))
A = []

for i in range(n):
    linha = []
    for j in range(m):
        linha.append(int(input("Entre com o valor inteiro para matriz:")))
    A.append(linha)

#Imprimindo a matriz criada
for i in range(n): #percorre cada linha
    for j in range(m):#percorre cada coluna
        print(A[i][j], end = " ")
    print("\n")

#Calculando o total de linhas nulas
cont_linhas_nulas = 0
i = 0 
while i < n: #percorre cada linha
    j = 0
    linha_nula = True
    if A[i][j] != 0:
        linha_nula = False
        j = j + 1
    if linha_nula == True:
        cont_linhas_nulas += 1
    i += 1

print(f"Total de linhas nulas é igual a {cont_linhas_nulas}")

#Calculando o total de colunas nulas
cont_col_nulas = 0
i = 0 
while i < m: #percorre cada coluna
    j = 0
    coluna_nula = True
    while j < n: #percorre cada linha
        if A[j][i] != 0:
            coluna_nula = False
        j = j + 1
    if coluna_nula == True:
        cont_col_nulas += 1
    i += 1

print(f"Total de colunas nulas é igual a {cont_col_nulas}")





