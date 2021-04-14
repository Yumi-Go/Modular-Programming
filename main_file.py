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
        if choose_menu < 1 or choose_menu > 7:
            print("Enter a number between 1 to 7")
        if choose_menu == 1:
            print("You choose 1")
            print(f"races_list = {races_list}\n"
                  f"names_list = {names_list}\n"
                  f"id_list = {id_list}\n")
        if choose_menu == 2:
            print("You choose 2")
            print(f"races_list = {races_list}\n"
                  f"names_list = {names_list}\n"
                  f"id_list = {id_list}\n")
        if choose_menu == 3:
            print("You choose 3")
            print(f"races_list = {races_list}\n"
                  f"names_list = {names_list}\n"
                  f"id_list = {id_list}\n")
        if choose_menu == 4:
            print("You choose 4")
            print(f"races_list = {races_list}\n"
                  f"names_list = {names_list}\n"
                  f"id_list = {id_list}\n")
        if choose_menu == 5:
            print("You choose 5")
            print(f"races_list = {races_list}\n"
                  f"names_list = {names_list}\n"
                  f"id_list = {id_list}\n")
        if choose_menu == 6:
            print("You choose 6")
            print(f"races_list = {races_list}\n"
                  f"names_list = {names_list}\n"
                  f"id_list = {id_list}\n")
        if choose_menu == 7:
            break
    return choose_menu


def save_races_list(races_list):
    # the save_races_list function takes the races list as a parameter
    # and recreates the races.txt file. Race locations many have been
    # added during the program run.
    print("hello")


def convert_time_from_seconds_to_minutes(time_list):
    converted_time_list = []
    for time in time_list:
        converted_time = f"{int(time) // 60} min {int(time) % 60} seconds"
        converted_time_list.append(converted_time)
    return converted_time_list


def find_position_of_winner(time_list):
    fastest = min(time_list)
    position_of_winner = time_list.index(fastest)
    return position_of_winner


def display_each_race_details(races_list, race_number):
    print("display each race details")
    race_position = int(race_number) - 1
    id_list_of_each_race = []
    time_list_of_each_race = []
    converted_time_list_of_each_race = []
    title = f"Result for {races_list[race_position]}"
    length_title = len(title)
    division_line = '=' * length_title
    print(title)
    print(division_line)
    connection = open(f"{races_list[race_position].lower()}.txt")
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
    print()
    position_of_winner = find_position_of_winner(time_list_of_each_race)
    print(f"{id_list_of_each_race[position_of_winner]} won the race.")


def show_race_details(races_list):
    # Display the list of races and allow the user enter a number .
    # From this number find the name of the race chosen.
    # Construct the name of the file for this race -
    # Open the file and read the data into 2 lists: and id_list and times_list.
    # Display this information to the screen.
    for i, item in enumerate(races_list): # 여기 그냥 단순 메뉴 제시로 수정하는게 어떨지.. 굳이 enumerate로 할 필요가 있을지..
        print(f"{i+1}: {item}")
    while True:
        race_number = module.get_positive_int("Choose a race: ")
        # id_list_of_each_race = []
        # time_list_of_each_race = []
        # converted_time_list_of_each_race = []
        if race_number == 1 or race_number == 2:
            if race_number == 1:
                display_each_race_details(races_list, race_number)
                # title = f"Result for {races_list[0]}"
                # length_title = len(title)
                # division_line = '=' * length_title
                # print(title)
                # print(division_line)
                # connection = open(f"{races_list[0].lower()}.txt")
                # while True:
                #     line = connection.readline()
                #     line_data = line.split(",")
                #     if line == "":
                #         break
                #     id_list_of_each_race.append(line_data[0])
                #     time_list_of_each_race.append(line_data[1].rstrip())
                #     converted_time_list = convert_time_from_seconds_to_minutes(time_list_of_each_race)
                #     converted_time_list_of_each_race = converted_time_list
                # connection.close()
                # for i in range(len(id_list_of_each_race)):
                #     print(f"{id_list_of_each_race[i]}   {converted_time_list_of_each_race[i]}")
                # print()
                # position_of_winner = find_position_of_winner(time_list_of_each_race)
                # print(f"{id_list_of_each_race[position_of_winner]} won the race.")
                break
            elif race_number == 2:
                display_each_race_details(races_list, race_number)
                # print(f"Result for {races_list[1]}")
                break
        else:
            print("Enter a correct number.")


def main():
    races_file = "races.txt"
    runners_file = "runners.txt"
    races_list, names_list, id_list = load_races_and_people(races_file, runners_file)
    show_menu(races_list, names_list, id_list)
    save_races_list(races_list)
    show_race_details(races_list)


main()