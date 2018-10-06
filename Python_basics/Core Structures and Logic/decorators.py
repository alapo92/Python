# decorators are functions that get called before another function
import functools


def moj_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("in the decorator!")
        func()
        print("after the decorator!")
    return function_that_runs_func  # this function replaces the my_function function passed as func


@moj_decorator
def my_function():
    print("I'm the function!")


my_function()


# useful for passing users permissions - if the user doesnt match admin permissions they wont see the page
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_thatruns_func(*args, **kwargs):
            print("in the decorator!")
            if number == 56:
                print('not running the function!')
            else:
                func(*args, **kwargs)
            print("after the decorator!")
        return function_thatruns_func
    return my_decorator


@decorator_with_arguments(57)
def my_function_two(x, y):
    print(x + y)


my_function_two(10, 15)
