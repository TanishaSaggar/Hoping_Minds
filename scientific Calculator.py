#scientific calculator

import math

def add():
    a,b=map(int,input("enter 2 numbers").split())
    d=a+b

    print(d)
    
def sub():
    a,b=map(int,input("enter 2 numbers").split())
    d=a-b
    print(d) 
    
def mult():
    a,b=map(int,input("enter 2 numbers").split())
    d=a*b
    print(d)

def div():
    a,b=map(int,input("enter 2 numbers").split())
    d=a/b
    print(d)
    
def floor():
    a,b=map(int,input("enter 2 numbers").split())
    d=a//b
    print(d)
    
def modulus():
    a,b=map(int,input("enter 2 numbers").split())
    d=a%b
    print(d)
    
def sin():
    a=int(input("enter a number: "))
    d=math.sin(a)
    print(d)
def cos():
    a=int(input("enter a number: "))
    d=math.cos(a)
    print(d)
def tan():
    a=int(input("enter a number: "))
    d=math.tan(a)
    print(d)
    
def sininv():
    a=int(input("enter a number: "))
    d=math.asin(a)
    print(d)
    
def cosinv():
    a=int(input("enter a number: "))
    d=math.acos(a)
    print(d)
    
def taninv():
    a=int(input("enter a number: "))
    d=math.atan(a)
    print(d)
    
def expon():
    a=int(input("enter base"))
    b=int(input("enter powerr"))
    print(a**b)
    
    
def log():
    a=int(input("enter a number : "))
    b=int(input("enter base"))
    print(math.log(a,b))
    
    
    
    
    
#drive code
print("1 for add , 2 for subtract , 3 for multiply , 4 for divide , 5 for floor division , 6 for modulus , 7 for sin , 8 for cos , 9 for tan , 10 for sininv , 11 for cosinv , 12 taninv,13 expon, 14 for log")
c=int(input("enter number: "))
if c==1:
    add()
elif c==2:
    sub()
elif c==3:
    mult()
elif c==4:
    div()
elif c==5:
    floor()
elif c==6:
    modulus()
elif c==7:
    sin()
elif c==8:
    cos()
elif c==9:
    tan()
elif c==10:
    sininv()
elif c==11:
    cosinv()
elif c==12:
    taninv()
elif c==13:
    expon()
elif c==14:
    log()
    
else:
    print("entered wrong number")

