""""Modelo de uma pessoa cadastrada."""


class Pessoa:  # pylint: disable=too-few-public-methods
    """Representa uma pessoa e expõe seus dados por propriedades."""

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
