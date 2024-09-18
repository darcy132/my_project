def a():
    b()
def b():
    c()
    
def c():
    print( 1 / 0)
    
a() print('hello')
