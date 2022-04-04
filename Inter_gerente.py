# interface do gerente
import random
import secrets
import pickle

print("Bem vindo ao Banco Alfa!")
print("Fazemos o que nenhum banco faz por você!")
agenda = []
with open("agenda.p", "rb") as f:
    agenda = pickle.load(f)
    print(agenda)



def cadastro():
    nome = input("digite o nome do cliente: ")
    profissão = input("digite a profissão do cliente: ")
    renda = input("digite o renda do cliente: ")
    endereço = input("digite o endereço do cliente: ")
    telefone = input("digite o telefone: ")
    conta = (random.randint(10000, 99999))
    senha = 1234

    cliente = [nome, profissão, renda, endereço, telefone, conta, senha]
    return cliente


def busca(agenda, nome_busca):
    # lista de resultados da busca
    lista_resultados = []
    for nome, profissao, renda, endereco, telefone, conta, senha in agenda:
        if nome_busca in nome:
            lista_resultados.append(
                (nome, profissao, renda, endereco, telefone, conta, senha))

    # retorno todos os resultados
    return lista_resultados


def listar(agenda):
    for cliente in agenda:
        print(
            f'nome:{cliente[0]} \n profissão:{cliente[1]} \n renda:{cliente[2]} \n #endereço:{cliente[3]} \n telefone:{cliente[4]} \n conta bancária: {cliente[5]} \t #senha:  {cliente[6]} \n \t \t |(A SENHA DEVE SER ALTERADA APÓS A CRIAÇÃO DA CONTA!)| \n Observação: A senha é gerada automaticamente pelo sistema (padrão alfanumérico).'
        )


def alterar_senha(agenda):
    # preciso encontrar qual elemento vai ser alterado
    nome_busca = input('Digite o nome do cliente:')
    # guardando o indice do contato a ser alterado
    indice_alteracao = -1
    # definir
    for i in range(len(agenda)):
        cliente = agenda[i]
        # o nome eh exatamente igual ao nome buscado?
        if nome_busca == cliente[0]:
            indice_alteracao = i
            break

    # verificando se eu achei o contato
    if indice_alteracao != -1:
        nova_senha = secrets.token_hex(4)
        print(
            f'\n \t \t #SENHA ALTERADA COM SUCESSO!!! \n Sua Nova senha é:{nova_senha}'
        )
        cliente = agenda[indice_alteracao]
        # contato agora tem um novo nome, mas telefone e email sao iguais
        cliente = cliente[0], cliente[1], cliente[2], cliente[3], cliente[
            4], cliente[5], nova_senha
        # mudando o contato na agenda tb
        agenda[indice_alteracao] = cliente
    else:
        print('Nao encontrei o contato a ser alterado!')
    # alterar o contato especifico
    return agenda


def menu():
    print("-" * 30)
    print("1 - cadastro novo cliente")
    print("2 - busca de cliente")
    print("3 - listar clientes")
    print("4 - gerar nova senha bancária")
    print("5 - fechar")
    print("-" * 30)


# criando uma agenda vazia
# para sempre, fico em repetição apresentando o menu
while True:
    menu()
    opção = int(input("Qual opção você deseja? \t"))
    if opção == 1:
        # cadastro
        cliente = cadastro()
        agenda.append(cliente)

    elif opção == 2:
        # buscar cliente
        nome_buscar = input("digite o nome que você deseja buscar: ")
        resultado = busca(agenda, nome_buscar)
        listar(resultado)

    elif opção == 3:
      listar(agenda)
    elif opção == 4:
        agenda = alterar_senha(agenda)

    elif opção == 5:
        # encerrar o software
        # exit()
        with open('agenda.p', 'wb') as file:
            pickle.dump(agenda, file)
            file.close()

            break
    else:
        print('Digite algo valido!')
