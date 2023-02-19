import random

import keyboard


def cards_choice():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
    player_cards = (random.choice(cards), random.choice(cards))
    while player_cards[0] == player_cards[1]:
        player_cards = (random.choice(cards), random.choice(cards))


def data_save(animals):
    file = open('Player_data.txt', 'r+')
    for i in animals:
        for j in i:
            file.write(j)
            file.write(',')
        file.write(' ')
    file.close()


def data_load():
    animals = open('Player_data.txt', 'r')
    an = animals.read()
    animals.close()
    print(an)
    return an


def data_sort(animals):
    animals_ = animals.split(' ')
    return animals_


def doing_is(animals):
    print("make new animal = click {m}', add feature to animal = click {a}, see your animals = click {w}: ")
    animals_sorted = animals.split(' ')
    print(animals_sorted)
    while True:
        try:
            if keyboard.is_pressed('s'):
                data_save(animals)
                break
            elif keyboard.is_pressed('l'):
                animals = data_sort(data_load())
            elif keyboard.is_pressed('m'):
                name = [input("Name of animal: ")]
                animals.append(name)
                return animals
            elif keyboard.is_pressed('a'):
                name = input('Name of animal: ')
                feature = int(input(f'predator + 1 - 1, camouflage - 2, fast - 3, ink cloud - 4, big + 1- 5, '
                                    f'Waterfowl - 6, Fat reserve - 7, Flight - 8, sleep - 9, Intelligence + 1 - 10: '))
                
            elif keyboard.is_pressed('w'):
                print(animals)
        except:
            print('Error')


def do_doing(doing, animals):
    if doing[:2] == 'mk ':
        animals.append(doing[2:])
        return animals
    elif doing[:2] == 'sa ':
        print(animals)
        return animals


def main():
    animals = data_load()
    while True:
        animals = (doing_is(animals))
        print(animals)


main()
