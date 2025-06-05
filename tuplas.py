# Solicita ao usuário as coordenadas geográficas (latitude e longitude)
coordenadas = input("Digite a latitude e longitude separadas por vírgula: ").split(",")

# Converte os valores para números float e desempacota a tupla
latitude, longitude = map(float, coordenadas)

# Exibe as coordenadas
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
