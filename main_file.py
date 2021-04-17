# Name: Yumi Go
# Description: Week 12 Project
# (일단 다 한 다음에) 함수 하나에 너무 많은 게 들어있으므로 별도의 함수로 분리해서 그걸 불러오는 식으로 너무 길게 늘어지는 함수들 정리하기
# 다 하면 http://pythontutor.com/visualize.html#mode=edit 돌려보기

import module


def load_races_and_people(races_file, runners_file):
    # This functions reads in the relevant files and creates three lists.
    # races list , names list and ids list.
    # All these lists are returned from this function
    # The lists are then passed into show menu function

    connection_races = open(races_file)
    races_list = []
    names_list = []
    id_list = []
    while True:
        line = connection_races.readline().rstrip()
        if line == "":
            break
        races_list.append(line)
    connection_races.close()

    connection_runners = open(runners_file)
    while True:
        line = connection_runners.readline()
        line_data = line.split(",")
        if line == "":
            break
        names_list.append(line_data[0])
        id_list.append(line_data[1].rstrip())
    connection_runners.close()
    print(f"races_list = {races_list}\n"
          f"names_list = {names_list}\n"
          f"id_list = {id_list}\n")
    return races_list, names_list, id_list


def show_menu(races_list, names_list, id_list):
    # the show menu function should accept three list parameters:
    # the races list, the names list and the ids list.
    # It contains a loop repeatedly displaying the menu until the user chooses the quit option.

    # What lists are passed into show menu ?
    # For each menu option decide on the name of the function to be called and
    # decide which list(s) need to be passed in to each function
    # show_race_details parameters : race list
    while True:
        choose_menu = module.get_positive_int("Choose the number of the menu:\n"
                                              "\t1. Show the results for a race\n"
                                              "\t2. Add results for a race\n"
                                              "\t3. Show all competitors by county\n"
                                              "\t4. Show the winner of each race\n"
                                              "\t5. Show all the race times for one competitor\n"
                                              "\t6. Show all competitors who have won a race\n"
                                              "\t7. Quit\n"
                                              "==> ")
        print("")
        if choose_menu < 1 or choose_menu > 7:
            print("Enter a number between 1 to 7")
        if choose_menu == 1:
            print("***** Show the results for a race *****\n")
            show_race_details(races_list)
            print(f"races_list = {races_list}\n"
                  f"names_list = {names_list}\n"
                  f"id_list = {id_list}\n")
        if choose_menu == 2:
            print("***** Add results for a race *****\n")
            add_new_race(races_list)
            #  When the user chooses to quit
            #  add code to make sure that the contents of places.txt is the same as the list of race locations stored in your program.
            #  Overwrite the existing file with the current list.
            print("[The contents of races.txt file]")  # to make sure that the contents of races.txt is the same as the list of race locations stored in this program.
            connection = open("races.txt")
            read_races_file = connection.read()
            print(read_races_file)
            connection.close()
            print(f"Races locations stored in this program: {races_list}")
            print(f"races_list = {races_list}\n"
                  f"names_list = {names_list}\n"
                  f"id_list = {id_list}\n")
        if choose_menu == 3:
            # This requires printing the competitors names and the competitors ids in two groups.
            # 1. Print those from Cork – ( if the id starts with “CK”)
            # 2. Print them those from Kerry – ( if the id starts with “KY”)
            print("***** Show all competitors by county *****\n")
            print(f"races_list = {races_list}\n"
                  f"names_list = {names_list}\n"
                  f"id_list = {id_list}\n")
        if choose_menu == 4:
            print("***** Show the winner of each race *****\n")
            print(f"races_list = {races_list}\n"
                  f"names_list = {names_list}\n"
                  f"id_list = {id_list}\n")
        if choose_menu == 5:
            print("***** Show all the race times for one competitor *****\n")
            print(f"races_list = {races_list}\n"
                  f"names_list = {names_list}\n"
                  f"id_list = {id_list}\n")
        if choose_menu == 6:
            print("***** Show all competitors who have won a race *****\n")
            print(f"races_list = {races_list}\n"
                  f"names_list = {names_list}\n"
                  f"id_list = {id_list}\n")
        if choose_menu == 7:
            break
    return races_list


# 메뉴 옵션1에 해당함
def show_race_details(races_list):
    # Display the list of races and allow the user enter a number .
    # From this number find the name of the race chosen.
    # Construct the name of the file for this race -
    # Open the file and read the data into 2 lists: and id_list and times_list.
    # Display this information to the screen.
    quit_number = len(races_list) + 1  # add quit menu option
    while True:
        for i, item in enumerate(races_list):
            print(f"{i + 1}: {item}")
        print(f"{quit_number}: Quit")
        race_number = module.get_positive_int("Choice >> ")
        if race_number == quit_number:  # if quit is chosen among the above menu
            break
        race_position = int(race_number) - 1
        id_list_of_each_race = []
        time_list_of_each_race = []
        converted_time_list_of_each_race = []
        title = f"Result for {races_list[race_position]}"
        length_title = len(title)
        division_line = '=' * length_title
        print("")
        print(division_line)
        print(title)
        print(division_line)
        connection = open(f"{races_list[race_position].lower()}.txt")  # open the each venue of race file
        while True:
            line = connection.readline()
            line_data = line.split(",")
            if line == "":
                break
            id_list_of_each_race.append(line_data[0])
            time_list_of_each_race.append(line_data[1].rstrip())
            converted_time_list = convert_time_from_seconds_to_minutes(time_list_of_each_race)
            converted_time_list_of_each_race = converted_time_list
        connection.close()
        for i in range(len(id_list_of_each_race)):
            print(f"{id_list_of_each_race[i]}   {converted_time_list_of_each_race[i]}")
        print("")
        position_of_winner = find_position_of_winner(time_list_of_each_race)
        print(f"{id_list_of_each_race[position_of_winner]} won the race.")
        print("\n\n")
        # 만약 따로 분리한 함수를 넣어주고 싶으면
        # if race_number == 1 or race_number == 2:
        #     display_each_race_details(races_list, race_number)
        #     break
        # else:
        #     print("Enter a correct number.")


def convert_time_from_seconds_to_minutes(time_list):
    converted_time_list = []
    for time in time_list:
        converted_time = f"{int(time) // 60} min {int(time) % 60:>2} seconds"
        converted_time_list.append(converted_time)
    return converted_time_list


def find_position_of_winner(time_list):
    fastest = min(time_list)
    position_of_winner = time_list.index(fastest)
    return position_of_winner


# 메뉴 옵션2에 해당함
def add_new_race(races_list):
    races_file = "races.txt"
    runners_file = "runners.txt"
    while True:
        get_new_venue = module.get_string("Enter a new venue of race: ")  # user에게 new race venue 물어보기
        new_venue = get_new_venue.capitalize()
        races_list.append(new_venue)
        destination_races_file = open(races_file, 'a')  # races.txt 파일에 new_venue 추가
        destination_races_file.write(f"{new_venue}\n")
        destination_races_file.close()
        # Bring all participants' names (IDs) from the file and display it to the user one by one,
        # and let the user enter each participant's time in seconds.
        connection = open(runners_file)
        while True:
            line = connection.readline()
            if line == "":
                break
            line_data = line.split(",")
            get_each_time_in_second = module.get_positive_int(f"Enter the time in seconds for "
                                                              f"{line_data[0]}({line_data[1].rstrip()}) in {new_venue} race\n"
                                                              f"(Enter 0 if this runner did not run in this race)\n"
                                                              f"==> ")
            print("")
            if get_each_time_in_second != 0:  # Only added when a non-zero number is entered
                added_result = f"{line_data[1].rstrip()},{get_each_time_in_second}"
                print(added_result)  # Print this data to the screen as it is entered in the following format: KY-12,319
                print("")
                new_venue_file = f"{get_new_venue.lower()}.txt"  # the name of a new race(in new venue) file which was gotten from above
                destination_new_venue_file = open(new_venue_file, 'a')  # create new race(in new venue) file and write to it in the following format: KY-12,319
                destination_new_venue_file.write(f"{added_result}\n")
                destination_new_venue_file.close()
        connection.close()
        choose_add_or_quit = module.get_positive_int("Do you want to add another new venue for the race continuously?\n"
                                                     "\t1. Yes - Continue\n"
                                                     "\t2. No - Quit\n"
                                                     "==> ")
        print("")
        if choose_add_or_quit == 2:
            break
        # Overwrite the existing file with the current list.


#def save_races_list(races_list):
    # races_list = show_menu()
# the save_races_list function takes the races list as a parameter
# and recreates the races.txt file. Race locations many have been
# added during the program run.


def main():
    races_file = "races.txt"
    runners_file = "runners.txt"
    races_list, names_list, id_list = load_races_and_people(races_file, runners_file)
    show_menu(races_list, names_list, id_list)


main()