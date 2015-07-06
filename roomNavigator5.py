#The rooms list structure is [["name",[direction],[name connecting room]]
import os.path
exit = False
print '''
Welcome to room navigator
In this program you can input or create a text file that contains a a list 
of rooms that are connected to other rooms and when in a room using the 
connection one can navigate to that room
'''
instructions_text = '''
Here are a list of commands you can use when 'use command:' shows up
import - imports a past rooms from the name of the text file in 
    the same folder
run - remember to import run the room simulation /exit is too exit
    type exit to return to 'use command'
create room - run through the instructions in order to create a new room
help - print the instructions you are reading
list all rooms - lists the names of all the rooms
print room list - prints the data structure
save the rooms - saves the current data structure into a text document
delete room - delete room and connections to it
'''    

#FOR CREATING THE ROOMS FROM A BACKUP FILE
import json
def import_rooms():
    print "You want to import rooms"
    print "if you want to go back to command select type n"
    input = raw_input('import file name:')
    file_name = input +'.json'
    if input == "n":
        return
    else:
        if os.path.isfile(file_name) == True:
            txt_file = open(file_name, 'r')
            json_data = txt_file.read()
            parsed_json = json.loads(json_data)
            return parsed_json
    print "FAILED TO IMPORT ROOM"
#DONE CREATING THE ROOMS FROM A BACKUP FILE
#RUNING ROOMS
def run_room(rooms, current_room):
    if rooms == [[],[],[]]:
        print "ERROR TRY IMPORTING A FILE"
        return 
    text_input = ' '
    where = True
    while text_input != 'exit':
        print "You are in room %s" % current_room
        print "Here is a list of the rooms you can go plus where they are"    
        print rooms[current_room]
        for direciton , name in rooms[current_room].iteritems():
            print  name + " is to the " + direciton
        text_input = raw_input("where would you like to go:")
        if text_input == "exit":
            return
        if text_input in rooms[current_room]:
            current_room = rooms[current_room][text_input]
            print " *************************"
        if text_input == "moo":
            print "MOOOOOOOO"
            return
        where = True
        if where == True:
            print "Whoops Where's that? \n *************************"
# DONE RUNNING ROOMS
# CREATING A NEW ROOM
def print_room_list(rooms):
    print rooms
def list_all_rooms(rooms):
    print "printing rooms"
    for i in range(len(rooms)):
        print rooms[i][0]
def create_room(rooms):
    print "Ok what room do you want to add to?"
    print "Here is a list:"
    print rooms.keys()
    works = False
    while works == False:
        room_prime =  raw_input("what room do you choose:")
        if room_prime in rooms:
            print"Should exit"
            works = True
        else:
            print "wait where's that"
    connecting_term = raw_input("how to get to the new room:")
    new_room_name = raw_input("new room name:")
    rooms[room_prime][connecting_term] = new_room_name
    print "To connect back type y or n"
    connection_back = raw_input("type y or n:")
    if connection_back == "y":
        connecting_term_back = raw_input("How do you get back:")
        rooms[new_room_name] = {connecting_term_back:room_prime}
    else:
        rooms[new_room_name] ={}
    return rooms
# DONE CREATING NEW ROOM
#SAVING THE DATA STRUCTURE
def save_the_rooms(rooms):
    json_string = json.dumps(rooms)
    name_of_file = raw_input("name the file you wish to save to:")
    txt_file = open(name_of_file + ".json", 'w+')
    txt_file.write(json_string)
    txt_file.close()
# SAVING THE DATA STRUCTURE
#DELETE ROOM
def del_room (rooms):
    print "here are the room names"
    for i in rooms:
        print i
    del_room_name = raw_input("which room would you like to delete:")
    if del_room_name in rooms:
        del rooms[del_room_name]
        i_list = []
        j_list = []
        for i in rooms:
            for j in rooms[i]:
                if rooms[i][j] == del_room_name:
                    i_list.append(i)
                    j_list.append(j)
        for k in range(len(i_list)):
            del rooms[i_list[k]][j_list[k]]
    else:
        print "Can't find that room"
# RUN THE REAL PROGRAM    
print instructions_text
rooms = [[],[],[]]
while exit != True:
    input = raw_input('use command:')
    print_what = True
    if input == "import":
        rooms = import_rooms()
        print_what = False
    if input == "run":
        run_room(rooms,"main")
        print_what = False
    if input == 'help':
        print instructions_text
        print_what = False
    if input == "create room":
        rooms = create_room(rooms)
        print_what = False
    if input == "list all rooms":
        list_all_rooms(rooms)
        print_what = False
    if input == "print room list":
        print_room_list(rooms)
        print_what = False
    if input == "save the rooms":
        save_the_rooms(rooms)
        print_what = False
    if input == "delete room":
        del_room(rooms)
    if print_what == True:
        print "command does not exist try again"
# DONE RUNING THE REAL PROGRAM    
