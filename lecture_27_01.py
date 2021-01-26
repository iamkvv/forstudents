'''
a=1

def f1():
    global a #!!!
    a=a+1

f1()
print(a)

####################

def f2(a):
    def f3():
        return a*10

    return f3

x = f2(50)

del f2 ##!!!
print(x) ## x is function
r= x()
'''



def calc_decor1(func):
    print('calc_decor1', func.__name__)
    counter=0
    def wrapper1(*args):
        nonlocal counter
        counter=counter+1
        print('start - 1', counter)
        
        res = func(*args)
        print('end')
        return res
    return wrapper1    

def calc_decor2(func):
    print('calc_decor2', func.__name__) ##!!!
    counter=0
    def wrapper2(*args):
        nonlocal counter
        counter=counter+1
        print('start - 2', counter)
        
        res = func(*args)
        print('end')
        return res
    return wrapper2
'''
d = calc_decor(adder)
res = d(2,2)
'''

@calc_decor1
@calc_decor2
def adder(n1, n2):
    return n1 + n2

print(adder.__name__)


def f5(n):
    return n * 2

res5 = f5(f5(f5(2)))

###########

def memoize1(func):
    cache = dict()
    print('memo',func.__name__)
    def memwrapper(*args1):
        print('first',args1,func.__name__)
        if args1 in cache:
            print('!!')
            return cache[args1],True
        result = func(*args1)
        cache[args1] = result
        return result,False

    return memwrapper


