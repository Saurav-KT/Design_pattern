from singleton_thread_safe import SingletonMeta
from threading import Lock, Thread


class Singleton(metaclass=SingletonMeta):
    """
       We'll use this property to prove that our Singleton really works.
       """

    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """


def test_singleton(name: str, address: str) -> None:
    singleton = Singleton(name, address)
    print(singleton.name, singleton.address)


if __name__ == "__main__":
    # The client code.

    "If you see the same value, then singleton was reused (yay!) If you see different values,then 2 singletons were " \
    "created (booo!!) RESULT:\n "

    process1 = Thread(target=test_singleton, args=("saurav", "Bangalore"))
    process2 = Thread(target=test_singleton, args=("priya", "Delhi"))
    process1.start()
    process2.start()
