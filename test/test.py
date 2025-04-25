from src.main import *
from unittest.mock import patch
import pytest
import pytest_asyncio

def test_sorteio_nome_mock():
    nomes = ["Ana", "Leo", "Kai"]
    with patch('random.choice', return_value="Ana"):
        resultado = sorteio_nome(nomes)  # sem await aqui!
        assert resultado == "Ana"

def test_sorteio_numero_mock():
    with patch('random.randint', return_value=7):
        numero = sorteio_numero()  # sem await aqui também!
        assert numero == 7

def test_adicionar_numeros():
    resultado = adicionar_numeros(2, 3)
    assert resultado == 5, f"Esperado 5, mas obteve {resultado}"


@pytest.mark.asyncio
async def test_realizar_sorteio():
    with patch('src.main.sorteio_nome', return_value="Ana"), patch('src.main.sorteio_numero', return_value=5):
        resultado = await realizar_sorteio(quantidade_sorteios=3)

        assert len(resultado["resultados"]) == 5
        assert "O nome sorteado é: Ana e o número sorteado é: 5" in resultado["resultados"]
        assert "A soma dos números sorteados é: 15" in resultado["resultados"]
        assert "Todos os sorteios foram realizados com sucesso!" in resultado["resultados"]

@pytest.mark.asyncio
async def test_root():
    resultado = await root()
    assert resultado == {"message": "Bem-vindo à API de sorteios!"}

