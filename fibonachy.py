def fibonachi(n):
 a=1
 b=1
 c= a+b
 if(b<n):
  return (fibonachi(c))
 
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

#print(fibonacci_recursive(7))

def fib(n):
   if(n==1 or n==2):
    return 1
   return fib(n-1) +fib(n-2)
   
print(fib(7)) 