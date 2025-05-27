# Definição da tupla para armazenar os livros
livros = (
    ("1984", "George Orwell", 1949),
    ("Dom Casmurro", "Machado de Assis", 1899),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
)

# Lista que será atualizada automaticamente com os livros da tupla
lista_livros = list(livros)

# Função para exibir os conteúdos da tupla e da lista
def consultar_livros():
    print("\nColeção de Livros (Tupla):")
    for livro in livros:
        print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")

    print("\nLista de Livros:")
    for livro in lista_livros:
        print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")

# Exibir os dados
consultar_livros()
