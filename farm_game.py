def player():
    player_data = {
        "current_location": is_a_number,
        "inventory": [],
        "stat_points": {
            "cooking": "amateur",
            "harvesting": "beginner",
            "sewing": "beginner"
        },
        "equipment": {
            "tool": "hoe",
            "shirt": "cotton shirt",
            "pants": "jeans"
        }
    }
    pants = player_data["equipment"]["pants"]
    return pants

# Call the player function and print the result
"""print(player())"""
def is_a_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def describe_location():
    while True:
        user_input = input("Please select 1, 2, 3, or quit: ")

        if user_input == 'quit':
            break
        elif is_a_number(user_input) and int(user_input) in [1, 2, 3]:
            move_to(user_input)
            print(player.current_location)
        else:
            print('Unrecognized command')

describe_location()

    
"""def farmland(acres):
    acres = 1

# Define the House
def home():{
    "kitchen": {
        "description": "You are in the kitchen.",
        "connected_rooms": ["living room"],
        "items": ["knife"]
    },
    "living room": {
        "description": "You are in the living room.",
        "connected_rooms": ["kitchen", "bedroom"],
        "items": ["television"]
    },
    "bedroom": {
        "description": "You are in the bedroom.",
        "connected_rooms": ["living room"],
        "items": ["bed", "lamp"]
    }
}

# Define the Player
def player():{
    "current_room": "living room",
    "inventory": []
}

# Main Game Loop
while True:
    # Print Player Location and Room Description
    current_room = home[player["current_room"]]
    print(current_room["description"])
    
    # Print Available Actions
    print("Available Actions:")
    print("1. Move to a different room")
    print("2. Examine the current room")
    print("3. Pick up an item")
    
    # Get Player Input
    choice = input("Enter your choice: ")
    
    # Process Player Input
    if choice == "1":
        # Move to a different room
        destination = raw_input("Enter the name of the room you want to move to: ")
        if destination in current_room["connected_rooms"]:
            player["current_room"] = destination
        else:
            print("You can't move to that room.")
    elif choice == "2":
        # Examine the current room
        items = current_room["items"]
        if len(items) > 0:
            print("You see the following items in the room:")
            for item in items:
                print("- " + item)
        else:
            print("There are no items in the room.")
    elif choice == "3":
        # Pick up an item
        items = current_room["items"]
        if len(items) > 0:
            print("You pick up the following item(s):")
            for item in items:
                player["inventory"].append(item)
                print("- " + item)
            current_room["items"] = []
        else:
            print("There are no items to pick up in the room.")
    else:
        print("Invalid choice. Please try again.")
home()

"""