# import from player file
from player import load_player, save_player

# Main game loop
def main():
    player = load_player()
    print("fWelcome, adventurer! You have ${player['coins']}")

    # Infinite loop, perfect to keep going until player quits
    while True:
        command = input("\nWhat would you like to do?\n" \
        " > balance\n" \
        " > quit\n")

        if command == "quit":
            save_player(player)
            print("Game saved. Goodbye, adventerer.")
            break
        elif command == "balance":
            print(f"You have ${player['coins']}")
        else:
            print("Please enter a valid command.")

# Run only when directly on this file
if __name__ == "__main__":
    main()