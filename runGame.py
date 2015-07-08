from RunRoomNavigatorClass import RunRoomNavigator
import json
import os.path
game_data = []
exit = False
run_Room_Navigator = RunRoomNavigator()
while exit != True:
    game_data = run_Room_Navigator.import_rooms()
    game_data = run_Room_Navigator.run(game_data)
    run_Room_Navigator.save_the_data(game_data)