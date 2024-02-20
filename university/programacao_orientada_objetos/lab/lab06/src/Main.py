'''
This class is the main class of the "World of Zuul" application.
@author  Admilson Ribeiro
@version 2008.03.30
'''
from Game import Game


class Main:
    game = Game()
    game.play()


'''
O que esta aplicação faz?
    r: roda um jogo de salas por linhas de comando
Que comando o jogo aceita?
    r: go <direção>, quit, help
O que cada comando faz?
    r: go <direção> anda para a sala na direção desejada se houver uma porta,
    quit sai do jogo e help mostra os comando e como funciona o game
Quantas salas estão no cenario?
    r: 5
Desenhe um mapa das salas exitentes.

                        bicen
                         /
    pub -- outside -- theatre
     /        |
   resun     lab -- office
'''
