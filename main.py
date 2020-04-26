from Rim import *

menu = 0
while int(menu) != 3:
    menu = input('\n' + 'Выберите требуемую операцию:' + '\n' +
                 '1. Перевести в арабские цифры' + '\n' +
                 '2. Выполнить арифметические операции' + '\n' +
                 '3. Выйти из программы' + '\n')

    if int(menu) == 1:
        rim1 = Rim(input('Введите первое число римскими цифрами: ').upper())
        rim2 = Rim(input('Введите втоое число римскими цифрами: ').upper())
        print('Первое число арабскими: ', rim1)
        print('Второе число арабскими: ', rim2)

    elif int(menu) == 2:
        calc = input('Введите арифметическое выражение с двумя римскими числами: ').upper()
        calc = calc.replace(' ', '')

        if calc.find('+') != -1:
            print(Rim(calc[:calc.find('+')]) + Rim(calc[calc.find('+') + 1:]))
        elif calc.find('-') != -1:
            print(Rim(calc[:calc.find('-')]) - Rim(calc[calc.find('-') + 1:]))
        elif calc.find('*') != -1:
            print(Rim(calc[:calc.find('*')]) * Rim(calc[calc.find('*') + 1:]))
        elif calc.find('/') != -1:
            print(Rim(calc[:calc.find('/')]) / Rim(calc[calc.find('/') + 1:]))
        elif calc.find('//') != -1:
            print(Rim(calc[:calc.find('//')]) // Rim(calc[calc.find('//') + 1:]))
        elif calc.find('%') != -1:
            print(Rim(calc[:calc.find('%')]) % Rim(calc[calc.find('%') + 1:]))
        elif calc.find('**') != -1:
            print(Rim(calc[:calc.find('**')]) ** Rim(calc[calc.find('**') + 1:]))
        elif calc.find('<') != -1:
            print(Rim(calc[:calc.find('<')]) < Rim(calc[calc.find('<') + 1:]))
        elif calc.find('<=') != -1:
            print(Rim(calc[:calc.find('<=')]) <= Rim(calc[calc.find('<=') + 1:]))
        elif calc.find('==') != -1:
            print(Rim(calc[:calc.find('==')]) == Rim(calc[calc.find('==') + 1:]))
        elif calc.find('>') != -1:
            print(Rim(calc[:calc.find('>')]) > Rim(calc[calc.find('>') + 1:]))
        elif calc.find('>=') != -1:
            print(Rim(calc[:calc.find('>=')]) >= Rim(calc[calc.find('>=') + 1:]))

    elif int(menu) == 3:
        break

