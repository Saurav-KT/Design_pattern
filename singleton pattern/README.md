#### Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.
The Singleton pattern solves two problems at the same time, violating the Single Responsibility Principle:
Here’s how it works: imagine that you created an object, but after a while decided to create a new one. Instead of receiving a fresh object, you’ll get the one you already created.

1. Ensure that a class has just a single instance. Why would anyone want to control how many instances a class has? The most common reason for this is to control access to some shared resource—for example, a database or a file.

2. Provide a global access point to that instance. Remember those global variables that you (all right, me) used to store some essential objects? While they’re very handy, they’re also very unsafe since any code can potentially overwrite the contents of those variables and crash the app.

Just like a global variable, the Singleton pattern lets you access some object from anywhere in the program. However, it also protects that instance from being overwritten by other code.

Singleton has almost the same pros and cons as global variables. Although they’re super-handy, they break the modularity of your code.

## Naïve Singleton
It’s pretty easy to implement a sloppy Singleton. You just need to hide the constructor and implement a static creation method.


```
Note:
The same class behaves incorrectly in a multithreaded environment. Multiple threads can call the creation method simultaneously 
and get several instances of Singleton class.
```
## Singleton with multithreaded

        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
