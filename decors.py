'''
>>> a, b, c = map(int, input("vvod ").split())
vvod 3 4 5
http://egoroffartem.pythonanywhere.com/course/python/funktsiya-input
'''
import functools

def control_input(func):
    def wrapper(*args):
        try:
            res=float(func(*args))
            return res
        except Exception as e:
            ##print(e,dir(e), type(e))
            print("Введено некорректное значение. " + str(e) )
            wrapper(*args)
            
    return wrapper

def controlInput(**kwargs):
    def inner(func):
        def wrapper():
            func()
        return wrapper
    return inner


def flog(func):
    print('flog',func.__name__)

    def wrapper(*nums):
        res= func(*nums)
        print('res', res)
        with open ("log.txt","a") as f:
            if res[1]:
                f.write(str(res[0])+ " memo " + "\n")
            else:
                f.write(str(res[0]) + "\n")

        return res
    return wrapper

def dec_args(fname):
    print(0,'dec_args')
    def dec(func):
        print(0,'dec')
        def wrapper(*nums):
            print(0,'wrapper')
            res= func(*nums)
            print('res', res, fname)
            with open (fname,"a") as f:
                '''
                if res[1]:
                    f.write(str(res[0])+ " memo " + "\n")
                else:
                    f.write(str(res[0]) + "\n")
                '''    
                f.write(str(res)+"\n") 
            return res
        return wrapper
    return dec



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

def memoize2(func):
    cache = dict()
    print('2',func.__name__)
    def memwrapper(*args2):
        print('second',args2,func.__name__)
        if args2 in cache:
            print('??')
            return cache[args2]
        result = func(*args2)
        cache[args2] = result
        return result

    return memwrapper

################
def dec_par(**kwargs):
    print('dec_par ', kwargs)
    def inner(func):
        print('dec_par inner ', func,  kwargs)
        def wrapper(*args):
            print(*args,*kwargs)
            func(*args)
        return wrapper
    return inner    


################


def multi(f_py=None, factor=2):
    #assert callable(f_py) or f_py is None
    print('multi',f_py)
    def _decorator(func):
        print('multi _decorator',func)
        #@functools.wraps(func)
        def wrapper(*args, **kwargs):
            return factor * func(*args, **kwargs)
        return wrapper
    return _decorator(f_py) if callable(f_py) else _decorator

def multi_new(f_py=None, factor=2):
    print('multi',f_py)
    def _decorator(func):
        print('multi _decorator',func)
        
        def wrapper(*args, **kwargs):
            return factor * func(*args, **kwargs)
        return wrapper
    
    return _decorator(f_py) 
