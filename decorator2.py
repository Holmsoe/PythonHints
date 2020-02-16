
#Struktur for decorator.


def our_decorator(func):        #Decorator har en funktion som argument
    def function_wrapper(x):    #Wrapper har samme antal argumenter som funktionen
        print("Action foer funktion")
        func(x)                 #Funktionen kaldes
        print("Action efter funktion")
    return function_wrapper

@our_decorator                  #Decorator kaldes
def minfunktion(n):             #Normal funktion
    print(n+1)
    return n + 1

minfunktion(10)                 #Funktion kaldes
