from time import sleep
from guess_number.guess_game import guess_play
from hangman.hangman_game import hangman_play
from tic_tac_toe.tic_tac_game import tic_tac_play
from menu.menu_select import *


while True:
    game = menu(['Jogo da Forca', 'Jogo da Adivinhação', 'Jogo da Velha', 'Sair do Sistema'])
    match game:
        case 1:
            print('Jogando Forca')
            hangman_play()
        case 2:
            print('Jogo da adivinhação')
            guess_play()
        case 3:
            print('Jogo da Velha')
            tic_tac_play()
        case 4:
            header('Saindo do Sistema até Logo')
            break
        case _:
            print('ERRO, digite uma opção válida')
    sleep(1)