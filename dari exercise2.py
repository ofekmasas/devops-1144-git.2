# exercise 1
def greet(name='Guest'):
    return(f'hello {name}')

# exercise 2
def sum(x,y):
    return x+y
# exercise 4
def recurse_factorial(n):
    if(n<0):
        return('invalid input!')
    if(n==0 or n==1):
        return 1
    return n*recurse_factorial(n-1)

def loop_factorial(n):
    if(n<0):
        return('invalid input!')
    if(n==0 or n==1):
        return 1
    sum=1
    for i in range(1,n+1):
        sum*= i
    return sum


# print(loop_factorial(3))
# print(greet())
# print(sum(12,-18))

# exercise 5
def double_list(lst):
    newlist=[]
    k=0
    for i in range(1,len(lst)+1):
        newlist.append(lst[k]*2)
        k+=1
    return newlist






def double_list_good(lst):
    double=[i*2 for i in lst]
    return double


print(double_list_good([1,2,3,4,5,20,50]))