def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print(type(kwargs))


what_are_kwargs(12, 13, 15, name='Peter', location='germany')
