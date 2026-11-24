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
        pessoa = self.buscar(nome)
        if pessoa is None:
            return False
        pessoa.nome = nova_pessoa.nome
        pessoa.idade = nova_pessoa.idade
        pessoa.email = nova_pessoa.email
        return True
