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


def main(): 
    ask_players()
    give_players()


if __name__ == "__main__":
    main()