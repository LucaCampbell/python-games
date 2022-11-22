def read_int(msg):
    while True:
        try:
            userinput = int(input(msg))
        except ValueError:
            print("Não é um inteiro!")
            continue
        else:
            c = userinput
            return c


def header(txt):
    print(lines())
    print(txt.center(42))
    print(lines())


def lines(tam=42):
    return '-' * tam


def menu(lista):
    header('ESCOLHA UM JOGO')
    for i, item in enumerate(lista):
        print(f'{i + 1} - {item}')
    print(lines())
    option = read_int('Sua Opção: ')
    print(lines())
    return option
