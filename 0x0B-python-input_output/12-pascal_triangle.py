#!/usr/bin/python3

"""
1. Create an empty list triangle (pascal) to store the rows of the triangle.
2. Loop through each line from 1 to n+1
   (where n is the number of rows the triangle should have).
3. Initialize a variable N to 1 for each line.
4. Create an empty list pascal to store the values of each line.
5. Loop through each number in the line from 1 to line + 1.
6. Append the value of N to the pascal.
7. Update the value of N using the formula N = N * (line - i) / i.
8. After the inner loop, append the pascal to the triangle list.
9. Repeat the process for each line.
10. Return the triangle list.
"""


def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return []
    for line in range(1, n+1):
        N = 1
        pascal = []
        for i in range(1, line+1):
            pascal.append(N)
            N = N * (line - i) // i
        triangle.append(pascal)
    return triangle
