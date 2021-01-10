import math
def nearest_square(n):
    try:
        lim=int(math.pow(n,0.5))
        return(int(math.pow(lim,2)))
    except ValueError:
        return(0)




