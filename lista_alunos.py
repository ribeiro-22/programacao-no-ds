# Lista de alunos com nome e nota
alunos = [
    {"nome": "Carlos", "nota": 85},
    {"nome": "Ana", "nota": 92},
    {"nome": "Bruno", "nota": 78},
    {"nome": "Diana", "nota": 90},
    {"nome": "Eduardo", "nota": 88}
]

# Ordenação por nome usando sort()
alunos.sort(key=lambda aluno: aluno["nome"])

print("Ordenação por nome:")
for aluno in alunos:
    print(aluno)

# Ordenação por nota em ordem decrescente usando sorted()
alunos_ordenados_por_nota = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)

print("\nOrdenação por nota (decrescente):")
for aluno in alunos_ordenados_por_nota:
    print(aluno)
