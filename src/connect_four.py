# import random // for bot

ROWS = 6
COLS = 7

game_board = [["O", "O", "O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O", "O", "O"],]

players = {}


def give_players():
    for player in players:
        print(f"Player on turn: {player} with {players[player]}")


def add_player(name, color):
    players.__setitem__(name, color)


def ask_players():
    for i in range(2):
        name = input(f"Give the name of the {i + 1} player: ")
        while True:
            color = input("Give the color for the player (red or yellow): ")
            if color.lower() == "yellow" or color.lower() == "red":
                if len(players) == 0 or color.lower() != next(iter(players.values())):
                    break
                else:
                    print("Color has been chosen already, pick again.")
            else:
                print("Wrong input, pick again.")
        add_player(name, color)
       
       
def print_game_board():
    print("      A     B     C     D     E     F     G")
    for i in range(ROWS):
        print("")
        print(f"{i + 1}  |", end="")
        for c in range(COLS):
            print(f"  {game_board[i][c]}  |", end="")
            

def check_for_winner(color):
    # horizontal
    for y in range(ROWS):
        for x in range(COLS - 3):
            if game_board[y][x] == color and game_board[y][x + 1] == color and game_board[y][x + 2] == color and game_board[y][x + 3] == color:
                print(f"Game over. {color} wins!")
                return True
    # vertical
    for y in range(ROWS - 3):
        for x in range(COLS):
            if game_board[y][x] == color and game_board[y + 1][x] == color and game_board[y + 2][x] == color and game_board[y + 3][x] == color:
                print(f"Game over. {color} wins!")
                return True
    # diagonal 1 (top left to bottom right)
    for y in range(ROWS - 3):
        for x in range(COLS - 3):
            if game_board[y][x] == color and game_board[y + 1][x + 1] == color and game_board[y + 2][x + 2] == color and game_board[y + 3][x + 3] == color:
                print(f"Game over. {color} wins!")
                return True
    # diagonal 2
    for y in range(ROWS - 3):
        for x in range(3, COLS):
            if game_board[y][x] == color and game_board[y - 1][x + 1] == color and game_board[y - 2][x + 2] == color and game_board[y - 3][x + 3] == color:
                print(f"Game over. {color} wins!")
                return True
    return False


def parse_coordinate(coordinate_given):
    coordinate = [None] * 2
    if coordinate_given[0] == "A":
        coordinate[1] = 0
    elif coordinate_given[0] == "B":
        coordinate[1] = 1
    elif coordinate_given[0] == "C":
        coordinate[1] = 2
    elif coordinate_given[0] == "D":
        coordinate[1] = 3
    elif coordinate_given[0] == "E":
        coordinate[1] = 4
    elif coordinate_given[0] == "F":
        coordinate[1] = 5
    elif coordinate_given[0] == "G":
        coordinate[1] = 6
    else:
        print("invalid")
    if int(coordinate_given[1]) <= COLS and int(coordinate_given[1]) > 0:
        coordinate[0] = int(coordinate_given[1]) - 1
    else:
        print("invalid")
    return coordinate


def is_place_available(coordinate):
    if game_board[coordinate[0]][coordinate[1]] == "O":
        return True
    else:
        return False


def check_gravity(coordinate):
    if coordinate[0] == ROWS - 1:
        return True
    else:
        for x in range(ROWS - 1):
            if is_place_available(coordinate[x + 1]):
                return False
            else:
                return True


def ask_coordinate(player):
    print(f"Player on turn: {player} with {players[player]}")
    coordinate = input("Give the coordinates \
where you would like to put your disk: ")
    return coordinate


def validate_coordinate(coordinate):
    if check_gravity(coordinate) is True and is_place_available(coordinate) is True:
        return True
    else:
        return False


def place_disk(coordinate, color):
    if color == "yellow":
        game_board[coordinate[0]][coordinate[1]] = "y"
    else:
        game_board[coordinate[0]][coordinate[1]] = "r"


def main():
    bot = input("Would you like to play a bot? (yes or no) ")
    if bot == "no":
        ask_players()
        winner = False
        while winner is False:
            for player in players:
                print("")
                print_game_board()
                print("\n\n")
                while True:
                    coordinate_given = ask_coordinate(player)
                    coordinate = parse_coordinate(coordinate_given)
                    if validate_coordinate:
                        place_disk(coordinate, players[player])
                        winner = check_for_winner(players[player])
                        break
                    else:
                        print("invalid position, try again")
        print_game_board()
    else:
        print_game_board()
        print()
        coordinate = parse_coordinate("D4")
        print(coordinate)
        if coordinate[0] is not None:
            print(is_place_available(coordinate))


if __name__ == "__main__":
    main()