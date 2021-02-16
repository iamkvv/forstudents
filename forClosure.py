g=3
def outer(a):
    l=4
    def getLoc():
        return l
    #if a: !!!
    def inner(b):
        global g
        nonlocal l
        g+=1
        l+=1
        print(locals())
        return (a+b)*g+l
    
    inner.GetLocal= getLoc
    return inner

x= outer(5)
plus_6 = outer(6)
del outer
v= x.GetLocal()
print(v)

#print(x.__name__)
#print(x.__closure__[0].cell_contents)


