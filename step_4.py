import numpy as np

def intersection_numpy(list1,list2):
    """Find the overalapping values of two lists.

    Makes use of the NumPy library to find the intersection of 
    the lists. 

    Parameters
    ----------
    list1 (array_like) : First list 
    list2 (array_like) : Second list

    Returns
    -------
    A numpy.ndarray datatype containing the common elements of the lists

    Note
    ----
    NumPy is not a part of the Python Standard Library,so
    it must be installed separately using Pip before using it in your code.
    Deatiled instrucions for installing NumPy can be found at: https://numpy.org/install/
    """
    return(np.intersect1d(list1, list2, assume_unique=False))

def intersection_datatype(list1, list2):
    """Find the overlapping values of two lists.

    Makes use of Python's datastructure, sets to find intersection of the 
    lists.

    Parameters
    ----------
    list1 (array_like) : First list 
    list2 (array_like) : Second list

    Returns
    -------
    A set datatype containing the common elements of the lists
    """
    return(set(list1)&set(list2))

A=[1,2,3,4,5,6,7,8,9,10]
B=[2,4,6,12]
C=intersection_numpy(A,B)
D=intersection_datatype(A,B)
print(f"The function 'intersection_numpy' returns a {type(C)} containing the common elements of the lists {A} and {B}:\n")
print(C,'\n')
print(f"The function 'intersection_datatype' returns a {type(D)} containing the common elements of the lists {A} and {B}:\n")
print(D)




