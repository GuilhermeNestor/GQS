"""Interface do sistema de cadastro de pessoas."""

from .cadastro_pessoas import CadastroPessoas


def menu(cadastro):
    """Exibe o menu e executa as operações do cadastro."""
    while True:
        print("=========================")
        print(" CADASTRO DE PESSOAS")
        print("=========================")
        print("1 - Cadastrar pessoa")
        print("2 - Consultar pessoa")
        print("3 - Alterar pessoa")
        print("4 - Listar pessoas")
        print("5 - Analisar pessoa")
        print("6 - Sair")

        opcao = int(input("Escolha uma opcao: "))
        if opcao == 1:
            nome = input("Digite o nome da pessoa: ")
            idade = int(input("Digite a idade da pessoa: "))
            email = input("Digite o email da pessoa: ")
            cadastro.cadastrar(nome, idade, email)
        elif opcao == 2:
            nome = input("Nome para consultar: ")
            pessoa = cadastro.consultar(nome)
            if pessoa is not None:
                print(f"Nome: {pessoa.nome}")
                print(f"Idade: {pessoa.idade}")
                print(f"E-mail: {pessoa.email}")
        elif opcao == 3:
            nome = input("Nome para alterar: ")
            novo_nome = input("Digite o novo nome da pessoa: ")
            nova_idade = int(input("Digite a nova idade da pessoa: "))
            novo_email = input("Digite o novo email da pessoa: ")
            cadastro.alterar(nome, novo_nome, nova_idade, novo_email)
        elif opcao == 4:
            for pessoa in cadastro.listar():
                print(f"Nome: {pessoa.nome}")
                print(f"Idade: {pessoa.idade}")
                print(f"E-mail: {pessoa.email}")
        elif opcao == 5:
            nome = input("Nome para analisar: ")
            analise = cadastro.analisar(nome)
            if analise is not None:
                print(f"Faixa etaria: {analise['faixa_etaria']}")
                print(f"Provedor: {analise['provedor']}")
                print(
                    "Cadastro apto para contato"
                    if analise["apto_para_contato"]
                    else "Cadastro sem contato"
                )
        elif opcao == 6:
            print("Saindo...")
            return
        else:
            print("Opcao invalida")


if __name__ == "__main__":
    menu(CadastroPessoas())
