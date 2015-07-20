class GodModeClass:
	def __init__(self):
		print '''
Welcome to room navigator
In this program you can input or create a text file that contains a a list 
of rooms that are connected to other rooms and when in a room using the 
connection one can navigate to that room
'''   
	# CREATING A NEW ROOM
	def print_room_list(self, game_data):
		if game_data == []:
			print "DID NOT IMPORT GAME DATA TYPE 'import'"
			return
		game_data = game_data["rooms"]
		print rooms
	def list_all_rooms(self, game_data):
		if game_data == []:
			print "DID NOT IMPORT GAME DATA TYPE 'import'"
			return
		print game_data["rooms"]
	def create_room(self, game_data):
		if game_data == []:
			print "DID NOT IMPORT GAME DATA TYPE 'import'"
			return
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
	#DELETE ROOM
	def del_room (self, game_data):
		if game_data == []:
			print "DID NOT IMPORT GAME DATA TYPE 'import'"
			return
		rooms = game_data["rooms"]
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
		return rooms