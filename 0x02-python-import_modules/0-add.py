#!/usr/bin/python3
if name == "main":
    from add_0 import add
# Change the values of a and b here
    a = 1
    b = 2
# Print the sum of a and b
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
