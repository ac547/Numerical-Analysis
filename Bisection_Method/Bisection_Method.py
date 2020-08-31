# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 05:51:34 2020

@author: Castellano
"""

class Bisection_Method(object):
    """Bisection Method for Finding Roots of a function.
    
    
    Parameters
    -------------
    function : 
        
        A function for which the root will be found
    
    a : int

        The beginning of an interval where we believe the root recides. 
    
    b : int
    
        The end of an interval where we believe the root recides.
    
    

    """
    
    def __init__(self, function, a=int, b=int):
        self.f = function
        self.a = a
        self.b = b
        
        
        
        
    def bisect(self, timed=False, verbose=False, tol=.001):
        """Bisect For Finding The Root of a function.
        

        
        verbose : Boolean
    
            Should results be printed on each iteration.
        
        timed : Boolean

            Should the execution time be displayed.
        
        tol : float
        
            The minimum tolerance to which the root should be found.
    
    
        Returns 
        ---------
        root : float
    
            Approximate solution for the roof of function f.
        
    
        """ 
        
        import numpy as np
        from time import time
    
        start_time = time()
    
        if np.sign(self.f(self.a))*np.sign(self.f(self.b)) >= 0:
        
            raise Exception('Provide an initial interval [a,b] such that f(a)*f(b)<0. ')
        
        fa = self.f(self.a)
        fb = self.f(self.b)
    
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
    
        while (self.b-self.a)/2 > tol:
            k += 1
            c = (self.a + self.b)/2
            fc = self.f(c)
            if fc == 0:
                break
            if np.sign(fc)*np.sign(fa) < 0:
                self.b , fb = c, fc
            else:
                self.a , fa = c, fc
                if verbose == True:
            
                    s = "{0:4d} {1:12f} {2:7d} {3:15f} {4:6d} {5:14f} {6:7d}".format(int(k), 
                                                                                     self.a,
                                                                                     int(np.sign(fa)), 
                                                                                     c, 
                                                                                     int(np.sign(fc)), 
                                                                                     self.b, 
                                                                                     int(np.sign(fb)))
                    print(s)
            
            xc = (self.a + self.b)/2 
    
        s = "{} {:6f}".format('The best estimate of the root is', xc)
        print(s)
    
        if timed == True:
            print(" Execution Took %s seconds ---" % (time() - start_time))
    
        root = xc
        return root
        
    def n_iter(self, tol=.001):
        """Calculates number of iteration for Bisection Method.
    
    
        Parameters
        -------------
    
    
        tol : float
    
            The minimum tolerance to which the root should be found.
        
   
    
        Returns 
        ---------
        n : float
    
            Approximate number of iterations required to find the root of function.
        
        
        """
        
    
        from math import log
    
        n = (log((self.b-self.a)/abs(tol))/log(2))
        
        return print(n, "Iterations \n")

