import random

print("Criando projeto")

nomes = ["Ana", "Leo", "Kai", "Zoe", "Lia", "Tom", "Eva", "Max", "Ben", "Ray"]

nome_sorteado = random.choice(nomes)
print(f"O nome sorteado é: {nome_sorteado}")

numero_sorteado = random.randint(1, 10)
print(f"O número sorteado é: {numero_sorteado}")

