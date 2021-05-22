"""Main module. Console game Tic Tac Toe"""

player_1 = ''
player_2 = ''


def draw_field(field):
    """There will be a docstring"""
    print("-------------")
    for i in range(3):
        print("|", field[i*3 + 1], "|",
              field[i*3 + 2], "|",
              field[i*3 + 3], "|")
        print("-------------")


def input_player_names():
    """There will be a docstring"""
    global player_1, player_2
    player_1 = input("Please, enter name first user: ")
    player_2 = input("Please, enter name second user: ")


def show_menu():
    """There will be a docstring"""
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


def check_win(field_cells):
    """There will be a docstring"""
    win_sets = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for i in win_sets:
        if field_cells[i[0]] == field_cells[i[1]] == field_cells[i[2]] == 'X':
            return player_1
        elif field_cells[i[0]] == field_cells[i[1]] == field_cells[i[2]] == '0':
            return player_2
    return False


def play_game():
    """There will be a docstring"""
    print(f"Player 1: {player_1} plays with 'X'\n"
          f"Player 2: {player_2} plays with '0'")
    field_cells = list(range(10))
    draw_field(field_cells)
    counter = 0

    while True:
        winner_player = check_win(field_cells)
        if winner_player:
            print(f"Winner is {winner_player}")
            break
        if counter == 9:
            print("The game is a draw! Nobody won")
            break
        # нужно написать отдельную функцию для проверки ввода числа пользователем
        if not counter % 2:
            player1_turn = input(f"{player_1} your turn! Enter number of free cell: ")
            try:
                player1_turn = int(player1_turn)
                field_cells[player1_turn] = "X"
            except ValueError:
                print("enter a number from 1 to 9")
                continue
        else:
            player2_turn = input(f"{player_2} your turn! Enter number of free cell: ")
            try:
                player2_turn = int(player2_turn)
                field_cells[player2_turn] = "0"
            except ValueError:
                print("enter a number from 1 to 9")
                continue
        counter += 1
        draw_field(field_cells)

    # нужно еще додумать с рестартом игры, сейчас выбор не влияет на рестарт (из-за цикла While?)
    restart = input('Do yot want to play again? Enter y/n: ')
    if restart == 'y' or 'Y':
        play_game()
    elif restart == 'n':
        show_menu()


if __name__ == "__main__":
    print("\nWelcome to the game of Tic-Tac-Toe!\n")
    show_menu()
