##################
# test szczęścia #
##################

import random

runda = 0

#funkcja do tego żeby można było podać swoją odpowiedź
def podajLiczbe():
    podaj_liczbe = int(input('podaj liczbe: '))

    if podaj_liczbe > 100:
        print('za duża liczba')
    elif podaj_liczbe < 0:
        print('za mała liczba')

x = 'y'

#petla
while x == 'y':
    liczba = random.randint(1, 100)

#poprawna odpowieć wylosowana przez program
    def poprawnaLiczba():
        print('poprawna liczba to ', liczba)
    podajLiczbe()

#komunikaty trafienia i nie trafienia poprawnej odpowiedzi
    if podajLiczbe == liczba:
        print('BRAWO!!! trafiłeś')
        poprawnaLiczba()
        print('\n wylosowałeś poprawną liczbę w prubir ', runda, '\n')
    else:
        print('nie trafiłeś')
        poprawnaLiczba()
        runda += 1
        print('\n aktualna pruba to ', runda, '\n')
#pytanie czy chce sie sprubować jeszcze raz
    x = input('jezeli chcesz sprubować jeszcze raz napisz y a jeżeli nie to napisz n: ')
    print('\n')
