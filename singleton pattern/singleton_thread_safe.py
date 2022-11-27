# To fix the problem of naive approach, you have to synchronize threads during the first creation of the Singleton object.

from threading import Lock, Thread


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.The first thread to acquire the lock, reaches this conditional,goes inside and creates the Singleton instance. 
    Once it leaves the lock block, a thread that might have been waiting for the lock
    release may then enter this section. But since the Singleton field is already initialized, the thread won't create a 
    new object.
    """

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]
