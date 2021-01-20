from decors import memoize
from functools import partial
import time

#first-class citizen

#Упаковка и распаковка параметров функции. Документирование.
def f1(*arg,**args):
    '''Документация'''
    print(arg,args)
    print(*arg,*args)
    ## ERROR print(**args)
    print(type(arg), type(args))
    a,b,c= args
    print(a,b)
    
    f2(*arg)
    f2(*args)
    f2(**args)
    
    f3(arg)


def f2(a,b,c):
    print('f3',a,b)

def f3(arg):
    d={}
    d[arg]=555
    print(d)
    print(arg)

##f1(1,2,a='11',b='22')

#####ЗАМЫКАНИЯ#######

def adder(a,b):
    print(locals())
    return a+b

def minuser(a,b):
    return a-b


def with_koef(k):
    def calc(func,*arg):
        return func(*arg) * k

    return calc

'''        
calc_with_koef = with_koef(3)
res=calc_with_koef(minuser,2,2)
'''

def multiplier( n ):    # замыкания - closure
    def mul( k ):
        return n * k
    return mul
 
mul3 = multiplier( 3 )

########
def mulPart( a, b,c,d ):    # частичное применение функции
    return a * b*c*d
 
par3 = partial( mulPart, 3 )




def применить_коеф2(k):
    count = 0
    def вычислить(func,*arg):
        nonlocal count 
        count=count+1
        print(locals())
        return func(*arg) * k, count

    return вычислить


#######МЕМОИЗАТОР#########
'''
def memoize(func):
    cache = dict()

    def memwrapper(*args):
        if args in cache:
            print('!!')
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memwrapper
'''    

def dec(f):
    def wrapp(a):
        print(1)
        print(time.time())
        f(a)
        print(2)
        print(time.time())

    return wrapp

def test(a):
    print("A",a)




######ДЕКОРАТОР#######
    
@memoize
def multiply(a,b):
    return a*b

