# implement the following matrix operations
# The description of these operations can be found in BasicMatrixOperation.pdf
# Write the number of iterations that each operation will take right above the function definition
# Write down more test cases in test_suit.txt
# Follow the same template has been provided in the test_suit.txt
# Make sure you have at least one test case for each possible case
# for developing accurate test cases you can use https://matrix.reshish.com/add&sub.php
# number of iterations: ??
def add(M1, M2):
    # Check if M1 and M2 are compatible for addition
    pass

# number of iterations: ??
def subtract(M1, M2):
    # Check if M1 and M2 are compatible for subtraction
    pass


# number of iterations in case one of the M1, and M2 is constant: ??
# number of iterations in case both M1 and M2 are two dimensional lists: ??
def multiply(M1, M2):
    # perform multiplication by a constant if one of the M1 and M2 is a constant (not a list) and the other is a matrix
    # (i.e. a two dimension list)

    # perform matrix multiplication if both M1 and M2 are matrix i.e. a two dimension list
    # make sure you check if M1 and M2 are compatible for multiplication

    # raise an exception if M1 and M2 were not suitable for any of the above operations
    pass

# number of iterations: ??
def transpose(M):
    # return transpose of M
    pass


# number of iterations: ??
def is_equal(M1, M2):
    # compares elements of M1 and M2 if they are two dimensional lists, and returns False if any
    # of the element dont match, otherwise returns True
    pass

# Read the following restriction
# MAKE SURE YOU DO NOT USE MORE THAN LINEAR SPACE 
# IN OTHER WORDS YOU CANT CREATE A NEW MATRIC OF THE SAME SIZE OF THE INPUT
# number of iterations: ??
def zero_matrix(M):
    # if an element in an MxN matrix is 0, its entire row and column are set to 0.
    # write 5 test cases for this if you opt to implement it
    # Example1:
    #      input: [[1,1,1],[1,0,1],[1,1,1]]
    #      output: [[1,0,1],[0,0,0],[1,0,1]]
    # Example2:
    #      input:  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    #      output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    # returns the zeroed matrix
    pass

# For local testing and debugging
if __name__ == "__main__":
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    sum = [[10, 10, 10], [10, 10, 10], [10, 10, 10]] # m1+m2
    difference12 = [[-8, -6, -4], [-2, 0, 2], [4, 6, 8]] # m1-m2
    difference21 = [[8, 6, 4], [2, 0, -2], [-4, -6, -8]] # m2-m1
    product12 = [[30, 24, 28], [84, 69, 54], [138, 114, 90]] # m1*m2
    product21 = [[90, 114, 138], [54, 69, 84], [18, 24, 30]] # m2*m1
    transposem1 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]] # transpose of m1
    constantproduct = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]  # multiplying m1 by 2

    if is_equal(m1, m1):
        print("is_equal passed the test")
    else:
        print("is_equal failed the test")

    if is_equal(transpose(m1), transposem1):
        print("transpose passed the test")
    else:
        print("transpose failed the test")

    if is_equal(add(m1, m2), sum):
        print("add passed the test")
    else:
        print("add failed the test")

    if is_equal(subtract(m1, m2), difference12):
        print("subtract passed the test")
    else:
        print("subtract failed the test")

    if is_equal(subtract(m2, m1), difference21):
        print("subtract reverse passed the test")
    else:
        print("subtract reverse failed the test")

    if is_equal(multiply(m1, 2), constantproduct):
        print("scalar multiplication passed the test")
    else:
        print("scalar multiplication failed the test")

    if is_equal(multiply(m1, m2), product12):
        print("matrix multiplication passed the test")
    else:
        print("matrix multiplication failed the test")

    if is_equal(multiply(m2, m1), product21):
        print("reverse matrix multiplication passed the test")
    else:
        print("reverse matrix multiplication failed the test")
        
    ZeroMatrixInput = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    ZeroMatrixOutput= [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    
    if is_equal(zero_matrix(ZeroMatrixInput), ZeroMatrixOutput):
        print("zero_matrix passed the test")
    else:
        print("zero_matrix failed the test")
