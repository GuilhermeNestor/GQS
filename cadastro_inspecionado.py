def

nome1 = ""
idade1 = 0
email1 = ""
nome2 = ""
idade2 = 0
email2 = ""
nome3 = ""
idade3 = 0
email3 = ""
 
qtd = 0
op = 0

def analisar_pessoa(nomes, idades, emails):
    procurado = input("Nome para analisar: ")
    pos = buscar_pessoa(nomes, procurado)

    if pos == -1:
        print("Pessoa nao encontrada")
    else:
        idade = idades[pos]
        email = emails[pos]

        if idade < 12:
            print("Faixa etaria: Crianca")
        elif idade < 18:
            print("Faixa etaria: Adolescente")
        elif idade < 30:
            print("Faixa etaria: Adulto jovem")
        elif idade < 60:
            print("Faixa etaria: Adulto")
        else:
            print("Faixa etaria: Idoso")

        if email == "":
            print("Cadastro incompleto: sem e-mail")
        else:
            if "@" not in email:
                print("E-mail invalido")
            else:
                if email.endswith("@gmail.com"):
                    print("Provedor: Gmail")
                elif email.endswith("@outlook.com"):
                    print("Provedor: Outlook")
                elif email.endswith("@hotmail.com"):
                    print("Provedor: Hotmail")
                elif email.endswith("@utfpr.edu.br"):
                    print("Provedor: UTFPR")
                else:
                    print("Provedor: Outro")

        if idade >= 18 and email != "":
            print("Cadastro apto para contato")
        elif idade >= 18 and email == "":
            print("Maior de idade sem contato")
        elif idade < 18 and email != "":
            print("Menor de idade com contato")
        else:
            print("Menor de idade sem contato")

while op != 5:
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    op = int(input("Escolha uma opcao: "))
 
    if op == 1:
        if qtd == 3:
            print("Cadastro cheio")
        else:
            n = input("Nome: ")
            i = int(input("Idade: "))
            e = input("E-mail: ")
            if qtd == 0:
                nome1 = n
                idade1 = i
                email1 = e
            elif qtd == 1:
                nome2 = n
                idade2 = i
                email2 = e
            else:
                nome3 = n
                idade3 = i
                email3 = e
            qtd = qtd + 1
            print("Pessoa cadastrada!")
            print("Nome: " + n)
            print("Idade: " + str(i))
            print("E-mail: " + e)
            if i >= 18:
                print("Situacao: Maior de idade")
            else:
                print("Situacao: Menor de idade") 
    elif op == 2:
        b = input("Nome para consultar: ")
        achou = 0
        if qtd >= 1 and b == nome1:
            achou = 1
            print("Nome: " + nome1)
            print("Idade: " + str(idade1))
            print("E-mail: " + email1)
            if idade1 >= 18:
                print("Situacao: Maior de idade")
            else:
                print("Situacao: Menor de idade")
        if qtd >= 2 and b == nome2:
            achou = 1
            print("Nome: " + nome2)
            print("Idade: " + str(idade2))
            print("E-mail: " + email2)
        if qtd >= 3 and b == nome3:
            achou = 1
            print("Nome: " + nome3)
            print("Idade: " + str(idade3))
            print("E-mail: " + email3)
        if achou == 0:
            print("Nao encontrado") 
    elif op == 3:
        b = input("Nome para alterar: ")
        achou = 0
        if b == nome1:
            achou = 1
            print("Dados atuais:")
            print("Nome: " + nome1)
            print("Idade: " + str(idade1))
            print("E-mail: " + email1)
            n = input("Novo nome: ")
            i = int(input("Nova idade: "))
            e = input("Novo e-mail: ")
            nome1 = n
            idade1 = i
            if e != "":
                email1 = e
            print("Alterado!")
        elif b == nome2:
            achou = 1
            print("Dados atuais:")
            print("Nome: " + nome2)
            print("Idade: " + str(idade2))
            print("E-mail: " + email2)
            n = input("Novo nome: ")
            i = int(input("Nova idade: "))
            e = input("Novo e-mail: ")
            nome2 = n
            idade2 = i
            email2 = e
            print("Alterado!")
        elif b == nome3:
            achou = 1
            print("Dados atuais:")
            print("Nome: " + nome3)
            print("Idade: " + str(idade3))
            print("E-mail: " + email3)
            n = input("Novo nome: ")
            i = int(input("Nova idade: "))
            e = input("Novo e-mail: ")
            nome3 = n
            idade3 = i
            email3 = e
            print("Alterado!")
        if achou == 0:
            print("Nao encontrado") 
    elif op == 4:
        if qtd == 0:
            print("Nenhuma pessoa cadastrada")
        if qtd >= 1:
            print("Nome: " + nome1)
            print("Idade: " + str(idade1))
            print("E-mail: " + email1)
            print("-------------------------")
        if qtd >= 2:
            print("Nome: " + nome2)
            print("Idade: " + str(idade2))
            print("E-mail: " + email2)
            print("-------------------------")
        if qtd >= 3:
            print("Nome: " + nome3)
            print("Idade: " + str(idade3))
            print("E-mail: " + email3)
            print("-------------------------")
        print("Total: " + str(qtd)) 
    elif op == 5:
        print("Saindo...")
 
    else:
        print("Opcao invalida")
 
print("Fim do programa")