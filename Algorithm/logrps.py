'''
    Logarithmic Random Poderated Selector Algorithm
'''

import random
import math

def logrps(objects: list):

    '''
        Logarithmic Random Poderated Selector:

        This algorithm gets a list of objects, and using
        a logarithmic scale, selects randomly one member
        of the list giving a higher probability weight to
        the initial objects of the list.

        This algorithm selects with more frecuency the
        initial members of the list, based on the
        logarithmic/exponential curve form.
    '''

    #* Amount of objects: "n":
    n = len(objects)

    #* Validation cases:
    #? When list is empty:
    if n == 0:
        return "List cannot be empty :c"
    #? When list has only one object:
    if n == 1:
        return objects[0]
    
    #* Throws a random float number based on the n objects:
    #? To operate the numbers, it will consider 1 as the
    #? first object; then when it selects an index of the
    #? list, it will take at 0-starting notation:
    #/ Random float between 1 and n with 4 decimals.
    #* This random represent a random point of selection
    #* in a linear axis in which all objects has the same
    #* space to be selected:
    randomLinearPoint = round(random.uniform(0, n), 4)
    # print(f"\nRandom Lineal Point: {randomLinearPoint}; ", end="")

    '''
    This is the propuse:

        * Having a linear scale between 1 - n, all the spaces
          between objects has the same size.
        
        * Having a logarithmic scale between 1 - n, the spaces
          between objects are different; the first object has
          the biggest space, the second is smaller, etc. The
          differences between the spaces is based on logarithms.

        * When the random is selected, you get the linear scale
          object; then it has to ponderate the space with the
          logarithmic scale, to select the equivalent.

        Example:
        NOTE: E1, E2, ..., E6 are the 6 objects of the list.

        LINEAR SCALE:
            E1      E2      E3      E4      E5      E6
        0       1       2       3       4       5       6
        |-------|-------|-------|-------|-------|-------|

        RANDOM POINT:
                                  *

        LOGARITHMIC SCALE:
                E1             E2        E3    E4   E5 E6
        0                1           2       3    4   5 6
        |----------------|-----------|-------|----|---|-|

        SELECTION:

            * Linear: 3.24: [E4];
            * Logarithmic: 3: [E2];
    
    '''

    #? The formula to calculate the distance between the start of
    #? the scale, and an "i" logarithmic point, is:
    #/ logPoint = n*log_n+1(i+1);
    #* So, it starts a loop to check if the random linear point is
    #* between the space of the first log point, or the second, or
    #* the third, etc.
    for i in range(2, (n+1)+1):
        # print((n+1) * math.log(i, n+1), end=" ")
        if randomLinearPoint <= (n * math.log(i, n+1)):
            #! Returns the selected object:
            # print(f"Logarithmic point: {i-1};")
            return objects[(i-1)-1]