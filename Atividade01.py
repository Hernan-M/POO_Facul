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
    elif option == '6':
        sixth()
    elif option == '7':
        seven()
    elif option == '8':
        oct()
    elif option == '9':
        nine()
    else:
        ten()


def first():
    salary = int(input('qto q o caba ta ganhano? '))
    salary = 25 * (salary / 100) + salary
    print('agr ele ganha issaq: ', salary)


def second():
    total = 780000.00
    percent = (total/100)
    first = percent * 46
    second = percent * 32
    lastOne = total - (first + second)
    print('O primeiro ganhou : ', first, '\nO segundo: ', second, '\nO ultimo: ',lastOne)


def third():
    daysOfWork = int(input('Insira os dias:  '))
    parcialSalary = daysOfWork * 30
    total = parcialSalary - 8 * (parcialSalary/100)
    print('O encanador receberá: ', total)

def fourth():
    hourValue = int(input('Insira o valor da hora: '))
    hourWorked = int(input('Insira o numero de horas trabalhadas: '))
    parcialValue = hourValue * hourWorked
    total = parcialValue + 10 *(parcialValue/100)
    print('o valor pago sera: ', total)

def fifth():
    salary = int(input('insira o salario base: '))
    salary = salary - 2 * (salary/100)
    print(salary)


def sixth():
    value =int(input('insira o valor: '))
    discountTen = value - 10  * (value/100)
    parcel = value/3
    comissionOne = 5 * (discountTen/100)
    comissionTwo =  5 * (value / 100)
    print('desconto 10%: ',discountTen, '\nparcelas: ', parcel,'\ncomissao a vista: ',comissionOne,'\ncomissao parcelada',comissionTwo)


def seven():
   heightDegrau =  float(input('mermao fala o tamanho desses degrau ae: '))
   heightSla =  float(input('agr ate onde tu quer ir: '))
   degraus = heightSla/heightDegrau
   print('tu vai andar nada mais nada menos q ', degraus, 'degraus, ok? (maluco)')


def oct():
    seconds = int(input('segundos ae amigao: '))
    minute = seconds/60
    hour =  minute/60
    print(hour,' horas, ',minute,' minutos e ',seconds,' segundos')

def nine():
    hour = int(input('fala a hora ae: '))
    minute = int(input('fala o minuto ae: '))
    second = int(input('segundos? '))
    totalSecond = second + (minute*60) + (hour*3600)
    duration = int(input('qto tempo durou em segundos? '))
    totalTime = totalSecond + duration
    print(totalTime, 'faz as conta ae')
    # a ultima parte achei chatinha e eu tava com sono :( #

def ten():
    ano = int(input('insira o ano: '))
    edad= int(input('insira la edad: '))
    anoNasc = ano - edad
    print('manito tu nasceste en: ', anoNasc)



main()