from threading import Thread

from singleton_naive import SingletonMeta


class Singleton(metaclass=SingletonMeta):
    def __init__(self, name, address, pincode):
        self.name = name
        self.address = address
        self.pincode = pincode

    def employee_details(self):
        print(self.name, self.address, self.pincode)


if __name__ == "__main__":
    s1 = Singleton("saurav", "BLR", "560105")
    s2 = Singleton("saurav", "BLR", "560105")
    # Id returns the location where the variable is stored. both the variable returns the same value
    print(id(s1))
    print(id(s2))

    # Same singleton class behaves incorrectly in a multithreaded environment.

    process1 = Thread(target=Singleton, args=("saurav", "BLR", "560105"))
    process2 = Thread(target=Singleton, args=("saurav", "BLR", "560106"))
    # Id returns the location where the variable is stored. both the variable returns the different value
    print(id(process1))
    print(id(process2))
