# implement the following matrix operations
# The description of these operations can be found in BasicMatrixOperation.pdf
# Write the number of iterations that each operation will take right above the function definition
# Write down more test cases in test_suit.txt
# Follow the same template has been provided in the test_suit.txt
# Make sure you have at least one test case for each possible case
# for developing accurate test cases you can use https://matrix.reshish.com/add&sub.php

# number of iterations: rowM1 * colM1
def add(M1, M2):
    # Check if M1 and M2 are compatible for addition by checking if matrices are the same size
    rowM1 = len(M1) #number of rows in the array
    colM1 = len(M1[0]) #number of elements in the row (columns)
# Calculates the number of rows and columns in M1 and stores it in these variables
    rowM2 = len(M2)
    colM2 = len(M2[0])
    # Calculates the number of rows and columns in M1 and stores it in these variables

    if (rowM1 != rowM2 or colM1 != colM2):
        print("M1 and M2 are not compatible for addition")
        return False

    if rowM1 == rowM2 and colM1 == colM2:
        M3= [[0] * colM1 for i in range(rowM1)] #creates new matrix to store new values after adding the matrices
        for j in range(len(M1[0])):
            for i in range(len(M1)):
                result = M1[i][j] + M2[i][j]  #adds the matrices together
                M3[i][j]= result  #puts the sum into new matrix
        return M3

    raise Exception(TypeError)

# number of iterations: rowM1 * colM1
def subtract(M1, M2):
    rowM1 = len(M1)  # number of rows in the array
    colM1 = len(M1[0])  # number of elements in the row (columns)
    # Calculates the number of rows and columns in M1 and stores it in these variables
    rowM2 = len(M2)
    colM2 = len(M2[0])
    # Calculates the number of rows and columns in M1 and stores it in these variables

    if (rowM1 != rowM2 or colM1 != colM2):
        print("M1 and M2 are not compatible for addition")

    if rowM1 == rowM2 and colM1 == colM2:
        M3 = [[0] * colM1 for i in range(rowM1)]  #creates new matrix to store new values after subtracting the matrices
        for j in range(len(M1[0])):
            for i in range(len(M1)):
                result = M1[i][j] - M2[i][j] #subtracts the matrices
                M3[i][j] = result  #puts the difference into new matrix
        return M3
    raise Exception(TypeError)


# number of iterations in case one of the M1, and M2 is constant: rows * columns
# number of iterations in case both M1 and M2 are two dimensional lists: colM2*rowM1*colM1
def multiply(M1, M2):
    if isinstance(M1,int) or isinstance(M1,float): #if M1 is the constant
        rowM2= len(M2)
        colM2= len(M2[0])
        M3 = [[0] * colM2 for i in range(rowM2)]

        for j in range(len(M2[0])):
            for i in range(len(M2)):
                result = M1 * M2[i][j]  #multiplies the constant by the matrix
                M3[i][j] = result
        return M3

    if isinstance(M2, int) or isinstance(M2, float):  #if M2 is the constant
        rowM1 = len(M1)
        colM1 = len(M1[0])
        M3 = [[0] * colM1 for i in range(rowM1)]

        for j in range(len(M1[0])):
            for i in range(len(M1)):
                result = M2 * M1[i][j]
                M3[i][j] = result
        return M3
    rowM1 = len(M1)  # number of rows in the array
    colM1 = len(M1[0])  # number of elements in the row
    # Calculates the number of rows and columns in M1 and stores it in these variables
    rowM2 = len(M2)
    colM2 = len(M2[0])
    if colM1 == rowM2:       #in order to multiply matrices the number of columns in M1 has to be equal to the number of rows in M2
        M3= [[0] * colM2 for i in range(rowM1)]
        for j in range(len(M3[0])):
            for i in range(len(M3)):
                result=0  #stores the sum of the values being multiplied for the new matrix
                for k in range (colM1):
                    result= result+ M1[i][k]*M2[k][j]
                M3[i][j]= result
        return M3

    # perform multiplication by a constant if one of the M1 and M2 is a constant (not a list) and the other is a matrix
    # (i.e. a two dimension list)
    raise Exception(TypeError)
    # perform matrix multiplication if both M1 and M2 are matrix i.e. a two dimension list
    # make sure you check if M1 and M2 are compatible for multiplication

    # raise an exception if M1 and M2 were not suitable for any of the above operations
    pass

# number of iterations: columns * rows
def transpose(M):
    rowM = len(M)  # number of rows in the array
    colM = len(M[0]) #number of elements in the row (columns)
    M2= [[0] * rowM for i in range(colM)]
    for j in range(len(M)):
        for i in range(len(M[j])):
            M2[i][j] = M[j][i]  #interchanges the rows and columns
    return M2

    # return transpose of M
    pass


# number of iterations: rows * columns
def is_equal(M1, M2):
    rowM1 = len(M1)  # number of rows in the array
    colM1 = len(M1[0])  # number of elements in the row
    # Calculates the number of rows and columns in M1 and stores it in these variables
    rowM2 = len(M2)
    colM2 = len(M2[0])
    # Calculates the number of rows and columns in M1 and stores it in these variables
    if [isinstance(M1, int) or isinstance(M1, float)] and [isinstance(M2,int) or isinstance(M2,float)]:
        if rowM1 == rowM2 and colM1 == colM2:
            for j in range(len(M1[0])):
                for i in range(len(M1)):
                    if M1[i][j] != M2[i][j]:  #compares exact values in the matrices
                        return False
    return True

    # compares elements of M1 and M2 if they are two dimensional lists, and returns False if any
    # if the element dont match, otherwise returns True
    pass

# Read the following restriction
# MAKE SURE YOU DO NOT USE MORE THAN LINEAR SPACE 
# IN OTHER WORDS YOU CANT CREATE A NEW MATRIX OF THE SAME SIZE OF THE INPUT
# number of iterations: 2 (columns * rows)
def zero_matrix(M):
    # if an element in an MxN matrix is 0, its entire row and column are set to 0.
    key=transpose(M) #calls the transpose function
    for j in range(len(M[0])):
        for i in range(len(M)):
            if 0 in M[i]:  #if there's a 0 in the matrix, all of the elements in that row will be set to 0
                M[i][j]=0
    for j in range(len(M[0])):
        for i in range(len(M)):
            if 0 in key[j]:  #if there's a 0 in the matrix, all of the elements in that column will be set to 0
                M[i][j]=0
    return M

    # returns the zeroed matrix
    pass

# For local testing and debugging
if __name__ == "__main__":
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    sum = [[10, 10, 10], [10, 10, 10], [10, 10, 10]] # m1+m2
    difference12 = [[-8, -6, -4], [-2, 0, 2], [4, 6, 8]] # m1-m2
    difference21 = [[8, 6, 4], [2, 0, -2], [-4, -6, -8]] # m2-m1
    product12 = [[30, 24, 18], [84, 69, 54], [138, 114, 90]] # m1*m2
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