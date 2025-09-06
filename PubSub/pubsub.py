callbacks = {}


def print_callbacks():
    print(callbacks)


def subscriber(*callbacks_):
    def outer_wrapper(func):
        callbacks[func] = [callback for callback in callbacks_]

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for callback in callbacks[func]:
                callback()
            return result

        return wrapper

    return outer_wrapper


def subscriber1():
    print("subscriber 1 called...")


def subscriber2():
    print("subscriber2 called...")


def subscriber3():
    print("subscriber3 called...")


@subscriber(subscriber1, subscriber3)
def my_func():
    print("my_func called...")
    another_func()


@subscriber(subscriber2)
def another_func():
    print("hello kitty")


my_func()
print_callbacks()
