def my_method(arg1, arg2):
    return arg1 + arg2

print(my_method(4, 8))

def addition_simplified(*args):
    return sum(args)

print(addition_simplified(4, 8, 7))

##

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(2, 4, 6, 7, 8, name='Jose', location='UK')
