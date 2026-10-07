"""Serviço de cadastro de pessoas."""

from .pessoa import Pessoa


class CadastroPessoas:
    """Encapsula o estado e as operações do cadastro de pessoas."""

    def __init__(self):
        self._pessoas = []

    def cadastrar(self, nome, idade, email):
        """Cadastra uma pessoa e retorna o registro criado."""
        pessoa = Pessoa(nome, idade, email)
        self._pessoas.append(pessoa)
        return pessoa

    def consultar(self, nome):
        """Retorna a pessoa com o nome informado ou None."""
        return next(
            (pessoa for pessoa in self._pessoas if pessoa.nome == nome),
            None,
        )

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        """Altera a pessoa encontrada e retorna True quando ela existe."""
        pessoa = self.consultar(nome)
        if pessoa is None:
            return False

        pessoa.nome = novo_nome
        pessoa.idade = nova_idade
        pessoa.email = novo_email
        return True

    def listar(self):
        """Retorna uma cópia da lista de pessoas."""
        return list(self._pessoas)

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
