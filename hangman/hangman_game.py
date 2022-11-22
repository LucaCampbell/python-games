import random
from menu.menu_select import header


def hangman_play():
    header('Bem vindo ao jogo de forca')
    secret_word = load_secret_word()

    got_letters = initalize_got_letters(secret_word)
    hanged = False
    got_it = False
    attemps = 0

    while not hanged and not got_it:  # loop checando se você acertou ou se enforcou

        guess = input('Qual letra? ').strip().upper()[0]
        guess = guess.strip().upper()  # tirando possiveis espaços de input e colocando em caixa alta

        if guess in secret_word:
            for i, letter in enumerate(secret_word):  # loop para checar se o palpite se encontra na palavra secreta
                if guess == letter:  # comparando letras
                    got_letters[i] = letter  # colocando as letras em suas posições

        else:
            attemps += 1
            draw_hanged(attemps)

        hanged = attemps == 6  # incrementando o contador para checar enforcamento
        got_it = '_' not in got_letters  # condição para parar o jogo e vencer
        print(got_letters)

    if got_it:
        winner_msg()
    else:
        lose_msg(secret_word)


def load_secret_word():
    file = open('palavras.txt', 'r')
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    rng = random.randrange(0, len(words))
    secret_word = words[rng].upper()
    return secret_word


def initalize_got_letters(word):
    return ['_' for letters in word]


def winner_msg():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def lose_msg(secret_word):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def draw_hanged(attemps):
    print("  _______     ")
    print(" |/      |    ")

    if (attemps == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (attemps == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (attemps == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (attemps == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (attemps == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (attemps == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (attemps == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print()


if __name__ == '__main__':
    hangman_play()
