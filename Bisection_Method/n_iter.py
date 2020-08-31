# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 04:43:26 2020

@author: Castellano
"""

def n_iter(a=int, b=int, tol=float):
    """Calculates number of iteration for Bisection Method.
    
    
    Parameters
    -------------
    
    a : int
    
        The beginning of an interval where we believe the root recides. 
    
    b : int
    
        The end of an interval where we believe the root recides.
    
    tol : float
    
        The minimum tolerance to which the root should be found.
        
   
    
    Returns 
    ---------
    n : float
    
        Approximate number of iterations required to find the root of function.
        
        
    """
    
    
    from math import log
    
    n = (log((b-a)/abs(tol))/log(2))
    return n
