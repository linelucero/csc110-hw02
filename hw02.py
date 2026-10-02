# ------------------------------------------------------
#        Name: Aline Valenzuela-Lucero
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    # ADD a Docstring for this function
    """Here we want to input from user, values for x and y and print them"""
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    x = int(input("give me x: "))
    
    y = int(input("give me y: "))
    
    return x,y


# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(x, y):
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    c = ( x*y )
    print("mult result:" ,c)
    
    d = ( x+y )
    print("add result:" ,d)
    
    xy_multadd = c/d
    return xy_multadd

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(x, y, xy_multadd):
    # ADD a Docstring for this function
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


def main ():
    # ADD a Docstring for this function
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    # TODO: add your call instead of this line
    x,y = read_two_ints()
    
    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd
    xy_multadd = compute_multadd(x,y)
    # TODO: add your call instead of this line

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;
    print_fancy(x, y, xy_multadd)
    # TODO: add your call instead of this line


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
