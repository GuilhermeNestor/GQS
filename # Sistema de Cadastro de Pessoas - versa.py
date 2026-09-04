# Sistema de Cadastro de Pessoas - versao 2
# novos requisitos: menu, consulta, alteracao e listagem
 
def menu():
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    op = int(input("Escolha uma opcao: "))

    return op

def cadastrar_pessoa(nomes, idades, emails):
    nome = input("digite o nome da pessoa: ")
    nomes.append(nome)
    idade = int(input("digite a idade da pessoa: "))
    idades.append(idade)
    email = input("digite o email da pessoa: ")
    emails.append(email)

    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

nome = [] 
idade = []
email = []
 
qtd = 0
op = 0
 
while op != 5:

    op = menu()
 
    if op == 1:
            cadastrar_pessoa(nome, idade, email)
    elif op == 2:
        b = input("Nome para consultar:")
        for i in range(len(nome)):
            if b == nome[i]:
                print("Nome: " + nome[i])
                print("Idade: " + str(idade[i]))
                print("E-mail: " + email[i])
                break
            else:
                print("Nao encontrado")
     
    elif op == 3:
        b = input("Nome para alterar: ")
        for i in range(len(nome)):
            if b == nome[i]:
                print("Nome: " + nome[i])
                print("Idade: " + str(idade[i]))
                print("E-mail: " + email[i])
                print("-------------------------")
                nome[i] = input("digite o novo nome da pessoa: ")
                idade[i] = int(input("digite a nova idade da pessoa: "))
                email[i] = input("digite o novo email da pessoa: ")
                break
            else:
                print("Nao encontrado")
    elif op == 4:
        print("Listagem de pessoas cadastradas:")
        for i in range(len(nome)):
            print("Nome: " + nome[i])
            print("Idade: " + str(idade[i]))
            print("E-mail: " + email[i])
            print("-------------------------")
    elif op == 5:
        print("Saindo...")
    else:
        print("Opcao invalida")
 
print("Fim do programa")