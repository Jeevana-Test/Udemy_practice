#write a deccorotor function for the practice the topic with the explanation of each step how to use when to use
def decorator_function(original_function):
    """This is a decorator function that takes another function as an argument."""
    def wrapper_function(*args, **kwargs):
        """This is the wrapper function that will be executed instead of the original function."""
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function
@decorator_function
def my_func():
    print("This is my function.")
my_func()
#expalin with the simple terms ans in real project how i will use the decorators
def my_decortaor(func):
    def wrapper():
        print("Before executing the function")
        func()
        print("After executing the function")
    return wrapper
@my_decortaor
def say_hello():
    print("Hello, World!")
say_hello()

@my_decortaor
def say_bye():
    print("Goodbye, World!")
say_bye()
# inthe above above what wraper is doing?#
# In the above code, the `wrapper` function is a nested function
# inside the `my_decorator` function. It is responsible for
# adding additional behavior before and after
# the execution of the original function (`func`).