from quiz_operations import *


def display_game():
    print("\tWELCOME TO TOPS QUIZE GAMING CHALLENGE")
    print(f"\tSelect your role :\n"
          f"\t\t-> Quize Matser  (press 1)\n"
          f"\t\t-> Quize Cracker  (press 2)")
    user_role = int(input("Enter Your Role:"))
    if user_role == 1:
        quiiz_matser()
    else:
        print("nothing")


def quiiz_matser():
    print("\t\t WELCOME MASTER")
    print("SHAKE YOUR BRAIN AND ADD SOME CHALLENGING QUESTION..")

    print(f"\t\tMENU")
    print(f"\tpress 1 for ADD Questions\n"
          f"\tpress 2 for VIEW Questions\n"
          f"\tpress 3 for DELETE questions\n"
          f"\tpress 4 for exit")
    operation = int(input("Which operations you want to perform :"))
    if operation == 1:
        add()
        quiiz_matser()
    elif operation == 2:
        view()
        quiiz_matser()
    elif operation == 3:
        print("3")
    elif operation == 4:
        print("EXit")
    else:
        print("Enter valid choice")
        quiiz_matser()


display_game()
