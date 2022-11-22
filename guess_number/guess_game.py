import random
from menu.menu_select import read_int, header


def guess_play():
    header('Bem vindo ao jogo de adivinhação')

    secret_number = random.randrange(1, 101)
    total_try = 0
    turn = 1
    points = 1000

    print('Escolha uma dificuldade')
    print('(1) Fácil (2) Médio (3) Difícil')
    level = read_int('Defina a dificuldade: ')
    match level:
        case 1:  # seleção de nível
            total_try = 20
        case 2:
            total_try = 10
        case _:
            total_try = 5

    while turn <= total_try:
        print(f'Tentativas {turn} de {total_try}')
        print()
        guess = read_int('Digite o seu palpite entre 1 e 100: ')  # capturando palpite do usuário

        if 1 <= guess <= 100:  # checando se o palpite está dentro do escopo do random
            if secret_number == guess:  # sistema de acerto
                print(f'Você acertou e fez {points} pontos')
                break
            else:
                if guess > secret_number:  # checando se o palpite está maior ou menor que o número secreto
                    print()
                    print(f'{guess} é maior que o número secreto')
                    print()
                elif guess < secret_number:
                    print()
                    print(f'{guess} é menor que o número secreto')
                    print()
                losed_points = abs(
                    secret_number - guess)  # sistema de pontuação absoluto por questão de possiveis negativos
                points = points - losed_points

            turn += 1  # incrementando o contador
            continue

        print('Você deve digitar um número entre 1 e 100!!')

    print()
    print(f'Fim de jogo, o número secreto era: {secret_number}')


if __name__ == '__main__':
    guess_play()
