import functools


def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print('In the decorator')
        func()
        print('After the decorator')
    return function_that_runs_func


@my_decorator
def my_function():
    print('my_function() is running')


# my_function()

##


def decorator_with_arg(role):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print('In the decorator')
            if role != 'admin':
                print('Not running the function')
            else:
                func(*args, **kwargs)
            print('After the decorator')
        return function_that_runs_func
    return my_decorator


@decorator_with_arg('admin')
def my_function_two(x, y):
    print('Hello from function two')
    print(x + y)


my_function_two(1, 3)
