x=10
a=12
b=18

def sum_func():
    return a+b

# print(sum_func())


def func():
    y=50
    global x
    x+=10
    print(x)

# func()
# print(f'The value of x after the function is: {x}')


def weird_func():
    z=100
    if True:
        z+=50
    print (z)

weird_func()