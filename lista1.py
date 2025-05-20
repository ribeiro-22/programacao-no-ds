# Solicita ao usuário um número inteiro positivo n
n = int(input("Digite um número inteiro positivo: "))

# Inicializa a lista vazia
lista = []

# Lê n números inteiros e adiciona à lista
for _ in range(n):
    num = int(input("Digite um número inteiro: "))
    lista.append(num)

# Solicita o número inteiro x para verificação
x = int(input("Digite um número inteiro para verificar se está na lista: "))

# Verifica se x pertence à lista
if x in lista:
    print(f"{x} pertence à lista!")
else:
    print(f"{x} não pertence à lista.")
