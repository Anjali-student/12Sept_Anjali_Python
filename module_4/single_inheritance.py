class super:
    def func1(self):
        print("This function is in parent class.")


# Derived class


class sub(super):
    def func2(self):
        print("This function is in child class.")


# Driver's code
object = sub()
object.func1()
object.func2()