import math

def summ(lst):
    if len(lst)==0:
        return 0 
    else:
        return lst[0] + summ(lst[1:]) 

    

def fact(num,a):
    print(locals())
    if num==1:
        return 1
    else:
        x=num
        return num*fact(num-1,x)


def rev(lst, i=0):
    print(lst)
    if i==len(lst)//2:
        return lst
    lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i] 
    return  rev(lst,i+1)


def tt(a=1,*args,**kargs):
    print(args,kargs)
