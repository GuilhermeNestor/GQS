"""Armazenamento de pessoas em memória."""

from .repositorio_pessoas import RepositorioPessoas


class RepositorioPessoasMemoria(RepositorioPessoas):
    """Mantém os cadastros durante a execução do programa."""

    def __init__(self):
        self._pessoas = []

    def cadastrar(self, pessoa):
        self._pessoas.append(pessoa)
        return pessoa

    def buscar(self, nome):
        return next((pessoa for pessoa in self._pessoas if pessoa.nome == nome), None)

    def listar(self):
        return list(self._pessoas)

    def alterar(self, nome, nova_pessoa):
        for indice, pessoa in enumerate(self._pessoas):
            if pessoa.nome == nome:
                self._pessoas[indice] = nova_pessoa
                return True
        return False
