def main():
    option = input('selecione a questao: ')
    if option == '1':
        first()
    elif option == '2':
        second()

def first():
    list = []
    x = range(5)
    for n in x:
        num = int(input('botai o numero: '))
        list.append(num)
    else:
        print(list)


def second():
    list = []
    x = range(10)
    for n in x:
        num = int(input('botai o numero: '))
        list.append(num)
    else:
        print(list.reverse())



main()

