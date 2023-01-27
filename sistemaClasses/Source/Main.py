
import Function as F1;
import Funcionary as F2;
import utils


def main():
    global sendThis
    option = int(input('1. Manipular Funcionários \n2. Manipular Fuções\n'))
    if option == 1:
            if utils.has_some('funcao') > 0:
                optionProletario = int(input('1. Cadastrar Funcionário\n2. Pesquisar Funcionário\n3. Editar Funcionário\n4. Deletar Funcionário \n0. Voltar ao Menu Principal\n'))
                if utils.has_some('funcionario') > 0:
                    if optionProletario > 1:
                        cpf_value = int(input('Insira o cpf do funcionário: '))
                        utils.find_some('funcionario', 'cpf', cpf_value)
                        if optionProletario == 3:
                            change_user(cpf_value)
                        elif optionProletario == 4:
                            utils.delete_some('funcionario', 'cpf', cpf_value)
                    elif optionProletario == 1:
                        new_user()
                elif optionProletario == 0:
                    return 0
                else:
                    print('Sem funcionários cadastrados')
                    main()
            else:
                print('Sem cargos cadastrados')
                main()

    if option == 2:
        optionCargo = int(input('1. Cadastrar Função\n2. Pesquisar Função\n3. Editar Função\n4. Deletar Função \n0. Voltar ao Menu Principal\n'))
        if optionCargo > 1:
            if utils.has_some('funcao') > 0:
                cod_value = int(input('Insira o código da função: '))
                utils.find_some('funcao', 'cod', cod_value)
                if optionCargo == 3:
                    change_func(cod_value)
                elif optionCargo == 4:
                    utils.delete_some('funcao', 'cod', cod_value)
            elif optionCargo == 0:
                return 0
            else:
                print('Sem cargos cadastrados')
                main()
        elif optionCargo == 1:
            new_func()
    else:
        main()


def new_user():
    name = input('Nome do funcionário: ')
    cpf = int(input('Cpf do funcionário: '))
    id = input('Id do cargo a ser adicionado:  ')
    salario = float(input('salario do funcionário'))
    zap = int(input('zap zap: '))
    funcionario = F2.Functionary(name, cpf, id, salario, zap)
    utils.send_functionary(funcionario)


def change_user(value):
    print('O que deseja mudar? (Escreva DE FORMA CORRETA o nome correspondente) ')
    column = input('1. nome\n2. cpf \n3. funcao \n4. salario \n5. telefone\n').lower()
    value_column = input('insira o novo valor de, {} : '.format(column))
    utils.change('funcionario',  column, value_column, 'cpf', value,)


def new_func():
    name = input('Nome do cargo: ')
    cod = int(input('Codigo do cargo: '))
    cargo = F1.Function(cod, name)
    utils.send_function(cargo)


def change_func(value):
    print('O que deseja mudar? (Escreva DE FORMA CORRETA o nome correspondente) ')
    column = input('1. cod\n2. nome\n').lower()
    value_column = input('insira o novo valor de, {} : '.format(column))
    utils.change('funcao',  column, value_column, 'cod', value,)




main()

