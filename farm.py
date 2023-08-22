import json
with open('garden_list.json', 'r') as file:
    plant_data = json.load(file)

class Player:
    def __init__(self):
        self.current_location = None

def move_to(location):
    if location == '1':
        player.current_location = "Cottage"
    elif location == '2':
        player.current_location = "Garden"
    elif location == '3':
        player.current_location = "Transcriber"


        
player = Player()

def describe_location():
    while True:
        user_input = input("Please select 1(Cottage), 2(Garden), 3(Transcriber), or quit: ")
        if user_input == 'quit':
            break
        elif user_input.isnumeric() and int(user_input) in [1, 2, 3]:
            move_to(user_input)
            print("You are now at:", player.current_location)
            perform_action()
        else:
            print('Unrecognized command')
            
garden_grid = [['empty' for _ in range(3)] for _ in range(3)]

def display_garden(grid):
    for row in grid:
        print(" | ".join(row))
    print("---------")
# Accessing and updating plant information
for plant in plant_data['plants']:
    name = plant['name']
    is_watered = plant['watered']
    quantity = plant['quantity']

    # You can update the watered status
    if not is_watered:
        # Do something, like watering the plant
        plant['watered'] = True

    # You can update the quantity
    if quantity > 0:
        # Do something, like harvesting the plant
        plant['quantity'] -= 1

# Save the updated data back to the JSON file
    with open('garden_list.json', 'w') as file:
        json.dump(plant_data, file, indent=4)
        
while True:
    display_garden(garden_grid)
    user_input = input("Enter the row and column (e.g., '1 2') to interact with a cell or 'exit' to quit: ")

    if user_input == 'exit':
        break

    row, col = map(int, user_input.split())
    cell_contents = garden_grid[row][col]
    if cell_contents == 'empty':
        print("This cell is empty.")
        elif cell_contents == 'Tomato':
            action = input("Water or harvest the tomato plant? ").lower()
    if action == 'water':
        # Handle watering the plant
        elif action == 'harvest':
        # Handle harvesting the plant
        else:
            print("Invalid action.")
else:
    print(f"This cell contains {cell_contents}.")

def perform_action():
    # farming sim
    if player.current_location == "Garden":
        display_garden(garden_grid)  # Pass the garden_grid to the display_garden function
        print("What do you want to do in the Garden?")
        while True:
             action = input("Options: plant, harvest, storage, or back: ")
            if action == "plant":
                print("You are planting in the Garden.")
            elif action == "harvest":
                print("You are harvesting in the Garden.")
            elif action == "storage":
                print("You are accessing storage in the Garden.")
            elif action == "back":
                break
            else:
                print("Invalid action. Try again.")
    #cooking sim
    elif player.current_location == "Cottage":
        print("What would you like to do in the Cottage?")
        while True:
            action = input("Options:  sleep, cook, weather, or back: ")
            if action == "sleep":
                print("You call it a night and go to bed.")
            elif action == "cook":
                print("You cook up some food.")
            elif action == "weather":
                print("You check the weather for the day.")
            elif action == "back":
                break
            else:
                print("Invalid action.  Try again.")
    #cloning sim
    elif player.current_location == "Transcriber":
        print("What would you like to work on?")
        while True:
            action = input("Transcribe: Machine, Plant, or Animal schematics?")
            if action == "machine":
                print("You build a new machine.")
            elif action == "plant":
                print("You clone a plant from Earth.")
            elif action == "animal":
                print("You clone an animal from Earth.")
            elif action == "back":
                break
            else:
                print("Invalid action.  Try again.")
# Start the game
describe_location()
