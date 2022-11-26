#### Singleton is a creational design pattern, which ensures that only one object of its kind exists and provides a single point of access to it for any other code.

Singleton has almost the same pros and cons as global variables. Although they’re super-handy, they break the modularity of your code.

## Naïve Singleton
It’s pretty easy to implement a sloppy Singleton. You just need to hide the constructor and implement a static creation method.


```
Note:
The same class behaves incorrectly in a multithreaded environment. Multiple threads can call the creation method simultaneously 
and get several instances of Singleton class.
```
