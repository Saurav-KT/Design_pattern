### Singletons are classes which can be instantiated once, and can be accessed globally.
#### Singleton is a creational design pattern, which ensures that only one object of its kind exists and provides a single point of access to it for any other code.Just like a global variable, the Singleton pattern lets you access some object from anywhere in the program. However, it also protects that instance from being overwritten by other code.

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
