"""Testes para cadastro de pessoas."""

import copy

import pytest

from src.cadastro_pessoas import CadastroPessoas
from src.pessoa import Pessoa
from src.repositorio_pessoas_memoria import RepositorioPessoasMemoria


def test_cadastrar_pessoa():
    """Cadastra uma pessoa e disponibiliza seus dados na listagem."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ana", 20, "ana@example.com")
    pessoas = cadastro.listar()

    assert len(pessoas) == 1
    assert pessoas[0].nome == "Ana"
    assert pessoas[0].idade == 20
    assert pessoas[0].email == "ana@example.com"


class RepositorioDeCopias(RepositorioPessoasMemoria):
    """Devolve cópias, simulando objetos reconstruídos (como no MySQL)."""

    def buscar(self, nome):
        pessoa = super().buscar(nome)
        if pessoa is None:
            return None
        return copy.copy(pessoa)


@pytest.mark.parametrize("fabrica", [RepositorioPessoasMemoria, RepositorioDeCopias])
def test_alterar_persiste(fabrica):
    """A alteração deve ser gravada no repositório, mesmo que ele devolva cópias."""
    repositorio = fabrica()
    repositorio.cadastrar(Pessoa("Ana Souza", 30, "ana@example.com"))

    cadastro = CadastroPessoas(repositorio)
    cadastro.alterar("Ana Souza", "Ana Souza", 31, "ana.s@example.com")

    pessoa = repositorio.buscar("Ana Souza")
    assert pessoa is not None
    assert pessoa.idade == 31
    assert pessoa.email == "ana.s@example.com"
