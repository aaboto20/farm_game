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

def perform_action():
    #farming sim 
    if player.current_location == "Garden":
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
