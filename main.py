from fastapi import FastAPI
import random

app = FastAPI()
# Função para sorteio de nomes
def sorteio_nome(nomes):
    return random.choice(nomes)

# Função para sorteio de números
def sorteio_numero():
    return random.randint(1, 10)

# Rota para realizar o sorteio
@app.get("/sorteio/")
async def realizar_sorteio(quantidade_sorteios: int):
    nomes = ["Ana", "Leo", "Kai", "Zoe", "Lia", "Tom", "Eva", "Max", "Ben", "Ray"]
    soma_numeros = 0
    resultados = []

    for _ in range(quantidade_sorteios):
        nome_sorteado = sorteio_nome(nomes)
        numero_sorteado = sorteio_numero()
        resultados.append(f"O nome sorteado é: {nome_sorteado} e o número sorteado é: {numero_sorteado}")
        soma_numeros += numero_sorteado

    resultados.append(f"A soma dos números sorteados é: {soma_numeros}")
    resultados.append("Todos os sorteios foram realizados com sucesso!")

    return {"resultados": resultados}

# Rota inicial para testar
@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de sorteios!"}
