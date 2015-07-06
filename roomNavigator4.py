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
'''	

#FOR CREATING THE ROOMS FROM A BACKUP FILE
import json
def import_rooms():
	print "You want to import rooms"
	print "if you want to go back to command select type n"
	input = raw_input('import file name:')
	if input == "n":
		return
	else:
		txt_file = open(input+'.json', 'r')
		json_data = txt_file.read()
		parsed_json = json.loads(json_data)
		return parsed_json
#DONE CREATING THE ROOMS FROM A BACKUP FILE
#RUNING ROOMS
def find_room(rooms, room_name):
	for j in range(len(rooms)):
		if rooms[j][0] == room_name:
			return j
	return -1	
def run_room(rooms, current_room):
	text_input = ' '
	where = True
	while text_input != 'exit':
		print "You are in room %s" % rooms[current_room][0]
		print "Here is a list of the rooms you can go plus where they are"	
		for i in range(len(rooms[current_room][1])):
			print rooms[current_room][1][i] + " is " + rooms[current_room][2][i]
		text_input = raw_input("where would you like to go:")
		for i in range(len(rooms[current_room][1])):
			if rooms[current_room][1][i] == text_input:
				current_room = find_room(rooms, rooms[current_room][2][i])
				print " *************************"
				break
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
	list_all_rooms(rooms)
	room_name =  raw_input("what room do you choose:")
	room_position = find_room(rooms, room_name)
	while (room_position == -1):
		print "wait where's that?"
		room_name =  raw_input("what room do you choose:")
		room_position = find_room(rooms, room_name)
	connecting_term = raw_input("how to get to the new room:")
	new_room_name = raw_input("new room name:")
	print room_position
	print rooms[room_position]
	rooms[room_position][1].append(connecting_term)
	rooms[room_position][2].append(new_room_name)
	rooms.append([new_room_name,[],[]])
	print "To connect back type y or n"
	connection_back = raw_input("type y or n:")
	if connection_back == "y":
		connecting_term_back = raw_input("How do you get back:")
		rooms[len(rooms)-1][1].append(connecting_term_back)
		rooms[len(rooms)-1][2].append(rooms[room_position][0])
	return rooms
# DONE CREATING NEW ROOM
#SAVING THE DATA STRUCTURE
def save_the_rooms(rooms):
	rooms_string = ""
	for i in rooms:
		print i
		rooms_string += i[0] + "\n"
		for j in i[1]:
			rooms_string += j + " "
		rooms_string += "\n"
		for j in i[2]:
			rooms_string += j + " "
		rooms_string += "\n"
	#print rooms_string
	name_of_file = raw_input("name the file you wish to save to:")
	txt_file = open(name_of_file + ".txt", 'w')
	txt_file.write(rooms_string)
	txt_file.close()
# SAVING THE DATA STRUCTURE
# RUN THE REAL PROGRAM	
print instructions_text
while exit != True:
	input = raw_input('use command:')
	print_what = True
	if input == "import":
		rooms = import_rooms()
		print_what = False
	if input == "run":
		run_room(rooms,0)
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
	if print_what == True:
		print "command does not exist try again"
# DONE RUNING THE REAL PROGRAM	
