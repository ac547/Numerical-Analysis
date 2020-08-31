# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 02:44:17 2020

@author: Castellano
"""


def bisect(f, a=int, b=int, tol=float, timed=False, verbose=False):
    """Basic Bisection Method For Finding The Root of a function.
    
    
    Parameters
    -------------
    function : 
        
        A function for which the root will be found
    
    a : int
    
        The beginning of an interval where we believe the root recides. 
    
    b : int
    
        The end of an interval where we believe the root recides.
    
    tol : float
    
        The minimum tolerance to which the root should be found.
        
    verbose : Boolean
    
        Should results be printed on each iteration.
        
    timed : Boolean

        Should the execution time be displayed.
    
    
    Returns 
    ---------
    root : float
    
        Approximate solution for the roof of function f.
        
        
    """
        
    import numpy as np
    from time import time
    
    start_time = time()
    
    if np.sign(f(a))*np.sign(f(b)) >= 0:
        
        raise Exception('Provide an initial interval [a,b] such that f(a)*f(b)<0. ')
        
    fa = f(a)
    fb = f(b)
    
    if verbose == True:
        
        s = "{} {} {} {} {} {} {}".format('|  k  ', 
                                      '|    ak    ',
                                      '|  f(ak)  ', 
                                      '|    ck    ', 
                                      '|  f(ck)  ', 
                                      '|    bk    ', 
                                      '|  f(bk)  ')
        print(s)
    
    k = 0
    
    while (b-a)/2 > tol:
        k += 1
        c = (a+b)/2
        fc = f(c)
        if fc == 0:
            break
        if np.sign(fc)*np.sign(fa) < 0:
            b , fb = c, fc
        else:
            a , fa = c, fc
        if verbose == True:
            
            s = "{0:4d} {1:12f} {2:7d} {3:15f} {4:6d} {5:14f} {6:7d}".format(int(k), 
                                      a,
                                      int(np.sign(fa)), 
                                      c, 
                                      int(np.sign(fc)), 
                                      b, 
                                      int(np.sign(fb)))
            print(s)
            
    xc = (a+b)/2 
    
    s = "{} {:6f}".format('The best estimate of the root is', xc)
    print(s)
    
    if timed == True:
        print(" Execution Took %s seconds ---" % (time() - start_time))
    
    root = xc
    return root

        