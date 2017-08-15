

def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("decorator as function")
        func(*args, **kwargs)

    return wrapper


class DecoratorClass(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Decorator as class')
        self.func(*args, **kwargs)


@decorator_func
def foo():
    print('foo')


@decorator_func
def foo(arg):
    print('foo', arg)


foo("teste")


@DecoratorClass
def foo():
    print('foo')

foo()
