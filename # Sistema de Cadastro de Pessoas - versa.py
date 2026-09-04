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

def consultar_pessoa(nomes):
    b = input("Nome para consultar:")
    buscar = buscar_pessoa(b, nomes)

def buscar_pessoa(b, nomes):
    for i in range(len(nomes)):
        if b == nomes[i]:
            exibir_pessoa(i)
            return i
    print("Nao encontrado")
    return -1

def exibir_pessoa(i):
    print("Nome: " + nome[i])
    print("Idade: " + str(idade[i]))
    print("E-mail: " + email[i])
    print("-------------------------")

def alterar_pessoa(i, nomes, idades, emails):
    b = input("Nome para alterar:")
    for i in range(len(nomes)):
            if b == nomes[i]:
                exibir_pessoa(i)
                nomes[i] = input("digite o novo nome da pessoa: ")
                idades[i] = int(input("digite a nova idade da pessoa: "))
                emails[i] = input("digite o novo email da pessoa: ")
            else:
                print("Nao encontrado")

def listar_pessoas(nomes, idades, emails):
    print("Listagem de pessoas cadastradas:")
    for i in range(len(nomes)):
        print("Nome: " + nomes[i])
        print("Idade: " + str(idades[i]))
        print("E-mail: " + emails[i])
        print("-------------------------")



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
        i = consultar_pessoa(nome)
     
    elif op == 3:
        alterar_pessoa(i, nome, idade, email)
    elif op == 4:
        listar_pessoas(nome, idade, email)
    elif op == 5:
        print("Saindo...")
    else:
        print("Opcao invalida")
 
print("Fim do programa")