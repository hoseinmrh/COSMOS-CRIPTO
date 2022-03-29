import numpy as np
from numpy.linalg import inv
def Matrix_Maker(fileName):
    # We define some lists to create our matrix
    matrix = []
    second_M =[]
    file1 = open(fileName, 'r')
    while True:
        # Get next line from file
        line = file1.readline()
        if not line:
            break
        first_M = line.split('\t')
        for i in range(0 ,len(first_M)):
            second_M.append(float(first_M[i])) # Change the lists item into floate type
        matrix.append(second_M) # Creat the matrix row by row
        second_M = [] # Clear the matrix to add new item in it
    file1.close()
    return matrix

def W_List(X, Y):
    # Calculate W0,W1,... using this equation [(X^T X)^(-1) . X^T.Y]
    wList = []
    A = np.array(X)
    B = np.array(Y)
    X_T = A.transpose() # X transposition
    X_1 = np.dot(X_T,A) # (X^T X)
    X_1_inverse = inv(X_1) # (X^T X)^(-1)
    X_2 = np.dot(X_1_inverse,X_T) #(X^T X)^(-1) . X^T
    W = np.dot(X_2,B) # [(X^T X)^(-1) . X^T.Y]
    for i in range (0,len(W)):
        wList.append(W[i][0])

    return wList

def norm_2(W,X,Y):
    # Calculate norm 2
    lenght_Y = len(Y)
    norm2 = 0
    for i in range(0,lenght_Y):
        norm2 = norm2 + ((W[0]*X[i][0] + W[1]*X[i][1] + W[2]*X[i][2]) - Y[i][0])**2
    return norm2

def Closing_Prtice():
    X = Matrix_Maker('ClosingPrice_X.txt')
    Y = Matrix_Maker('ClosingPrice_Y.txt')
    W = W_List(X, Y)
    lenght_Y = len(Y)
    cosmos_value = W[0] + Y[lenght_Y - 2][0] * W[1] + Y[lenght_Y-1][0] * W[2]
    real_value_on_that_day = 8.082147899
    print("My guess for cosmos closing price's value on 25th Jan is : ",cosmos_value)
    error = real_value_on_that_day - cosmos_value
    print("Differance norm 1 : ",error)
    norm2_C_P = norm_2(W,X,Y)
    print("The norm 2 of closing price using this method is : ", norm2_C_P)
    error2 = real_value_on_that_day - norm2_C_P
    print("Differance norm 2 : ", error2)

    exit()

def TwnentyFour_H_Open():
    X = Matrix_Maker('24hOpen_X.txt')
    Y = Matrix_Maker('24hOpen_Y.txt')
    W = W_List(X, Y)
    lenght_Y = len(Y)
    cosmos_value = W[0] + Y[lenght_Y - 2][0] * W[1] + Y[lenght_Y-1][0] * W[2]
    real_value_on_that_day = 7.9939175825
    print("My guess for cosmos 24h open's value on 25th Jan is : ",cosmos_value)
    error = real_value_on_that_day - cosmos_value
    print("Differance norm 1 : ", error)
    norm2_C_P = norm_2(W,X,Y)
    print("The norm 2 of 24h open using this method is : ", norm2_C_P)
    error2 = real_value_on_that_day - norm2_C_P
    print("Differance norm 2 : ", error2)
    exit()

def TwentyFour_H_High():
    X = Matrix_Maker('24hHigh_X.txt')
    Y = Matrix_Maker('24hHigh_Y.txt')
    W = W_List(X, Y)
    lenght_Y = len(Y)
    cosmos_value = W[0] + Y[lenght_Y - 2][0] * W[1] + Y[lenght_Y-1][0] * W[2]
    real_value_on_that_day = 8.5399013831
    print("My guess for cosmos 24h high's value on 25th Jan is : ",cosmos_value)
    error = real_value_on_that_day - cosmos_value
    print("Differance norm 1 : ", error)
    norm2_C_P = norm_2(W,X,Y)
    print("The norm 2 of 24h high using this method is : ", norm2_C_P)
    error2 = real_value_on_that_day - norm2_C_P
    print("Differance norm 2 : ", error2)
    exit()

def TwentyFour_H_Low():
    X = Matrix_Maker('24hLow_X.txt')
    Y = Matrix_Maker('24hLow_Y.txt')
    W = W_List(X, Y)
    lenght_Y = len(Y)
    cosmos_value = W[0] + Y[lenght_Y - 2][0] * W[1] + Y[lenght_Y-1][0] * W[2]
    real_value_on_that_day = 7.9713813968
    print("My guess for cosmos 24h low's value on 25th Jan is : ",cosmos_value)
    error = real_value_on_that_day - cosmos_value
    print("Differance norm 1 : ", error)
    norm2_C_P = norm_2(W,X,Y)
    print("The norm 2 of 24h low using this method is : ", norm2_C_P)
    error2 = real_value_on_that_day - norm2_C_P
    print("Differance norm 2 : ", error2)
    exit()

def menu():
# Define menu
    print("Enter:\n '1' to show closing price\n '2' to show 24h open\n '3' to show 24h high\n '4' to show 24h low\n")
    n = int(input())
    if (n == 1):
        Closing_Prtice()
    if (n == 2):
        TwnentyFour_H_Open()
    if (n == 3):
        TwentyFour_H_High()
    if (n == 4):
        TwentyFour_H_Low()
    else:
        print("Invalid input, Please try again\n")
        menu()

menu()
