# Last Modified: 09/28/26
# By Ab Mosca
#
# Demo of boolean operations 


def main():

    # Set up Booleans 
    is_raining = True
    is_wet = True
    is_sunny = False
    is_hot = False

    print("Value of is_raining:", is_raining)
    print("Value of is_wet:", is_wet)
    print("Value of is_sunny:", is_sunny)
    print("Value of is_hot:", is_hot)

    ##############
    # not Operator
    ##############
    print("Value of not is_raining:", not is_raining)
    print("Value of not is_wet:", not is_wet)
    print("Value of not is_sunny:", not is_sunny)
    print("Value of not is_hot:", not is_hot)

    # What does the not operator do? 

    ##############
    # and Operator
    ##############
    
    print("Value of is_raining and is_wet:", is_raining and is_wet)
    print("Value of is_raining and is_sunny:", is_raining and is_sunny)
    print("Value of is_sunny and is_hot:", is_sunny and is_hot)
    print("Value of is_sunny and is_wet:", is_sunny and is_wet)

    # What does the and operator do?
    """only gives a true answer when both are true"""

    #############
    # or operator
    #############
    print("Value of is_raining or is_wet:", is_raining or is_wet)
    print("Value of is_raining or is_sunny:", is_raining or is_sunny)
    print("Value of is_sunny or is_hot:", is_sunny or is_hot)
    print("Value of is_sunny or is_wet:", is_sunny or is_wet)

    # What does the or operator do?
"""one has to be true"""

    ############
    # YOUR TURN!
    ############
    # Try out the != operator
    print("Value of is_raining != is_wet:", is_raining != is_wet)
    print("Value of is_raining != is_sunny:", is_raining != is_sunny)
    print("Value of is_sunny != is_hot:", is_sunny != is_hot)
    print("Value of is_sunny != is_wet:", is_sunny != is_wet)
    
    # What does it do?
    '''one can be true, cant be true at the same time'''
    
    
    #indentation tells python that code is contained within the block
    
    



if __name__ == '__main__':
    main()