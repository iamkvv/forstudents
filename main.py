from decors import control_input,memoize1,logger
import sys
import importlib
import time
import timeit

'''
    OPERATORS = {
        '+': float.__add__, 
        '-': float.__sub__,
        '*': float.__mul__,
        '/': float.__truediv__,
        '%': float.__mod__,
        '^': float.__pow__,
    }
'''
#OPERATORS[sign](n1,n2)

@control_input
def InPut(message):
    return input(f"Введите {message} число: ")

@logger
@memoize1
def Calc(n1,n2,sign):
    s1 = time.perf_counter_ns() 
    OPERATORS = {
        '+': float.__add__, 
        '-': float.__sub__,
        '*': float.__mul__,
        '/': float.__truediv__,
        '%': float.__mod__,
        '^': float.__pow__,
    }
    res=OPERATORS[sign](n1,n2)
    f1 = time.perf_counter_ns()
    print('opers',f1 - s1)
    
    s1 = time.perf_counter_ns()
    LambdaOpers = {
        '+': lambda n1,n2: n1+2, 
        '-': lambda n1,n2: n1-2,
        '*': lambda n1,n2: n1*2,
        '/': lambda n1,n2: n1/2,
        #'%': lambda n1,n2: n1/2,
        #'^': lambda n1,n2: n1**2
    }
    res=LambdaOpers[sign](n1,n2)
    f1 = time.perf_counter_ns()
    print('lamdbaopers',f1 - s1)
    
   
    f1=time.perf_counter_ns()
   
    #return OPERATORS[sign](n1,n2)
    s = time.perf_counter_ns()
    
    res=None
    if sign == "+":   res = n1+n2
    elif sign == "-": res = n1-n2
    elif sign == "/": res = n1/n2
    elif sign == "*":  res = n1*n2
    else: raise ValueError
    
    f=time.perf_counter_ns()  #timeit.default_timer()

    print('IF-opers',f-s )
    
    return res

    
def InPuts():

        n1 = InPut("first")
        n2 = InPut("second")
        print(n1,n2)
        return n1,n2,"+"
 
        

def runCalc():
    res_input = InPuts()
    res_calc = Calc(*res_input)
    
    print(round(res_calc[0],3))

    cont = input("Продолжить? (Y/n)")
    if cont.lower() == "y" or not cont :
        # print(type(Calc.__closure__))
        
        print(Calc.__closure__[0].cell_contents.GetCache())
        runCalc()

 
if __name__ == "__main__":
    runCalc()
    
    #for arg in sys.argv:
    #    print(arg)


    #for mod in sys.modules.values():
     #   print(mod)

##importlib.reload(sys.modules[__name__])
