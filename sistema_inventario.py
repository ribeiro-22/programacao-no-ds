# Lista de dicionários representando produtos
produtos = [
    {"nome": "Teclado", "preco": 45.50, "quantidade": 12},
    {"nome": "Mouse", "preco": 20.75, "quantidade": 50},
    {"nome": "Monitor", "preco": 150.00, "quantidade": 8},
    {"nome": "CPU", "preco": 500.00, "quantidade": 5},
    {"nome": "Cabo HDMI", "preco": 15.00, "quantidade": 30}
]

# Ordenar os produtos pelo preço de forma crescente
produtos_ordenados_preco = sorted(produtos, key=lambda x: x['preco'])
print("Produtos ordenados pelo preço (crescente):")
for produto in produtos_ordenados_preco:
    print(f"{produto['nome']}: ${produto['preco']}")

# Ordenar os produtos pelo nome em ordem alfabética
produtos_ordenados_nome = sorted(produtos, key=lambda x: x['nome'])
print("\nProdutos ordenados pelo nome (alfabética):")
for produto in produtos_ordenados_nome:
    print(f"{produto['nome']}: ${produto['preco']}")

# Ordenar os produtos pela quantidade em estoque de forma decrescente
produtos_ordenados_quantidade = sorted(produtos, key=lambda x: x['quantidade'], reverse=True)
print("\nProdutos ordenados pela quantidade (decrescente):")
for produto in produtos_ordenados_quantidade:
    print(f"{produto['nome']}: {produto['quantidade']} unidades")
