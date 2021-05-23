"""Main module. Console game Tic Tac Toe"""


PLAYER_1 = ''
PLAYER_2 = ''
field_cells = list(range(10))


def draw_field(field):
    """Here will be a docstring"""
    print("-------------")
    for i in range(3):
        print("|", field[i * 3 + 1], "|",
              field[i * 3 + 2], "|",
              field[i * 3 + 3], "|")
        print("-------------")


def input_player_names():
    """Here will be a docstring"""
    global PLAYER_1, PLAYER_2
    PLAYER_1 = input("Please, enter name first user: ")
    PLAYER_2 = input("Please, enter name second user: ")


def show_menu():
    """Here will be a docstring"""
    menu_choice = 0
    while menu_choice == 0:

        print("Enter number:\n"
              "1 - Start game\n"
              "2 - Change name user\n"
              "3 - View game history\n"
              "4 - Exit")
        menu_choice = input("Please, enter your choice: ")
        if menu_choice == "1":
            input_player_names()
            play_game()
        elif menu_choice == "2":
            input_player_names()
        elif menu_choice == "3":
            pass
        elif menu_choice == "4":
            menu_choice = 4
            print('You have exit the game')
        else:
            print("Please enter number from menu")


def check_win(field):
    """Here will be a docstring"""
    win_sets = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for i in win_sets:
        if field[i[0]] == field[i[1]] == field[i[2]] == 'X':
            return PLAYER_1
        if field[i[0]] == field[i[1]] == field[i[2]] == '0':
            return PLAYER_2
    return False


def take_player_input(player_symbol, player_name):
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


def play_game():
    """Here will be a docstring"""
    print(f"Player 1: {PLAYER_1} plays with 'X'\n"
          f"Player 2: {PLAYER_2} plays with '0'")
    draw_field(field_cells)
    counter = 0
    win = False
    while not win:
        winner_player = check_win(field_cells)
        if winner_player:
            # не понимаю, как поменять перменную win, чтобы прервать цикл?
            win = True
            print(f"Winner is {winner_player}")
            break
        if counter == 9:
            print("The game is a draw! Nobody won")
            break
        if not counter % 2:
            take_player_input('X', PLAYER_1)
        else:
            take_player_input('0', PLAYER_2)
        counter += 1
        draw_field(field_cells)

    # нужно еще додумать с рестартом игры, сейчас выбор не влияет на рестарт (из-за цикла While?)
    # restart = input('Do yot want to play again? Enter y/n: ')
    # if restart == 'y' or 'Y':
    #     play_game()
    # elif restart == 'n':
    #     show_menu()


if __name__ == "__main__":
    print("\nWelcome to the game of Tic-Tac-Toe!\n")
    show_menu()
