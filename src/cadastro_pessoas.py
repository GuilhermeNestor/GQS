"""Serviço de cadastro de pessoas."""

from .pessoa import Pessoa
from .repositorio_pessoas import RepositorioPessoas
from .repositorio_pessoas_memoria import RepositorioPessoasMemoria


class CadastroPessoas:
    """Encapsula o estado e as operações do cadastro de pessoas."""

    def __init__(self, repositorio: RepositorioPessoas | None = None):
        self._repositorio = repositorio if repositorio is not None else RepositorioPessoasMemoria()

    def cadastrar(self, nome, idade, email):
        """Cadastra uma pessoa e retorna o registro criado."""
        pessoa = Pessoa(nome, idade, email)
        return self._repositorio.cadastrar(pessoa)

    def consultar(self, nome):
        """Retorna a pessoa com o nome informado ou None."""
        return self._repositorio.buscar(nome)

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        """Altera a pessoa encontrada e retorna True quando ela existe."""
        return self._repositorio.alterar(nome, Pessoa(novo_nome, nova_idade, novo_email))

    def listar(self):
        """Retorna uma cópia da lista de pessoas."""
        return self._repositorio.listar()

    def analisar(self, nome):
        """Retorna os dados de análise da pessoa procurada."""
        pessoa = self.consultar(nome)
        if pessoa is None:
            return None

        if pessoa.idade < 12:
            faixa_etaria = "Crianca"
        elif pessoa.idade < 18:
            faixa_etaria = "Adolescente"
        elif pessoa.idade < 30:
            faixa_etaria = "Adulto jovem"
        elif pessoa.idade < 60:
            faixa_etaria = "Adulto"
        else:
            faixa_etaria = "Idoso"

        if pessoa.email.endswith("@gmail.com"):
            provedor = "Gmail"
        elif pessoa.email.endswith("@outlook.com"):
            provedor = "Outlook"
        elif pessoa.email.endswith("@hotmail.com"):
            provedor = "Hotmail"
        elif pessoa.email.endswith("@utfpr.edu.br"):
            provedor = "UTFPR"
        else:
            provedor = "Outro"

        return {
            "faixa_etaria": faixa_etaria,
            "provedor": provedor,
            "apto_para_contato": pessoa.idade >= 18 and bool(pessoa.email),
        }
