def scope_test():
    
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "main function spam"
    print('Main function',spam)
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


#We call main function
#We call local but this does not change spam in main function space
#we call non local which shares variable inside whole function space
#We call global function with gloabl variable. This does not change variable inside main space
#We print variable outside function. Here the gloabl variable is valid.
    
#summary: without any spec the varibale is only valid inside actual (sub)function.
# with nonlocal varibale is shared in main function
#global is valid outside main function
   
scope_test()
print("In global scope:", spam)
