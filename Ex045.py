#Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time

#ESCOLHA DO PC
pc = random.randint(1, 3)

#Introdução
print('====== DHG Entertainment Studios ======')
print('\n=============== JOKENPÔ ===============')
print('\nEscolha uma OPÇÃO entre: '
      '\n(pedra, papel e tesoura)')

#ESCOLHA DO JOGADOR
jogador = (input('\nFAÇA SUA JOGADA: ')).upper()

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!\n')

#numero por palavra
if pc == 1:
    pc = 'PEDRA'
elif pc == 2:
    pc = 'TESOURA'
elif pc == 3:
    pc = 'PAPEL'

#REGRAS
if jogador == 'PEDRA' and pc == 'TESOURA' or jogador == 'TESOURA' and pc == 'PAPEL' or jogador == 'PAPEL' and pc == 'PEDRA':
    print('=' * 13)
    print(f'| JOGADOR | {jogador}' + "\n ----------------------------------         "
          f'\n|    PC   | {pc}')
    print('=' * 13)
    print('VOCÊ GANHOU!!')

elif pc == 'PEDRA' and jogador == 'TESOURA' or pc == 'TESOURA' and jogador == 'PAPEL' or pc == 'PAPEL' and jogador == 'PEDRA':
    print('=' * 13)
    print(f'| JOGADOR | {jogador}'
          f'\n|    PC   | {pc}')
    print('=' * 13)
    print('VOCÊ PERDEU!!')

elif jogador == pc:
    print('=' * 13)
    print(f'| JOGADOR | {jogador}'
          f'\n|    PC   | {pc}')
    print('=' * 13)
    print('EMPATE')

else:
    print('!OPÇÃO INVÁLIDA!'
          '\n!TENTE NOVAMENTE!')
