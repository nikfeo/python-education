"""Console game Tic Tac Toe"""

import sys
import logging

logging.basicConfig(filename='XO_game_log.txt',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)

# ===================================================================================
# HELP FUNCTIONS


def draw_field(field_cells):
    """Here will be a docstring"""
    print("-------------")
    for i in range(3):
        print("|", field_cells[i * 3 + 1], "|",
              field_cells[i * 3 + 2], "|",
              field_cells[i * 3 + 3], "|")
        print("-------------")


def input_player_names():
    """Here will be a docstring"""
    player_1 = input("Please, enter name first user: ")
    player_2 = input("Please, enter name second user: ")
    player_sign = {"X": player_1, "0": player_2}
    return player_1, player_2, player_sign


def check_win(field_cells):
    """Here will be a docstring"""
    win_sets = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for i in win_sets:
        if field_cells[i[0]] == field_cells[i[1]] == field_cells[i[2]]:
            return field_cells[i[0]]
    return False


def take_player_input(player_symbol, player_name, field_cells):
    """Here will be a docstring"""
    valid = False
    while not valid:
        player_input = input(f"{player_name} your turn! Enter number of free cell: ")
        try:
            player_input = int(player_input)
        except ValueError:
            print("Enter a number from 1 to 9")
            continue
        if player_input in range(1, 10):
            if str(field_cells[player_input]) not in "X0":
                field_cells[player_input] = player_symbol
                valid = True
            else:
                print("This cell is already taken")
        else:
            print("Enter a number from 1 to 9")


# ===================================================================================
# LOGGING FUNCTIONS

def write_to_file(winner, finish_game, player_sign):
    """Here will be a docstring"""
    if winner:
        logging.info(f"Winner: {player_sign[finish_game]}")
    else:
        logging.info("Game finished with DRAW")


def view_prev_games(filename):
    """Here will be a docstring"""
    with open(filename, "r") as file:
        previous_games = file.read()
    if len(previous_games) == 0:
        print("File is empty")
    else:
        print(previous_games)


# ===================================================================================
# MAIN FUNCTIONS

def play_game(player_1, player_2, player_sign, player_score):
    """Here will be a docstring"""
    print(f"Player 1: {player_1} plays with 'X'\n"
          f"Player 2: {player_2} plays with '0'")
    field_cells = list(range(10))
    draw_field(field_cells)
    counter = 0
    winner = True

    while True:
        if counter == 9:
            print("The game is a draw! Nobody won")
            winner = False
            break
        if counter >= 5:
            finished_game = check_win(field_cells)
            if finished_game:
                print(f"Winner {player_sign[finished_game]}")
                break
        if not counter % 2:
            take_player_input('X', player_1, field_cells)
        else:
            take_player_input('0', player_2, field_cells)
        counter += 1
        draw_field(field_cells)

    write_to_file(winner, finished_game, player_sign)
    restart_game(player_1, player_2, finished_game, player_sign, player_score)


def restart_game(player1, player2, finished_game, player_sign, player_score):
    """Here will be a docstring"""
    while True:
        print("1 - Restart game")
        print("2 - Exit to menu")

        try:
            user_input = int(input("Please, enter your choice: "))
        except (ValueError, TypeError):
            print("Enter NUMBER, please.")
            continue
        else:
            if user_input == 1:
                if finished_game:
                    player_score[player_sign[finished_game]] += 1
                    for key, value in player_score.items():
                        print(f"Player {key} has {value} point(s)")
                        logging.info(f"Player {key} has {value} point(s)")
                play_game(player1, player2, player_sign, player_score)
            elif user_input == 2:
                show_menu()
            else:
                print("Enter a number from 1 to 2")


def show_menu():
    """Here will be a docstring"""
    player_1, player_2, player_sign = input_player_names()
    while True:

        print("Enter number:\n"
              "1 - Start new game\n"
              "2 - Change name user\n"
              "3 - View game history\n"
              "4 - Exit\n"
              "5 - Delete game history")
        menu_choice = input("Please, enter your choice: ")
        if menu_choice == "1":
            player_score = {player_1: 0, player_2: 0}
            finished_game = play_game(player_1, player_2, player_sign, player_score)
            restart_game(player_1, player_2, finished_game, player_sign, player_score)
        elif menu_choice == "2":
            player_1, player_2, player_score = input_player_names()
        elif menu_choice == "3":
            view_prev_games("XO_game_log.txt")
        elif menu_choice == "4":
            sys.exit('You have exit the game')
        elif menu_choice == "5":
            with open("history_game.txt", "r+") as file:
                file.truncate(0)
        else:
            print("Please enter number from menu")


# ===================================================================================

if __name__ == "__main__":
    print("\nWelcome to the game of Tic-Tac-Toe!\n")
    show_menu()
