class RunRoomNavigator:
    def __init__(self):
        print "type 'what' for help" 
    def import_rooms(self):
        import json
        import os.path
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
    def save_the_data(self, game_data):
        import json
        import os.path
        if game_data == []:
            print "DID NOT IMPORT GAME DATA TYPE 'import'"
            return
        json_string = json.dumps(game_data)
        name_of_file = raw_input("name the file you wish to save to:")
        txt_file = open(name_of_file + ".json", 'w+')
        txt_file.write(json_string)
        txt_file.close()
    def run(self, game_data):
        def check_for_items(items, current_room):
            print items[current_room]
        def where_to_go(rooms, current_room):
            print "You are in room %s" % current_room
            print "Here is a list of the rooms you can go plus where they are"    
            print "You can also type check for items"
            for direciton , name in rooms[current_room].iteritems():
                print  name + " is " + direciton
            text_input = raw_input("where would you like to go:")
            if text_input in rooms[current_room]:
                current_room = rooms[current_room][text_input]
                print "you are now in", current_room
                return current_room
            else:
                print "Whoops Where's that? \n *************************"
        def pocket_item(items, current_room, player_items):
            print "Choose an item, if it exists"
            item = raw_input("-->")
            for i in items[current_room]:
                if i == item:
                    if items[current_room][i] != 0:
                        for j in player_items:
                            if j == item:
                                player_items[item] = player_items[item]+1
                        else:
                            player_items[item] = 1
                        print "you pocket one ", item, " you now have", player_items[item], "pie('s)"
                        items[current_room][item] = items[current_room][item]-1
                        return items, player_items
            else:
                print "can't seem to find that"
        def display_stats(health, power_points, level):
            print "level ",level, " health ", health, " and power points", power_points
        if game_data == []:
            print "DID NOT IMPORT GAME DATA TYPE 'import'"
            return
        player_items = game_data["player_items"]
        health = game_data["health"]
        power_points = game_data["power_points"]
        level = game_data["level"]
        food = game_data["food"]
        rooms = game_data["rooms"]
        items = game_data["items"] 
        text_input = ' '
        while text_input != 'exit':
            print_what = True
            print "what would you like to do?"
            text_input = raw_input("-->")
            if text_input == "where to go":
                print_what = False
                game_data["current room"] =  where_to_go(rooms, game_data["current room"])
            if text_input == "check for items":
                print_what = False
                check_for_items(items, game_data["current room"])  
            if text_input == "pocket":
                print_what = False
                items, player_items = pocket_item(items, game_data["current room"], player_items)
            if text_input == "eat":
                print_what = False
                print "what do you want to eat?"
                text_input = raw_input("-->")
                for i in food:
                    for j in player_items:
                        if i == j == text_input:
                           print "you eat one", text_input 
                           health += food[i][0]
                           power_points +=  food[i][1]
                           display_stats(health, power_points, level) 
                           items[game_data["current room"]][text_input] -= 1
                print "can't find that"
            if text_input == "items":
                print_what = False
                if player_items != {}:
                    print "here is a list of your items"
                    for i in player_items:
                        print i
                else:
                    print "nothing here"
            if text_input == "stats":
                print_what = False
                display_stats(health, power_points, level)
            if text_input == "what":
                print game_data["help"]
            if print_what == True:
                print "did not catch that"