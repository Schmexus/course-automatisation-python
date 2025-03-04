while True:
    primer = input('Введите через пробел число, действие, число: ').split()
    if primer[0] == 'СТОП':
        break
    try:
        number_1= float(primer[0])
        number_2=float(primer[2])
    except:
        print('Вы ввели не числа, либо ввели не через пробел, попробуйте снова')
        continue
    match primer[1]:
        case '+':
            result = number_1 + number_2
            print(f'{primer[0]} + {primer[2]} = {str(result)}')
        case '-':
            result = number_1-number_2
            print(f'{primer[0]} - {primer[2]} = {str(result)}')
        case '/':
            if number_2 == 0:
                print('на 0 делить нельзя. Пробуй снова')
                continue
            result = number_1/number_2
            print(f'{primer[0]} / {primer[2]} = {str(result)}')
        case '*':
            result = number_1 * number_2
            print(f'{primer[0]} * {primer[2]} = {str(result)}')
    print('Введите "СТОП" для выхода')