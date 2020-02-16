

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))
    return x+1

def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1



def mintest():
    mintest.tael+=17
    return mintest.tael

foo(42)

print("antal kald før",succ.calls)
for i in range(10):
    succ(i)
    
print("antal kald efter",succ.calls)

#Bemærk hvordan en variabel kan initieres udenfor funktionen
mintest.tael=2
print("sæt variabel udenfor funktion",mintest())


