
#first-class citizen

#Упаковка и распаковка параметров функции. Документирование.
def f1(*arg: int,**args: str) -> tuple:
    '''Документация'''
    print(arg,args)
    print(*arg,*args)
    ## ERROR print(**args)
    print(type(arg), type(args))

    f2(*arg)
    f2(*args)
    f2(**args)


def f2(a,b):
    print('f3',a,b)

##f1(1,2,a='11',b='22')

#####ЗАМЫКАНИЯ#######

def adder(a,b):
    return a+b

def minuser(a,b):
    return a-b


def применить_коеф(k):
    def вычислить(func,*arg):
        return func(*arg) * k

    return вычислить
        
## рез_коеф=применить_коеф(3)
## рез_коеф(minuser,2,2)
    
def применить_коеф2(k):
    count = 0
    def вычислить(func,*arg):
        nonlocal count
        count=count+1
        return func(*arg) * k, count

    return вычислить


#######МЕМОИЗАТОР#########
def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            print('!!')
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func
    

######ДЕКОРАТОР#######
    
@memoize
def multiply(a,b):
    return a*b

## https://tirinox.ru/python-decorators/
