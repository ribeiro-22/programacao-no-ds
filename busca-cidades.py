# Lista pré-definida com pelo menos 8 cidades
cidades = [
    "Curitiba", "Londrina", "Maringá", "Cascavel",
    "Foz do Iguaçu", "Ponta Grossa", "Guarapuava", "Paranaguá"
]

# Solicita ao usuário uma letra ou sequência de caracteres
busca = input("Digite uma letra ou parte do nome da cidade: ").lower()

# Filtra as cidades que contêm a string buscada (ignorando maiúsculas/minúsculas)
encontradas = [cidade for cidade in cidades if busca in cidade.lower()]

# Exibe o resultado
if encontradas:
    print("\nCidades encontradas:")
    for cidade in encontradas:
        print("-", cidade)
else:
    print("\nNenhuma cidade corresponde ao critério de busca.")
