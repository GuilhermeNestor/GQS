"""Verifica a alteração de pessoas por meio do repositório."""

from src.cadastro_pessoas import CadastroPessoas
from src.repositorio_pessoas_memoria import RepositorioPessoasMemoria


def test_alterar_por_repositorio_compartilhado():
    repositorio = RepositorioPessoasMemoria()
    cadastro = CadastroPessoas(repositorio)
    cadastro.cadastrar("Ana", 20, "ana@example.com")
    assert cadastro.alterar("Ana", "Bia", 21, "bia@example.com")

    pessoa = repositorio.buscar("Bia")
    assert (pessoa.idade, pessoa.email) == (21, "bia@example.com")
    assert repositorio.buscar("Ana") is None
    assert not cadastro.alterar("Ausente", "Outra", 30, "")
