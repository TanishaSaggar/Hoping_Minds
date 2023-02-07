#calling inner function from outer one 
def f():
    a="10"
    print("outer function called")
    
    def g():
        print("inner function")
        print(a)
    g()
    
        
f()    #calling outer function 



        
    

