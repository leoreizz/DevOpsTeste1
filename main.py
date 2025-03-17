import random

def sorteio_nome(nomes):
    return random.choice(nomes)

def sorteio_numero():
    return random.randint(1, 10)

print("Criando projeto")

nomes = ["Ana", "Leo", "Kai", "Zoe", "Lia", "Tom", "Eva", "Max", "Ben", "Ray"]

nome_sorteado = sorteio_nome(nomes)

numero_sorteado = sorteio_numero()

quantidade_sorteios = int(input("Quantos sorteios você quer realizar? "))

print(f"Realizando {quantidade_sorteios} sorteios...")

soma_numeros = 0

for _ in range(quantidade_sorteios):
    nome_sorteado = sorteio_nome(nomes)
    numero_sorteado = sorteio_numero()
    print(f"O nome sorteado é: {nome_sorteado} e o número sorteado é: {numero_sorteado}")
    soma_numeros += numero_sorteado

print(f"A soma dos números sorteados é: {soma_numeros}")

print("Todos os sorteios foram realizados com sucesso!")
