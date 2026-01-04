import json

# Player creation, with starting values
def create_player():
    # Player data
    player = {
        "coins": 0,
        # Change fron list to dict bc easier to access with item name as key
        "inventory": {},
        "task_cooldown": 0,
    }

    return player

# Save player data to JSON file to save across sessions
def save_player(player):
    # Create/open player data file in write mode, dump Pytthon data to JSON
    with open("player_data.json", "w") as file:
        json.dump(player, file, indent = 4)

# Pull player data from JSON if existing, create if not (one player only)
def load_player():
    # try/catch error handing with specific error
    try:
        with open("player_data.json", "r") as file:
            player = json.load(file)
            return player
    
    # Create new player if file not found
    except FileNotFoundError:
        print("No existing save file. New adventurer!")
        player = create_player()
        save_player(player)
        return player