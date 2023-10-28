while True :
        b = int(input('first num: '))
        c = input('operator: ')
        d = int(input('second num: '))
        if c == '+':
            print(b + d)
        elif c == '-':
            print(b - d)
        elif c == '*':
            print(b * d)
        elif c == '/':
            print(b / d)
        q = input('do you want to continue?: ')
        if q == 'y':
            continue
        else:
            break
