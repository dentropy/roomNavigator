from RunRoomNavigatorClass import RunRoomNavigator
game_data = []
exit = False
run_Room_Navigator = RunRoomNavigator()
while exit != True:
    game_data = run_Room_Navigator.import_rooms()
    run_Room_Navigator.run(game_data)
    run_Room_Navigator.save_the_data(game_data)   
