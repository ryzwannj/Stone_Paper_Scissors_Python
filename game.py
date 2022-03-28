import random
from secrets import choice
from bcolor import bcolors

choices = {1: 'Pierre', 2: 'Feuille', 3: 'Ciseaux'}

your_score = 0
desktop_score = 0 

def menue():
    global random_choice
    random_choice = random.choice(list(choices))
    print('Selectionnez votre signe: ')
    for index, signe in choices.items():
        print(index, ':', signe)
    try:
        global your_choice 
        your_choice = int(input('Votre signe (le chiffre correspondant a votre signe): '))
        if your_choice > 3:
            print(f'{bcolors.WARNING}Entrez un signe valide (chiffre valide)!{bcolors.ENDC}')
            return False
        else:
            return True
        
    except ValueError:
        print(f'{bcolors.WARNING}Entrez un signe valide (chiffre valide)!{bcolors.ENDC}')
        menue()

def display_score():
    print(f'{bcolors.OKBLUE}Your Score: {bcolors.ENDC}', your_score)
    print(f'{bcolors.OKBLUE}Desktop Score: {bcolors.ENDC}', desktop_score)


running = True

while running:

    display_score()
    menue()

    if your_choice == random_choice:
        print(f'{bcolors.OKBLUE}Egalité{bcolors.ENDC}')

    if your_choice == 1 and random_choice == 2:
        print(f'{bcolors.WARNING}La FEUILLE vous a recouvert{bcolors.ENDC}')
        desktop_score += 1
    if your_choice == 1 and random_choice == 3:
        print(f"{bcolors.OKGREEN}Vous avez casser les CISEAUX de l'adversaire{bcolors.ENDC}")
        your_score += 1


    if your_choice == 2 and random_choice == 1:
        print(f"{bcolors.OKGREEN}Vous avez recouvert la PIERRE{bcolors.ENDC}")
        your_score +=1
    if your_choice == 2 and random_choice == 3:
        print(f"{bcolors.WARNING}Vous avez etait couper par les CISEAUX de l'adversaire!{bcolors.ENDC}")
        desktop_score +=1
    
    if your_choice == 3 and random_choice == 2:
        print(f'{bcolors.OKGREEN}Vous avez couper la FEUILLE{bcolors.ENDC}')
        your_score += 1
    if your_choice == 3 and random_choice == 1:
        print(f"{bcolors.WARNING}La PIERRE de l'adversaire vous a ecrasez!{bcolors.ENDC}")
        desktop_score += 1

    if your_score == 10 and desktop_score < your_score:
        print(f'{bcolors.OKGREEN}{bcolors.BOLD}Vous avez GAGNE!!{bcolors.ENDC}')
        display_score()
        break
    
    if desktop_score == 10 and your_score < desktop_score:
        print(f'{bcolors.WARNING}{bcolors.BOLD}Vous avez PERDU!!{bcolors.ENDC}')
        display_score
        break