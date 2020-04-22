# create function for Fibonacci series   
def fibonacci(n):
    if n > 1:
        return fibonacci(n-2) + fibonacci(n-1)
    return n

# create function for Lucas series   
def lucas(n):
    n1 = 2 #lucas default fist value 
    n2 = 1 #lucas default second value  
    
    if n == 1:   
        return n1 # lucas fist value 
        
    if n == 2:  
        return n2 # lucas second value 
    #sum the series value till the number of times given in parameter    
    #since we know first two values lets us do this sum till n-2 times
    if n > 2:
        x = n-2
        while x != 0:
            n3 = n1+n2
            n1 = n2
            n2 = n3 
            x  = x-1        
        return n3

# create function for sum series   
def sum_series(n,a,b):
    # when function called with 0,1 values call Fibonacci function
    if a == 0 and b == 1:
        return fibonacci(n)
    # when function called with 2,1 values call lucas function
    
    if a == 2 and b == 1:
        return lucas(n)    
    #else form new series
    #the series value till the number of times given in parameter    
    #since we know first two values lets us do this sum till n-2 times
       
    else:
        n1 = a  
        n2 = b   
        
        if n == 1:   
            return n1
        
        if n == 2:   
            return n2
        
        if n >= 2:
            x = n-2
            while x != 0:
                n3 = n1+n2
                n1 = n2
                n2 = n3 
                x  = x-1        
            return n3
          

