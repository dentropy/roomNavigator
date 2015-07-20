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
                print game_data["items"][game_data["current room"]]
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
        def pocket_item(items, current_room, player_items):
            print "Choose an item, if it exists"
            item = raw_input("-->")
            if item in items[current_room]:   
                if items[current_room][item] != 0:
                    if item in player_items:
                        player_items[item] = player_items[item]+1
                        items[current_room][item] = items[current_room][item]-1
                        print "you picked up an ", item
                        print "you pocket one ", item, " you now have", player_items[item], item, "('s)"
                    else:
                        player_items[item] = 1   
                        items[current_room][item] = items[current_room][item]-1 
                        print "you pocket one ", item, " you now have", player_items[item], item, "('s)" 
                        print "you picked up an ", item  
            else:
                print "can't seem to find that"
            return items, player_items
        def display_stats(health, power_points, level):
            print "level ",level, " health ", health, " and power points", power_points
        def eat(game_data):
            pass
        def run_monster(game_data):
        #[NAME],[Health],[Damage]
            if game_data['current room'] in game_data["monsters"]:
                print "There's a monster in the room"
                print "do you want to fight it 'yes' or 'no'"
                text_input = raw_input("-->")
                if text_input == "no":
                    game_data['current room'] = past_room
                if text_input == "yes":
                    monster_name = game_data["monsters"][game_data['current room']][0]
                    print "time to fight ", monster_name
                    monster_health = random.randint(game_data["monsters"][game_data['current room']][1][0],game_data["monsters"][game_data['current room']][1][1])
                    while monster_health > 0:
                        print "here are your attacks"
                        for i in attacks:
                            print i
                        text_input =  raw_input("choose attack: ")
                        if text_input in attacks:
                            damage_to_monster = random.randint(attacks[text_input][0][0],attacks[text_input][0][1])
                            game_data['power points'] -= attacks[text_input][1]
                            monster_health -= damage_to_monster
                            print "you did ", damage_to_monster, "damage to ", monster_name
                        else:
                            print "what attack?"
                        monster_damage = random.randint(game_data["monsters"][game_data['current room']][1][0],\
                            game_data["monsters"][game_data['current room']][1][1])
                        game_data["health"] -= monster_damage
                        print "monster did ", monster_damage, " to you"
                        display_stats(game_data["health"], game_data['power points'], game_data["level"])
                    current_room = game_data["current room"]
                    del game_data["monsters"][current_room]
                    print "THE MONSTER ID DEAD"
            return game_data
        if game_data == []:
            print "DID NOT IMPORT GAME DATA TYPE 'import'"
            return
        food = game_data["food"]
        past_room = ""
        attacks = game_data["attacks"]
        text_input = ' '
        while text_input != 'exit':
            print_what = True
            game_data = run_monster(game_data)
            print "what would you like to do? Or type what."
            text_input = raw_input("-->")
            if text_input == "go":
                print_what = False
                game_data["current room"], game_data["past room"] =  where_to_go(game_data)
            if text_input == "check for items":
                check_for_items(game_data) 
                print_what = False 
            if text_input == "pocket":
                print_what = False
                game_data["items"] , game_data["player items"] = pocket_item(game_data["items"] , game_data["current room"], game_data["player items"])
            if text_input == "eat":
                print_what = False
                print "what do you want to eat?"
                text_input = raw_input("-->")
                for i in food:
                    for j in game_data["player items"]:
                        if i == j == text_input:
                           print "you eat one", text_input 
                           game_data["health"] += food[i][0]
                           power_points +=  food[i][1]
                           display_stats(game_data["health"], power_points, game_data["level"]) 
                           items[game_data["current room"]][text_input] -= 1
                print "can't find that"
            if text_input == "items":   
                check_for_items(game_data)
                print_what = False
            if text_input == "stats":
                print_what = False
                display_stats(game_data["health"], game_data["power points"], game_data["level"])
            if text_input == "what":
                print game_data["help"]
            if print_what == True:
                print "did not catch that"
        return game_data