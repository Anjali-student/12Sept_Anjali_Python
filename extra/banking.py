import random

print("\tBANKING SYSTEM")


def acount_details():
    ac_no = random.randint(1111111111, 99999999999)
    print("Your Account NO.:", ac_no)
    ac_name = input("Enter A/C holder Name: ")
    print(f"Enter A/C Type:\n"
          f"Press 1 for Saving\n"
          f"press 2 for Current")


acount_details()
