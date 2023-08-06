SUMMARY = "Things I recode all the time : facotrial, combination, permutation, timethat, print_tb, print_nb"
__doc__ = SUMMARY

from math import factorial as _factorial, gamma as _gamma
import time

alls = ["factorial",
        "combination",
        "permutation",
        "timethat", #decorator
        "print_tb",
        "print_nb"]

def factorial(n):
    """Returns the factorial of n for all 'n' a real numbers.
    If complex numbers are used, the gamma function from spicy.special is used."""
    if type(n) == int and n>=0:
        return _factorial(n)
    elif isinstance(n,(float,int)):
        return _gamma(n+1)
    elif isinstance(n,complex) :
        try :
            import spicy.special as sp
            return sp.gamma(n+1)
        except ImportError:
            raise TypeError("n must be a real number")
    else :
        raise TypeError("n must be a number type")

def combination(n,p):
    """Returns the number of ways to choose p items from n items."""
    return factorial(n)/(factorial(p)*factorial(n-p))

def permutation(n,p):
    """Returns the number of ways to choose p items from n items in a specific order."""
    return factorial(n)/factorial(n-p)

def timethat(func):
    """Decorator to time a function's execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start} seconds")
        return result
    return wrapper

def print_tb(*tbs,between_tbs = "\n", sep=' ',end='\n',flush=False,file=None):
    """Prints nicely formatted array."""
    for tb in tbs:
        if isinstance(tb,(list,tuple,dict,set)):
            for line in tb:
                print(*line, sep=sep,end=end,flush=False,file=file)
        else : # assume it's a not a list or tuple or dict or set
            print(tb,end="",sep="",flush=False,file=file)
        print(between_tbs,end="",sep="",flush=False,file=file)
    return None

lookup_dir = {"00":"U","01":"L","10":"R","11":"D"}
lookup_dir_arr = {"00":"↑","01":"←","10":"→","11":"↓"}
lookup_up = ["U","↑"]
lookup_left = ["L","←"]
lookup_right = ["R","→"]
lookup_down = ["D","↓"]

def shrink(tb:list,char=""):
    """Returns a list of strings that are the result of removing the borders of the table tb."""
    res = []
    for i in range(len(tb)):
        if tb[i].count(char) != len(tb[i]):
            res.append(tb[i])
    min_ind = len(res[0])+1
    max_ind = 0
    for j in range(len(res)):
        for k in range(len(res[j])):
            if res[j][k]!=char:
                if k < min_ind :
                    min_ind=k
                break
        for k in range(len(res[j])-1,0,-1):
            if res[j][k]!=char:
                if k > max_ind :
                    max_ind= k
                break
    final = []
    for m in range(len(res)):
        final.append(res[m][min_ind:max_ind])
    return final




def print_nb(n:int,mode="arr",/ , verbose=False):
    """Still in development. And not working yet.
    Prints the number n in the notation of the number of blocks.
    mode is either "arr" or "str" for arrow or string.
    """
    work:str = bin(n)[2:]
    if len(work)%2 == 1: # missing 0 to to 00 = up or 01 = left 
        work = "0"+work
    res = ""
    if mode == "arr":
        for i in range(len(work)//2):
            res += lookup_dir_arr[work[i:i+2]]
    else  :
        for i in range(len(work)//2):
            res += lookup_dir[work[i:i+2]]
    print(res) 
    #print(res,"    ",work)
    env = [[""]*2*len(res) for i in range(2*len(res))]
    #print_tb(env)
    curr_i = len(res)
    curr_j = len(res)

    for i in range(len(res)):
        if env[curr_i][curr_j] == "": 
            env[curr_i][curr_j]= res[i]
            print(res[i],end=" ")
        else :
            print("That polyomino doesn't exist")
            return -1
        if res[i] in lookup_up : 
            curr_j+=1
        elif res[i] in lookup_down:
            curr_j-=1
        elif res[i] in lookup_right:
            curr_i+=1
        elif res[i] in lookup_left:
            curr_i-=1
        else:
            print("whatcha got here dude:",res[i])
    # need shrink empty spaces now
    new = shrink(env)
    if verbose : print_tb(new,env)

    env = [[""]*2*len(res) for i in range(2*len(res))]
    #print_tb(env)
    curr_i = len(res)
    curr_j = len(res)
    env[curr_i][curr_j]="0"
    #env = shrink(env)
    print(res)
    print_tb(env)
    return new # return the polyomino
