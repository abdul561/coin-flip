import random


def coinflips(n):
    Heads = 0
    Tails = 0 
    
    for x in range(n):
        x = random.choice(['h','t'])
        if x == 'h':
            Heads +=1 
        else :
            Tails +=1 
            
            
            
    return f" Heads : {Heads} and Tails : {Tails}"
