"""Contrato de armazenamento do cadastro de pessoas."""

from abc import ABC, abstractmethod

from .pessoa import Pessoa


class RepositorioPessoas(ABC):
    """Define as operações de armazenamento usadas pelo serviço."""

    @abstractmethod
    def cadastrar(self, pessoa: Pessoa) -> Pessoa:
        """Armazena a pessoa e retorna o registro criado."""

    @abstractmethod
    def buscar(self, nome: str) -> Pessoa | None:
        """Busca a primeira pessoa com o nome informado."""

    @abstractmethod
    def listar(self) -> list[Pessoa]:
        """Lista as pessoas em ordem de cadastro."""

    @abstractmethod
    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Atualiza o primeiro registro encontrado e informa se ele existe."""
