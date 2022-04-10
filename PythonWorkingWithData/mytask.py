b=1
def addition():
    global b
    print(b)
    b=b+1
    if b<101:
        addition()
addition()    


    
    
