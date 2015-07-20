import json
import os.path
import random
class RunRoomNavigator:
    def import_rooms(self):
        print "You want to import rooms probably rooms"
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
        if game_data == []:
            print "DID NOT IMPORT GAME DATA TYPE 'import'"
            return
        json_string = json.dumps(game_data)
        name_of_file = raw_input("name the file you wish to save to:")
        txt_file = open(name_of_file + ".json", 'w+')
        txt_file.write(json_string)
        txt_file.close()
    def run(self, game_data):
        print "type 'what' for help"
        def check_for_items(game_data):
             if game_data["current room"] in game_data["items"]:
                for i in game_data["items"][game_data["current room"]]:
                    if game_data["items"][game_data["current room"]][i] >= 1:
                        print i
             else:
                print "there is nothing in", game_data["current room"]
        def where_to_go(game_data):
            current_room = game_data["current room"]
            print "You are in room %s" % game_data["current room"]
            print "Here is a list of the rooms you can go plus where they are"    
            print "You can also type check for items"
            for direciton , name in game_data["rooms"][current_room].iteritems():
                print name, " is ", direciton
            text_input = raw_input("where would you like to go:")
            if text_input in game_data["rooms"][current_room]:
                past_room = current_room
                current_room = game_data["rooms"][current_room][text_input]
                print "you are now in", current_room
                return current_room,past_room
            else:
                print "Whoops Where's that? \n *************************"
                return game_data["current room"], game_data["past room"]
        def pocket_item(game_data):
            print "Choose an item, if it exists"
            item = raw_input("-->")
            current_room = game_data["current room"]
            items = game_data["items"]
            if item in game_data["items"][current_room] and game_data["items"][current_room] >= 1:   
                if game_data["items"][current_room][item] >= 1:
                    if item in game_data["player items"]:
                        game_data["player items"][item] = game_data["player items"][item]+1
                        items[current_room][item] = items[current_room][item]-1
                        print "you picked up an ", item
                        print "you pocket one ", item, " you now have", player_items[item], item, "('s)"
                    else:
                        game_data["player items"][item] = 1   
                        items[current_room][item] = items[current_room][item]-1 
                        print "you pocket one ", item, " you now have", game_data["player items"][item], item, "('s)" 
                        print "you picked up an ", item  
            else:
                print "can't seem to find that"
            return game_data
        def display_stats(game_data):
            print "level ", game_data["level"], " health ", game_data["health"], " and power points", game_data["power points"]
        def eat(game_data):
            print "what do you want to eat?"
            text_input = raw_input("-->")
            for i in game_data["food"]:
                for j in game_data["player items"]:
                    if i == j == text_input:
                       print "you eat one", text_input 
                       game_data["health"] += game_data["food"][i][0]
                       game_data["power points"] +=  game_data["food"][i][1]
                       display_stats(game_data) 
                       game_data["items"][game_data["current room"]][text_input] -= 1
                print "can't find that"
            return game_data
        def run_monster(game_data):
            current_room = game_data["current room"]
            if game_data['current room'] in game_data["monsters"]:
                print "There's a monster in the room"
                print "do you want to fight it 'yes' or 'no'"
                text_input = raw_input("-->")
                if text_input == "yes":
                    monster = game_data["monsters"][current_room]
                    monster_health = random.randint(monster["health"][0],monster["health"][1])
                    print "time to fight ", monster["name"]
                    print monster["name"], " has ",  monster_health, "health"
                    while monster_health > 0 and game_data["health"] > 0:
                        print "here are your attacks"
                        for i in game_data["attacks"]:
                            print i
                        text_input =  raw_input("choose attack: ")
                        if text_input in game_data["attacks"]:
                            damage_to_monster = random.randint(game_data["attacks"][text_input]["damage"][0],game_data["attacks"][text_input]["damage"][1])
                            game_data['power points'] -= game_data["attacks"][text_input]["power points"]
                            monster_health -= damage_to_monster
                            print "you did ", damage_to_monster, "damage to ", monster["name"]
                        else:
                            print "what attack?"
                        monster_damage = random.randint(game_data["monsters"][current_room]["damage"][0],\
                            game_data["monsters"][current_room]["damage"][1])
                        game_data["health"] -= monster_damage
                        print monster["name"], " did ", monster_damage, "damage to you"
                        display_stats(game_data)
                    if monster_health <= 0:
                        del game_data["monsters"][current_room]
                        print "THE MONSTER ID DEAD"
                else:
                    print "OK run away"
                    game_data['current room'] = game_data['past room']
            return game_data
        def list_inventory(game_data):
            if len(game_data["player items"]) != 0:
                for i in game_data["player items"]:
                    print i
            else:
                print "sadly it's empty"
        def check_input(game_data):
            print_what = True
            game_data = run_monster(game_data)
            if game_data["health"] <= 0:
                print "Game Over \n\n\n\n\n\n\n\n\n\n"
                game_data = "dead"
                return game_data, True
            print "what would you like to do? Or type what."
            text_input = raw_input("-->")
            if text_input == "go":
                print_what = game_data, False#exit the while loop
                game_data["current room"], game_data["past room"] =  where_to_go(game_data)
            if text_input == "check for items":
                check_for_items(game_data) 
                print_what = False 
            if text_input == "pocket":
                print_what = False
                game_data = pocket_item(game_data)
            if text_input == "eat":
                print_what = False
                game_data = eat(game_data)
            if text_input == "items":   
                check_for_items(game_data)
                print_what = False
            if text_input == "stats":
                print_what = False
                display_stats(game_data)
            if text_input == "what":
                print game_data["help"]
            if text_input == "list inventory":
                print_what = False
                list_inventory(game_data)
            if text_input == "exit":
                return game_data, True
            if print_what == True:
                print "did not catch that"
            return game_data, False #run again 
        if game_data == []:
            print "DID NOT IMPORT GAME DATA TYPE 'import'"
            return
        while True:
            game_data, play_condition = check_input(game_data)
            if play_condition == True:
                break
        return game_data