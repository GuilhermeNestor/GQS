"""Sistema de Cadastro de Pessoas - versao 2
   novos requisitos: menu, consulta, alteracao e listagem"""
def menu():
    """Exibe o menu principal e retorna a opção escolhida pelo usuário.

    Recebe: nenhum parâmetro; lê a opção diretamente pelo input.
    Como funciona: mostra as ações disponíveis e converte a escolha para inteiro.
    Retorna: um número inteiro com a opção selecionada pelo usuário.
    """
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

    return opcao

def cadastrar_pessoa(nomes, idades, emails):
    """Cadastra uma pessoa nova nas listas de nomes, idades e e-mails.

    Recebe: nomes (lista de nomes), idades (lista de idades) e emails (lista de e-mails).
    Como funciona: solicita nome, idade e e-mail ao usuário, salva cada dado em sua lista
    e informa se a pessoa é maior ou menor de idade.
    Retorna: nenhum valor explícito; atualiza as listas e imprime a situação.
    """
    novo_nome = input("digite o nome da pessoa: ")
    nomes.append(novo_nome)
    nova_idade = int(input("digite a idade da pessoa: "))
    idades.append(nova_idade)
    novo_email = input("digite o email da pessoa: ")
    emails.append(novo_email)

    if nova_idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def consultar_pessoa(nomes):
    """Solicita um nome para consultar e tenta localizar a pessoa cadastrada.

    Recebe: nomes, a lista com os nomes cadastrados.
    Como funciona: lê o nome pesquisado e chama a busca na lista para localizar o registro.
    Retorna: o valor devolvido por buscar_pessoa, que normalmente é o índice encontrado ou -1.
    """
    b = input("Nome para consultar:")
    buscar_pessoa(b, nomes)

def buscar_pessoa(b, nomes):
    """Busca um nome na lista e exibe os dados da pessoa correspondente.

    Recebe: b (nome a ser procurado) e nomes (lista de nomes cadastrados).
    Como funciona: percorre a lista em busca do nome informado; quando encontra, chama exibir_pessoa
    com o índice correspondente e retorna esse índice.
    Retorna: o índice da pessoa encontrada ou -1 caso não exista.
    """
    for i, nome_pessoas in enumerate((nomes)):
        if b == nome_pessoas:
            exibir_pessoa(i)
            return i
    print("Nao encontrado")
    return -1

def exibir_pessoa(i):
    """Mostra na tela os dados completos da pessoa no índice informado.

    Recebe: i, o índice da pessoa nas listas globais nome, idade e email.
    Como funciona: acessa as listas globais usando o mesmo índice e imprime cada dado em texto.
    Retorna: nenhum valor; apenas exibe as informações no console.
    """
    print("Nome: " + nome[i])
    print("Idade: " + str(idade[i]))
    print("E-mail: " + email[i])
    print("-------------------------")

def alterar_pessoa(nomes, idades, emails):
    """Altera os dados de uma pessoa cadastrada pelo nome informado.

    Recebe: i (índice da pessoa), nomes, idades e emails, listas com os dados do cadastro.
    Como funciona: busca o nome desejado, mostra os dados antigos e solicita novos valores para
    atualizar o registro na mesma posição.
    Retorna: nenhum valor explícito; modifica diretamente as listas.
    """
    b = input("Nome para alterar:")
    for i, nome_pessoa in enumerate((nomes)):
        if b == nome_pessoa:
            exibir_pessoa(i)
            nomes[i] = input("digite o novo nome da pessoa: ")
            idades[i] = int(input("digite a nova idade da pessoa: "))
            emails[i] = input("digite o novo email da pessoa: ")
        else:
            print("Nao encontrado")

def listar_pessoas(nomes, idades, emails):
    """Lista todos os cadastros existentes nas listas de dados.

    Recebe: nomes, idades e emails, contendo os registros do sistema.
    Como funciona: percorre cada índice das listas e imprime os dados de cada pessoa em sequência.
    Retorna: nenhum valor; apenas exibe a listagem no terminal.
    """
    print("Listagem de pessoas cadastradas:")
    for i, nome_pessoa in enumerate((nomes)):
        print("Nome: " + nome_pessoa)
        print("Idade: " + str(idades[i]))
        print("E-mail: " + emails[i])
        print("-------------------------")

def analisar_pessoa(nomes):
    """Analisa uma pessoa e mostra informações sobre seu cadastro.

    Recebe: nomes, lista contendo os nomes cadastrados.
    Como funciona: solicita o nome da pessoa, localiza sua posição, e chama funções que avaliam
    faixa etária, e-mail, provedor e condição de contato.
    Retorna: nenhum valor explícito; imprime os resultados da análise.
    """
    busca = input("Nome para analisar: ")
    pos = buscar_pessoa(busca, nomes)
    if pos == -1:
        print("Pessoa nao encontrada")

    classificar_faixa_etaria(pos)

    avaliar_email(pos)

    identificar_provedor(pos)

    definir_condicao_contato(pos)



def classificar_faixa_etaria(pos):
    """Classifica a pessoa de acordo com a faixa etária.

    Recebe: pos, a posição da pessoa na lista global de idades.
    Como funciona: compara a idade com faixas pré-definidas, como criança, adolescente,
    adulto jovem, adulto e idoso.
    Retorna: nenhum valor; imprime a classificação do perfil.
    """
    if pos == -1:
        print("Pessoa nao encontrada")
    else:
        verificar = idade[pos]
        if verificar < 12:
            print("Faixa etaria: Crianca")
        elif verificar < 18:
            print("Faixa etaria: Adolescente")
        elif verificar < 30:
            print("Faixa etaria: Adulto jovem")
        elif verificar < 60:
            print("Faixa etaria: Adulto")
        else:
            print("Faixa etaria: Idoso")


def avaliar_email(pos):
    """Verifica se o e-mail da pessoa está preenchido e tem formato básico.

    Recebe: pos, a posição da pessoa nas listas globais.
    Como funciona: verifica se o campo de e-mail está vazio e depois analiza se o caractere '@'
    está presente para validar a estrutura.
    Retorna: nenhum valor; imprime mensagens sobre o estado do e-mail.
    """
    if email[pos] == "":
        print("Cadastro incompleto: sem e-mail")
    else:
        if "@" not in email[pos]:
            print("E-mail invalido")


def identificar_provedor(pos):
    """Identifica o provedor do e-mail informado pela pessoa.

    Recebe: pos, a posição da pessoa nas listas globais.
    Como funciona: verifica o final do e-mail e compara com domínios conhecidos, como Gmail,
    Outlook, Hotmail, UTFPR e outros.
    Retorna: nenhum valor; imprime o nome do provedor detectado.
    """
    if email[pos].endswith("@gmail.com"):
        print("Provedor: Gmail")
    elif email[pos].endswith("@outlook.com"):
        print("Provedor: Outlook")
    elif email[pos].endswith("@hotmail.com"):
        print("Provedor: Hotmail")
    elif email[pos].endswith("@utfpr.edu.br"):
        print("Provedor: UTFPR")
    else:
        print("Provedor: Outro")

def definir_condicao_contato(pos):
    """Avalia se o cadastro está apto para contato com base na idade e no e-mail.

    Recebe: pos, a posição da pessoa nas listas globais.
    Como funciona: verifica se a pessoa é maior de idade e se o e-mail foi preenchido, emitindo
    uma mensagem conforme as regras de contato.
    Retorna: nenhum valor; apenas exibe a condição do cadastro.
    """
    if idade[pos] >= 18 and email[pos] != "":
        print("Cadastro apto para contato")
    elif idade[pos] >= 18 and email[pos] == "":
        print("Maior de idade sem contato")
    elif idade[pos] < 18 and email[pos] != "":
        print("Menor de idade com contato")
    else:
        print("Menor de idade sem contato")

nome = []
idade = []
email = []

QTD = 0
op = 0

while op != 6:

    op = menu()

    if op == 1:
        cadastrar_pessoa(nome, idade, email)
    elif op == 2:
        consultar_pessoa(nome)
    elif op == 3:
        alterar_pessoa(nome, idade, email)
    elif op == 4:
        listar_pessoas(nome, idade, email)
    elif op == 5:
        analisar_pessoa(nome)
    elif op == 6:
        print("Saindo...")
    else:
        print("Opcao invalida")

print("Fim do programa")
