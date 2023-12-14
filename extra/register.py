class Register:
    id1 = 0
    mobile = 0
    city = ""
    name1 = ""
    id2 = 0
    name2 = ""

    def signup(self):
        print("\tWelcome to sign up page..")
        self.id1 = int(input("Enter Your ID:"))
        self.name1 = input("Enter your Name:")
        self.city = input("enter your City Name:")
        self.mobile = int(input("Enter your mobile no:"))
        f = open('register.txt', 'a')
        f.writelines(f'ID:{self.id1}\n{self.name1}\n{self.city}\n{self.mobile}\n')

    def login(self):
        print("Please Login...")
        self.id2 = int(input("Enter Your id:"))
        self.name2 = input("Enter your Name:")


obj = Register()
try:
    obj.signup()

except Exception as e:
    print("Enter valid Mobile No.", e)
    obj.signup()
else:
    obj.login()
    if obj.id1 == obj.id2 and obj.name1 == obj.name2:
        print("You Have Successfully login.")
    else:
        print("Sorry... Enter valid Id and Name.")
        obj.login()
