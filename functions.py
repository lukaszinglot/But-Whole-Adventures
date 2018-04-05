import sys
import time
import os
import termios
import tty
import random



def delay_print(file_name ="Fabula.txt"):
    '''
    Function to show our story letter by letter
    '''
    with open(file_name) as story:
        for line in story:
            for char in line:
                sys.stdout.write("{}".format(char))
                sys.stdout.flush()
                time.sleep(0.0001)


def getch():
    '''
    Making step without pressing Enter
    '''
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def character_creation():
    '''
    Hero creator Function
    '''
    creation = False
    player = "@"
    while creation == False:
        player_choose = getch()
        player_choose.isdigit()
        if player_choose == '1':
            player = "🚶"
            break
        elif player_choose == '2':
            player = "🎩"
            break
        elif player_choose == '3':
            player = "👳"
            break
        elif player_choose == '4':
            player = "🕵️"
            break
        else:
            creation = False

    return player

def interaction_with_items(live,inventory,board,x_pos,y_pos):
    '''
    Function to interact with items, which we put in game_over
    It gives item, or item values
    '''
    if board[x_pos][y_pos] == "💩":
        if "poo" in inventory:
            inventory["poo"] += 1
        else:
            inventory["poo"] = 1
        live -= 7
    elif board[x_pos][y_pos] == "♥":
        live = 100
    elif board[x_pos][y_pos] == "💣":
        if "money" in inventory:
            inventory["money"] += 5
        else:
            inventory["money"] = 5
    elif board[x_pos][y_pos] == "*":
        if "star" in inventory:
            inventory["star"] += 10
        else:
            inventory["star"] = 10
    return live, inventory

def print_inventory(board,inventory,live,X,Y):
    '''
    Function that show our inventory on-screen
    '''
    if "money" in inventory:
        board [X][Y] = inventory["money"]
    if "poo" in inventory:
        board [X+1][Y] = inventory["poo"]
    if "star" in inventory:
        board [X+2][Y]= inventory["star"]
    board[X+3][Y] = live

    return board
