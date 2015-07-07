class RunRoomNavigator:
    def __init__(self, game_data, current_room):
        print "type 'what' for help" 
    def run(self, game_data, current_room):
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
            print "what would you like to do?"
            text_input = raw_input("-->")
            if text_input == "where to go":
                current_room = where_to_go(rooms, current_room)
            if text_input == "check for items":
                check_for_items(items, current_room)  
            if text_input == "pocket":
                items, player_items = pocket_item(items, current_room, player_items)
            if text_input == "eat":
                print "what do you want to eat?"
                text_input = raw_input("-->")
                for i in food:
                    for j in player_items:
                        if i == j == text_input:
                           print "you eat one", text_input 
                           health += food[i][0]
                           power_points +=  food[i][1]
                           display_stats(health, power_points, level) 
                           del items[text_input]
                print "can't find that"
            if text_input == "items":
                if player_items != {}:
                    print "here is a list of your items"
                    for i in player_items:
                        print i
                else:
                    print "nothing here"
            if text_input == "stats":
                display_stats(health, power_points, level)
            if text_input == "what":
                print game_data["help"]