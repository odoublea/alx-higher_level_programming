#!/usr/bin/python3

"""
1. Create an empty list triangle (pascal) to store the rows of the triangle.
2. Loop through each line from 1 to n+1
   (where n is the number of rows the triangle should have).
3. Initialize a variable C to 1 to keep track of the current value.
4. Create an empty list pascal to store the values of each line.
5. Loop through each number in the line from 1 to line + 1.
6. Append the value of C to the pascal.
7. Update the value of C using the formula C = C * (line - i) / i.
8. After the inner loop, append the pascal to the triangle list.
9. Repeat the process for each line.
10. Return the triangle list.
"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    Arg:
        n(int): size of the triangle
    """
    if n <= 0:
        return []

    triangle = []
    for line in range(1, n+1):
        pascal = []
        C = 1
        for i in range(1, line+1):
            pascal.append(C)
            C = C * (line - i) // i
        triangle.append(pascal)
    return triangle
