"""Armazenamento de pessoas na tabela pessoa do MySQL."""

import os

import mysql.connector
from mysql.connector.constants import ClientFlag

from .pessoa import Pessoa
from .repositorio_pessoas import RepositorioPessoas


class RepositorioPessoasMySQL(RepositorioPessoas):
    """Persiste pessoas na tabela pessoa do MySQL principal."""

    def __init__(self, host, port, usuario, senha, banco):
        self._config = {
            "host": host,
            "port": port,
            "user": usuario,
            "password": senha,
            "database": banco,
            "client_flags": [ClientFlag.FOUND_ROWS],
        }

    @classmethod
    def a_partir_do_ambiente(cls):
        """Lê a configuração das variáveis de ambiente."""
        return cls(
            host=os.environ.get("DB_HOST", "localhost"),
            port=int(os.environ["DB_PORT"]),
            usuario=os.environ["DB_USER"],
            senha=os.environ["DB_PASSWORD"],
            banco=os.environ.get("DB_NAME", "cadastro"),
        )

    def _conectar(self):
        """Abre uma nova conexão com o MySQL principal."""
        return mysql.connector.connect(**self._config)

    def _executar(self, sql, valores):
        """Executa INSERT/UPDATE em transação e devolve as linhas afetadas."""
        conexao = self._conectar()
        try:
            cursor = conexao.cursor()
            try:
                cursor.execute(sql, valores)
                conexao.commit()
                return cursor.rowcount
            finally:
                cursor.close()
        except mysql.connector.Error:
            conexao.rollback()
            raise
        finally:
            conexao.close()

    def _consultar(self, sql, valores=()):
        """Executa um SELECT e devolve todas as linhas."""
        conexao = self._conectar()
        try:
            cursor = conexao.cursor()
            try:
                cursor.execute(sql, valores)
                return cursor.fetchall()
            finally:
                cursor.close()
        finally:
            conexao.close()

    @staticmethod
    def _para_pessoa(linha) -> Pessoa:
        """Converte uma linha (nome, idade, email) em Pessoa."""
        nome, idade, email = linha
        return Pessoa(nome, idade, email)

    def cadastrar(self, pessoa: Pessoa) -> Pessoa:
        sql = "INSERT INTO pessoa (nome, idade, email) VALUES (%s, %s, %s)"
        self._executar(sql, (pessoa.nome, pessoa.idade, pessoa.email))
        return pessoa

    def buscar(self, nome: str) -> Pessoa | None:
        sql = "SELECT nome, idade, email FROM pessoa WHERE nome = %s ORDER BY id LIMIT 1"
        linhas = self._consultar(sql, (nome,))
        return self._para_pessoa(linhas[0]) if linhas else None

    def listar(self) -> list[Pessoa]:
        sql = "SELECT nome, idade, email FROM pessoa ORDER BY id"
        return [self._para_pessoa(linha) for linha in self._consultar(sql)]

    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        sql = "UPDATE pessoa SET nome = %s, idade = %s, email = %s WHERE nome = %s"
        valores = (nova_pessoa.nome, nova_pessoa.idade, nova_pessoa.email, nome)
        return self._executar(sql, valores) > 0
