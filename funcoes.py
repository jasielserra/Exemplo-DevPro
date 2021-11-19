import dis

def f():
    return 42

print(f())

def f(a,b,c='dC', *args):
    print(a,b,c, args)

f('A','B','C','D','E','F')

def funcao(a, b, c='dC', *args,x,y, **kwargs):
    print(a,b,c,x,y, args, kwargs)


funcao('A','B','C','D','E', x=1, y=2,z='Z',w='W')

def filter(**lookups):
    for k,v in lookups.items():
        print(k.split('__'),v)

filter(name__startswith='Hen', age__lt=30, city__endswith='roi')

def f(*args, **kwargs):
    print(args, kwargs)

t = 'A', 'B', 'C'
d = dict(z='Z', w='W')

print(t,d)
f(t[0],t[1],t[2], z=d['z'], w=d['w'])

def add(a,b):
    return a + b

def mult(a,b):
    return a * b

print(type(add))

print(add.__code__)

dis.dis(add)

print(add,2,3)

def calc(op,a,b):
    return op(a,b)


print(calc(add,3,4))
print(calc(mult,3,4))
