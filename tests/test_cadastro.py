"""Testes para cadastro de pessoas."""

from src.cadastro_pessoas import CadastroPessoas


def test_cadastrar_pessoa():
    """Cadastra uma pessoa e disponibiliza seus dados na listagem."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ana", 20, "ana@example.com")
    pessoas = cadastro.listar()

    assert len(pessoas) == 1
    assert pessoas[0].nome == "Ana"
    assert pessoas[0].idade == 20
    assert pessoas[0].email == "ana@example.com"
