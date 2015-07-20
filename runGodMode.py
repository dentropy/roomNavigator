game_data = []
exit = False
from RunRoomNavigatorClass import RunRoomNavigator
from GodModeFunctions import GodModeClass
# RUN THE REAL PROGRAM 
god_mode_functions = GodModeClass()   
instructions_text = '''
Here are a list of commands you can use when 'use command:' shows up
import - imports a past rooms from the name of the text file in 
    the same folder
run - remember to import run the room simulation /exit is too exit
    type exit to return to 'use command'
create room - run through the instructions in order to create a new room
help - print the instructions you are reading
list all rooms - lists the names of all the rooms
print game data - prints the data structure
save the data - saves the current data structure into a text document
delete room - delete room and connections to it
''' 
print instructions_text
while exit != True:
    input = raw_input('use command:')
    print_what = True
    if input == "import":
        run_Room_Navigator = RunRoomNavigator()
        game_data = run_Room_Navigator.import_rooms()
        print_what = False
    if input == "run":
        run_Room_Navigator = RunRoomNavigator()
        game_data = run_Room_Navigator.run(game_data)
        print_what = False
    if input == 'help':
        print instructions_text
        print_what = False
    if input == "create room":
        game_data = god_mode_functions.create_room(game_data["rooms"])
        print_what = False
    if input == "list all rooms":
        for i in game_data["rooms"]:
            print i
        print_what = False
    if input == "print game data":
        print game_data["rooms"]
        print_what = False
    if input == "save the data":
        run_Room_Navigator = RunRoomNavigator()
        run_Room_Navigator.save_the_data(game_data)
        print_what = False
    if input == "delete room":
        game_data["rooms"] = god_mode_functions.del_room(game_data)
        print game_data
        print_what = False  
    #input new commands above this comment
    if print_what == True:
        print "command does not exist try again"
# DONE RUNING THE REAL PROGRAM    
