

#Ekstra overbygning for at få parametre ind i selve decorator. Her count.
def mydecorator_not_actually(count):
    def true_decorator(f):
        def wrapped(*args, **kwargs):
            for i in range(count):
                print ("Before decorated function")
            r = f(*args, **kwargs)
            for i in range(count):
                print ("After decorated function")
            return r
        return wrapped
    return true_decorator

@mydecorator_not_actually(2)    #Her overføres count til decorator
def myfunc(a):
    print ("my function", a)
    return a*2

r = myfunc(37)
print (r)

