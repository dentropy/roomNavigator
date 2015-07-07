from RunRoomNavigatorClass import RunRoomNavigator
game_data = []
exit = False

#SAVING THE DATA STRUCTURE
def save_the_data(game_data):
    if game_data == []:
        print "DID NOT IMPORT GAME DATA TYPE 'import'"
        return
    json_string = json.dumps(game_data)
    name_of_file = raw_input("name the file you wish to save to:")
    txt_file = open(name_of_file + ".json", 'w+')
    txt_file.write(json_string)
    txt_file.close()
# SAVING THE DATA STRUCTURE



import json
import os.path
def import_rooms():
    print "You want to import rooms"
    print "if you want to go back to command select type n"
    print "type the name of the json file that came with this game"
    file_name = ""
    while os.path.isfile(file_name) == False:
        input = raw_input('import file name:')
        file_name = input +'.json'
        if os.path.isfile(file_name) == True:
            txt_file = open(file_name, 'r')
            json_data = txt_file.read()
            parsed_json = json.loads(json_data)
            return parsed_json
        print "FAILED TO IMPORT ROOM"


game_data = import_rooms()
while exit != True:
    input = "run"
    print_what = True
    if input == "run":
        run_Room_Navigator = RunRoomNavigator(game_data,"main")
        run_Room_Navigator.run(game_data,"main")
        print_what = False
	input = "save the data"
    if input == "save the data":
        save_the_data(game_data)
        print_what = False   
