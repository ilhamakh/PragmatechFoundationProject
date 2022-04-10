ilkeded=1
araeded=ilkeded
def artir():
    global araeded
    print(araeded)
    araeded=araeded+1
    if araeded<10:
        artir()
artir()    


    
    
