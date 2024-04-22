players = []


class Player:
    name = ""
    color = ""

    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
     
    def __str__(self) -> str:
        return self.name
    
    def get_color(self):
        return self.color


def add_player(name, color):
    players.append(Player(name, color))
   

def ask_players():
    for i in range(2):
        name = input(f"Give the name of the {i + 1} player: ")
        while True:
            color = input("Give the color for the player (red or yellow): ")
            if color.lower() == "yellow" or color.lower() == "red":
                if len(players) == 0 or color.lower() != players[0].color:
                    break
                else:
                    print("Color has been chosen already, pick again.")
            else:
                print("Wrong input, pick again.")
        players.append(Player(name, color))
    return players


def main(): 
    ask_players()


if __name__ == "__main__":
    main()