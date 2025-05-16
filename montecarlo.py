import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
anos = 10
simulacoes = 10  # Ajuste conforme necessário para melhor visualização
retorno_medio = 0.07
desvio_padrao = 0.20
valor_inicial = 10000  # Valor inicial da carteira

# Simulação de Monte Carlo
np.random.seed(42)  # Para reprodução dos resultados
anos_array = np.arange(anos + 1)
resultados = np.zeros((simulacoes, anos + 1))
resultados[:, 0] = valor_inicial

# Gerando trajetórias simuladas
for i in range(simulacoes):
    for j in range(1, anos + 1):
        retorno_aleatorio = np.random.normal(retorno_medio, desvio_padrao)
        resultados[i, j] = resultados[i, j - 1] * (1 + retorno_aleatorio)

# Plotando o gráfico
plt.figure(figsize=(10, 6))
for i in range(simulacoes):
    plt.plot(anos_array, resultados[i], alpha=0.7)

plt.xlabel("Anos")
plt.ylabel("Valor da Carteira")
plt.title("Simulação de Monte Carlo para Investimentos em Ações")
plt.grid()
plt.show()
