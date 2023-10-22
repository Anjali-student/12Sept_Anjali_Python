def game_Title():
    print("\tWELCOME TO TOPS QUIZE GAMING CHALLENGE")
    print(f"\tSelect your role :\n"
          f"\t\t-> Quize Matser  (press 1)\n"
          f"\t\t-> Quize Cracker  (press 2)")
    user_role = int(input("Enter Your Role:"))
    if user_role == 1:
        game_menu()
    else:
        print("nothing")


def game_menu():
    print("\t\t WELCOME MASTER")
    print("SHAKE YOUR BRAIN AND ADD SOME CHALLENGING QUESTION..")

    print(f"\t\tMENU")
    print(f"\tpress 1 for ADD Questions\n"
          f"\tpress 2 for VIEW Questions\n"
          f"\tpress 3 for DELETE questions\n"
          f"\tpress 4 for exit")
    operation = int(input("Which operations you want to perform :"))
    if operation == 1:
        question()
        game_menu()
    elif operation == 2:
        view()
        game_menu()
    elif operation == 3:
        dele_fun()
        game_menu()
    elif operation == 4:
        print("EXIT")
    else:
        print("Enter valid choice")
        game_menu()

def question():
    global que_list
    for i in range(1):
        que_list = {}
        que = input("Enter question :")
        que_list[que] = {}
        op_1 = input("Enter option-1 :")
        op_2 = input("Enter option-2 :")
        ans = input("Enter The right answer :")
        que_list[que]["A"] = op_1
        que_list[que]["B"] = op_2
        que_list[que]["Right Answer"] = ans
        temp = 1
        f = open('question.txt', 'a')
        for k in que_list.items():
            temp = temp + 1
            f.write(f"{temp}) {que} \nA :{op_1} \nB :{op_2} \nRIGHT ANS :{ans}\n")
    return que_list

def view():
    file = open("question.txt", "r")
    while file:
        line = file.readline()
        print(line,end= "")
        if line == "":
            break
    file.close()

def dele_fun():
    desicion = input("are you sure you want to delete : ")
    if(desicion == "yes"):
        file=open("question.txt",'r+')
        file.truncate()
        print("You have successfully Deleted all data")
    else:
        print("Not deletd")


game_Title()