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