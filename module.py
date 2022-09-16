def get_positive_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num >= 0:
                break
            else:
                print("Enter a positive number")
        except:
            print("Error occured")

    return num



def get_positive_float(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num >= 0:
                break
        except:
            print("Enter a positive floating number")
    return num


def get_string(prompt):
    while True:
        try:
            answer = input(prompt)
            length = len(answer)
            if length != 0:
                break
        except:
            print("Please enter a non-empty string")
    return answer


def main():
    name = get_string("What is your name? ")
    print(name)

# main()