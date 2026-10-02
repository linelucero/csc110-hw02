# ------------------------------------------------------
#        Name: Aline Valenzuela-Lucero
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    # ADD a Docstring for this function
    """This function takes user input for x and y values"""
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    x = int(input("give me x: "))
    
    y = int(input("give me y: "))
    #input values for x and y
    
    return x,y


# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(x, y):
    # ADD a Docstring for this function
    '''This function computes arithmetic with x and y, (x*y)/(x+y) and inserts it into xy_multadd variable'''
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    c = ( x*y )
    print("mult result:" ,c)
    #set x*y to c and print the value to mult result
    
    d = ( x+y )
    print("add result:" ,d)
    #set x+y to d and print the value to add result
    
    xy_multadd = c/d
    return xy_multadd
    #set the division of c and d to xy_multadd 

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(x, y, xy_multadd):
    # ADD a Docstring for this function
    """This function prints the results for x, y, and the multadd operation in an organized manner under 16 * and over  16 ="""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    el_string = "*"*16
    otro_string = "="*16
    print(el_string)
    print("RESULTS:")
    print("first number:", x)
    print("second number:", y)
    print("multadd result:", xy_multadd)
    print(otro_string)
    #organize all the variables under a organized print.


def main ():
    # ADD a Docstring for this function
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    x,y = read_two_ints()
    # call the values for x and y
    
    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd
    xy_multadd = compute_multadd(x,y)
    #call xy_multadd operation

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;
    print_fancy(x, y, xy_multadd)
    # call the fancy print


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
