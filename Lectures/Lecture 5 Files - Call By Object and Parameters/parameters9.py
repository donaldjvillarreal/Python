def last_one(*args, **kwargs):
    print("List items:")
    print(args)
    #for arg in args:
     #   print(arg)
    print("Dictionary items:")
    for key, value in kwargs.items():
        print(key, value)

last_one(1, 2, a=3, b=4, c=5)