from typing import Dict, List, Any

allUsers = []


def main():
    optionMenu = int(input('1-Cadastrar caba\n2-Pesquisar Funcionario'
                           '\n3-Cadastrar o zap \n4-muda o caba '
                           '\n5-apaga esse safado \n0- borinbora?\n'))
    if optionMenu == 1:
        user = None
        userData()
    elif optionMenu == 0:
        return 0
    elif optionMenu <= 5:
        if allUsers:
            numberOfAccount = int(input('cpf do safado(somente numeros): '))
            for cpf in allUsers.key():
                print(cpf)
        else:
            tryAgain()
    else:
        print('escolha um valor correto!')
        main()


def userData():
    global newUser
    name = input('Nome do caba: ')
    cpf = int(input('cpf do safado: '))
    whatDo = input('qq esse corno faz ae ')
    ammount = float(input('quanto esse corno recebe '))
    tel = []
    tel.append(input('insira o numero'))
    newUser = dict([('name', name), ('cpf', cpf), ('cargo', whatDo), ('salario', ammount), ('numeros', tel)])
    print(newUser)


def usersControl(user):
    if user:
        print(allUsers)
        main()
    else:
        allUsers.append(userData())
        print(allUsers)
        main()




def tryAgain():
    print('Erro, tente novamente!')
    main()


main()
