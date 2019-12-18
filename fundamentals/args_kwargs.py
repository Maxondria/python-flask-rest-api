def method(arg1, arg2):
    return arg1 + arg2


def addition_simplified(*args):
    print(args)  # A turple of args
    return sum(args)


# addition_simplified(1, 2, 3, 4, 5)

# kwargs


def what_are_kwargs(*args, **kwargs):
    print(args)  # (12, 3, 4, 5, 6, 7, 8)
    print(kwargs)
    # {} if no named args are passed in else we get {'name': 'Jackin', 'location': 'London, UK'}


what_are_kwargs(12, 3, 4, 5, name='Jackin', location="London, UK")
