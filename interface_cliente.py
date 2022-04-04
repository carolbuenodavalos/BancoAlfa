import pickle
#import numpy


a = open( 'agenda.p', 'rb' )    # 'r' para leitura; pode ser omitido mydict
dados_clientes = pickle.load(a)          # carregar o conteúdo do arquivo como mydict
a.close()





print("Bem vindo ao Banco Alfa!")
print("Fazemos o que nenhum outro banco faz por você!")

global montante
montante = 0



def menu():
    print("-" * 30)
    print("1 - Saque ")
    print("2 - Depósito ")
    print("3 - Visualizar saldo")
    print("4 - Simulador de investimento")
    print("5 - Finalizar ações.")
    print("-" * 30)

def deposito():
    conta_bancaria = input("Digite sua conta bancária:")
    senha_conta = int(input('Digite a senha da sua conta bancária:'))
    # percorrendo lista externa
    for i in dados_clientes:
        # verificando se o valor buscado esta dentro de alguma lista interna
        if i[5] == senha_conta and i[6] == conta_bancaria:
            deposito = float(input("Qual valor você gostaria de depositar? "))
            global montante
            montante_total = montante + deposito
            print(f'Saldo atual:R$ {montante_total}')
            montante = montante_total
            return montante

    else:
        # caso o valor buscado nao seja encontrado
        print('Desculpe! Não encontramos esta conta em nosso sistema!')
        return None






def saldo():
  global montante
  print(montante)


def saque():
    conta_bancaria = input("Digite sua conta bancária:")
    senha_conta = int(input('Digite a senha da sua conta bancária:'))
    # percorrendo lista externa
    for i in dados_clientes:
        # verificando se o valor buscado esta dentro de alguma lista interna
        if i[5] == senha_conta and i[6] == conta_bancaria:
          global montante
          valor_saque = float(input("Valor do saque: "))
          if valor_saque > montante:
            print("Desculpe, saldo insuficiente.")
          else:
            montante = (montante - valor_saque)
            print(f'Saldo atual:R$ {montante} ')
    else:
        # caso o valor buscado nao seja encontrado
        print('Desculpe! Não encontramos esta conta em nosso sistema!')
        return None


def investir():
    investimento = float(input("Valor inicial do investimento: "))
    meses = float(input("Por quantos meses será o investimento? "))
    taxa = 1.5
    if meses >= 60:

        calculo_investimento = investimento * ((1 + taxa / 100) ** meses)

        subtrair_lucro = calculo_investimento - investimento
        taxa_adm = (0.5 / 100) * subtrair_lucro
        total_investimento = calculo_investimento - taxa_adm
        print(f' Valor total ao final dos meses de investimento: R$ {total_investimento:.2f}')

    elif meses < 60:
        calculo_investimento = investimento * ((1 + taxa / 100) ** meses)

        subtrair_lucro = calculo_investimento - investimento
        taxa_adm = (1 / 100) * subtrair_lucro
        total_investimento = calculo_investimento - taxa_adm
        print(f' Valor total ao final dos meses de investimento: R$ {total_investimento:.2f}')

while True:
    menu()
    opção = int(input("Qual opção você deseja? \t"))
    if opção == 1:
        # SAQUE
        saque()

    elif opção == 2:
        # DEPOSITO
        deposito()

    elif opção == 3:
        # SALDO
        saldo()

    elif opção == 4:
        # SIMULA INVESTIMENTO
        investir()

    elif opção == 5:
        # FECHA SISTEMA
        break
    else:
        print("Digite uma opção válida")