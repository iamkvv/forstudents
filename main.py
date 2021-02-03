from decors import control_input,memoize1,logger


@control_input
def InPut(message):
    return input(f"Введите {message} число: ")

@logger
@memoize1
def Calc(n1,n2,sign):
    if sign == "+":   return n1+n2
    elif sign == "-": return n1-n2
    elif sign == "/": return n1/n2
    elif sign == "*": return n1*n2
    else: raise ValueError        

def InPuts():
    n1 = InPut("first")
    n2 = InPut("second")
    print(n1,n2)
    return n1,n2,"+"

def runCalc():
    r = InPuts()
    r2 = Calc(*r)
    
    print(r2)

    cont = input("Продолжить? (Y/n)")
    if cont.lower() == "y" or not cont :
        runCalc()

 
if __name__ == "__main__":
    runCalc()
