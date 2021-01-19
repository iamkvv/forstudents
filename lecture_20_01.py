from decors import memoize
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
    a=99
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

def применить_коеф2(k):
    count = 0
    def вычислить(func,*arg):
        #nonlocal count 
        count=count+1
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

######ДЕКОРАТОР#######
    
@memoize
def multiply(a,b):
    return a*b

