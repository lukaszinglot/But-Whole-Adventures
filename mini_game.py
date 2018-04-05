import os
import random

class Colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def rock_paper_scissors():

    player_moves = ["KAMIEN", "PAPIER", "NOZYCE"]
    computer_moves = player_moves[random.randint(0,2)]
    player = False
    while player == False:
    #set player to False
        player = input("KAMIEN, PAPIER, NOZYCE?").upper()
        os.system('clear')
        if player in player_moves:
            if player == computer_moves:
                print("REMIS!")
                print("JESZCZE RAZ")
                player = False
                computer_moves = player_moves[random.randint(0,2)]
            elif player == "KAMIEN":
                if computer_moves == "PAPIER":
                    print("PRZEGRALES!", computer_moves, "ZAKRYWA", player)
                    print("JESZCZE RAZ")
                    player = False
                    computer_moves = player_moves[random.randint(0,2)]
                else:
                    print("WYGRALES!", player, "MIAZDZY", computer_moves)
            elif player == "PAPIER":
                if computer_moves == "NOZYCE":
                    print("PRZEGRALES!", computer_moves, "TNIE", player)
                    print("JESZCZE RAZ")
                    player = False
                    computer_moves = player_moves[random.randint(0,2)]
                else:
                    print("WYGRALES!", player, "ZAKRYWA", computer_moves)
            elif player == "NOZYCE":
                if computer_moves == "KAMIEN":
                    print("PRZEGRALES...", computer_moves, "MIAZDZY", player)
                    print("JESZCZE RAZ")
                    player = False
                    computer_moves = player_moves[random.randint(0,2)]
                else:
                    print("WYGRALES!", player, "TNIE", computer_moves)
            else:
                print("NO CHYBA NIE!")
                player = False
                computer_moves = player_moves[randint(0,2)]
        else:
            print("NO CHYBA NIE !")
            player = False
    return


def random_number():
    tries = 10
    number_random = str(random.randint(100,999))
    print(number_random)
    print('\n')
    print('''                                             ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `
                -,-..\  _  \  `  /  ,  / `._) _,-\`
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \  V   V, /`     /
    ,--\(        ,     <_/`\      ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```
   ''')
    print("Myślę o 3 cyfrowej liczbie. Zgadnij co to za liczba!")
    i = 1


    while i<= tries:

        number_try = input("\n" + "Zgadnij " + str(i) + " : " + "\n")


        if len(number_try) != 3 or not number_try.isdigit():
            print("Podaj 3 cyfrową liczbę:")
        elif number_try == number_random:
            print("GORĄCO GORĄCO GORĄCO")
            print("Udało się!")
            return
        else:
            i += 1
            iterator = 0
            guessed_numb = 0
            for element in number_try:
                if element in number_random:
                    if element == number_random[iterator]:
                        print(Colour.RED + "Gorąco" + Colour.END, end = ' ')
                    else:
                        print("Ciepło", end = ' ')
                    guessed_numb += 1
                iterator += 1
            if guessed_numb == 0:
                print(Colour.BLUE + 'Zimno' + Colour.END)
    print('Koniec gry')
