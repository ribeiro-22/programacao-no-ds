# Solicita ao usuário uma lista de nomes, separados por vírgula
nomes = input("Digite uma lista de nomes separados por vírgula: ").split(",")

# Itera sobre a lista usando a função enumerate()
for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome.strip()}")
