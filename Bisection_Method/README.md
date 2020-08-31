# Bisection_Method

This is class for creating objects representing a mathematical function f, on an interval [a,b]


There are two methods within the class, the bisect, and n_iter return the approximate root on the interval and the number of iterations required respectively. 

# How to Use

define a mathematical function for which the root must be found

  > def f(x): x + 1
  
Initialize the bisection method for this function by providing the function and the interval [a,b] where you know the root resides.

  > my_bisection = Bisection_Method(f, a=int, b=int)
  
Access each method by providing a tolerance and in the case of the bisect method, some optional functionality.

  > my_bisection.bisect(False, True, tol=10**-9)
  > my_bisect.n_iter(tol=.001)
  
  
  # Sources 
  
    https://www.youtube.com/watch?v=MlP_W-obuNg
