
# Lista com pelo menos 10 títulos de livros
livros = [
    "O Pequeno Príncipe",
￼

    "Dom Casmurro",
    "A Revolução dos Bichos",
    "1984",
    "Cem Anos de Solidão",
    "Capitães da Areia",
    "Harry Potter e a Pedra Filosofal",
    "O Senhor dos Anéis",
    "A Menina que Roubava Livros",
    "O Código Da Vinci"
]

# Solicita uma palavra-chave ao usuário
palavra_chave = input("Digite uma palavra ou trecho do título do livro: ").lower()

# Filtra os livros que contê- Crie um programa simples em Python que filtre dados emm a palavra-chave (ignorando maiúsculas/minúsculas)
resultados = [livro for livro in livros if palavra_chave in livro.lower()]

# Exibe os resultados
if resultados:
    print("\nTítulos encontrados:")
    for titulo in resultados:
        print("-", titulo)
else:
    print("\nNenhum título corresponde ao critério de busca.")

