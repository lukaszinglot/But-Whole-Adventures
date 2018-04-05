from random import randint
import os
import functions
import time
import mini_game
import highscore

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


def create_board(filename="mapa.txt"):
    with open(filename,"r") as mapa:
        the_map_list = []
        for line in mapa.readlines():
            list_of_chars = []

            for char in line:
                if char != "\n":
                    list_of_chars.append(char)
            the_map_list.append(list_of_chars)

    return the_map_list

def print_board(board):
    for row in board:
        for char in row:
            if char == "♥":
                char = Colour.RED + "♥" + Colour.END
            print(char, end='')
        print()

def wsad(board, char, x_pos, y_pos):
    board[x_pos][y_pos] = " "
    movable_items = [" ","💩","♥","💣","#","*","$"]
    if char == 'd' and  board[x_pos][y_pos +1] in movable_items:
        y_pos += 1
    elif char == 'a' and board[x_pos][y_pos - 1] in movable_items:
        y_pos -= 1
    elif char == 'w' and board[x_pos - 1][y_pos] in movable_items:
        x_pos -= 1
    elif char == 's' and board[x_pos + 1][y_pos] in movable_items:
        x_pos += 1
    elif char == "p":
        exit()
    return board, x_pos, y_pos



def insert_player(board, x_pos, y_pos,player):
    board[x_pos][y_pos] = player
    return board

def level(player,inv,board_name,file_name,inv_X,inv_Y,ret_X,ret_Y):
    life = 100
    char = ""
    x_pos = 1
    y_pos = 1
    board = create_board(board_name)
    functions.delay_print(file_name)
    time.sleep(15)
    os.system('clear')
    functions.delay_print("click_to_start.txt")
    while char!= "p":
        if board[ret_X][ret_Y] == player:
            os.system('clear')
            return

        if life <= 0:
            os.system('clear')
            functions.delay_print("koniec_gry.txt")
            exit()

        char = functions.getch()
        board,x_pos, y_pos = wsad(board,char, x_pos, y_pos)
        life,inv = functions.interaction_with_items(life,inv,board,x_pos,y_pos)

        board_with_player = insert_player(board, x_pos, y_pos,player)
        board = functions.print_inventory(board,inv,life,inv_X,inv_Y)
        os.system('clear')
        print_board(board_with_player)


def level_1(player,inv):
    level(player,inv,"mapa.txt","Fabula.txt",1,51,16,43)


def level_2(player,inv):
    level(player,inv,"mapa3.txt","rozdzial2.txt",1,97,4,90)


def level_3(player,inv):
    level(player,inv,"mapa4.txt","rozdzial3.txt",1,80,21,68)


def level_4(player,inv):
    level(player,inv,"mapa5.txt","rozdzial4.txt",1,100,27,91)


def main():
    inv = {"kupa":50,"dupa":25}
    functions.delay_print("how_to_play.txt")
    time.sleep(20)
    os.system('clear')
    functions.delay_print("wybor_postaci.txt")
    player = functions.character_creation()
    os.system("clear")
    level_1(player,inv)
    mini_game.rock_paper_scissors()
    level_2(player,inv)
    mini_game.rock_paper_scissors()
    level_3(player,inv)
    mini_game.rock_paper_scissors()
    level_4(player,inv)
    mini_game.random_number()
    functions.delay_print("rozdzial5.txt")
    time.sleep(14)
    os.system('clear')
    functions.delay_print("About_screen.txt")

    highscore.save_file(highscore.add_new_highscore(inv))
    highscore.print_highscore(highscore.read_file())


if __name__=="__main__":
    main()
