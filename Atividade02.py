def main():
    option = input('selecione a questao: ')
    if option == '1':
        first()
    elif option == '2':
        second()
    elif option == '3':
        third()
    elif option == '4':
        fourth()
    elif option == '5':
        fifth()


def first():
    number = int(input('insira o numero'))
    print('é par') if number%2 == 2  else print('impar')


def second():
   number1 = int(input('numero 1: '))
   number2 = int(input('numero 2: '))
   num = number1 - number2
   print(number1, 'é o maior') if num > 0 else print(number2, 'é o maior')
   print('a diferença é de: ', num)


def third():
    number1 = int(input('numero 1: '))
    number2 = int(input('numero 2: '))
    num = number1 - number2
    if num > 0:
        print(number1, 'é o maior')
    elif num == 0:
        print('numeros iguais')
    else:
        print(number2, 'é o maior')


def fourth():
    nota1 = float(input('nota 1 do safado: '))
    nota2 = float(input('nota 2 do safado: '))
    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
        media = (nota1 + nota2)/2
        print('eh a media ', media)
    else:
        print('nota invalida')



def fifth():
    salarioooo = float(input('vala qto tu ganha ae rei: '))
    prestaCAO = float(input('fala a parcela do celta ae: '))
    vintePorcente = 20 * (salarioooo/100)
    if prestaCAO >= vintePorcente:
        print('mermao num da nao')
    else:
        print('ta aprovadooooooooooooooooooo')


main()