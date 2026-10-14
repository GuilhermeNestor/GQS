"""Testes para busca de pessoas no cadastro."""

from src.cadastro_pessoas import CadastroPessoas


def test_buscar_por_nome():
    """Encontra uma pessoa já cadastrada."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ana", 20, "ana@example.com")

    encontrada = cadastro.consultar("Ana")

    assert encontrada is not None
    assert encontrada.nome == "Ana"
    assert encontrada.idade == 20
    assert encontrada.email == "ana@example.com"
