
def mindecorator(f):
    print("Decorator før")
    def minwrapper(*args):
        result=f()
        return result
    print("Decorator efter")
    return f
    
        
@mindecorator
def funktion1(*a):
    for item in a:
        print(type(item))
    return 37

print(funktion1(2,3,[1,2,3],{1:"abe",2:"buh"}))

