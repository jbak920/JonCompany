from game_state import GameState

game_state = GameState()

game_state.manager_of_shipping._treasury = 100

print("You are the Manager of Shipping.")
print()
print(f"There are {game_state.board.map._e._num_company_ships} ships in the East")
print(f"There are {game_state.board.map._w._num_company_ships} ships in the West")
print(f"There are {game_state.board.map._s._num_company_ships} ships in the South")
print(f"There are {game_state.board.map._c._num_company_ships} ships in China")
print(f"You have {game_state.manager_of_shipping._treasury} pounds in your treasury.")
print()

while(True):
    fit = input("Would you like to fit a ship? ")
    if fit not in ["yes", "y"]:
        print("Goodbye")
        exit()
    if game_state.manager_of_shipping._treasury < 5:
        print("You're out of money!")
        print("Goodbye")
        exit()

    zone = input("Where would you like to place it? ")
    game_state.add_company_ship_to_sea_zone(zone)

    print(f"There are {game_state.board.map._e._num_company_ships} ships in the East")
    print(f"There are {game_state.board.map._w._num_company_ships} ships in the West")
    print(f"There are {game_state.board.map._s._num_company_ships} ships in the South")
    print(f"There are {game_state.board.map._c._num_company_ships} ships in China")
    print(f"You have {game_state.manager_of_shipping._treasury} pounds in your treasury.")
    print()