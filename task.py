import json
import numpy as np

with open("Ранжировка  A.json") as A_:
    A = json.load(A_)

with open("Ранжировка  B.json") as B_:
    B = json.load(B_)

def making_matrix(A):
    elements = []
    for x in A:
        if type(x) == int:
            elements.append(x)
        else:
            for y in x:
                elements.append(y)

    A_matrix = np.identity(len(elements))
    
    for i in range(len(A)):
        if type(A[i]) == int:
            for j in range(i, len(A)):
                if type(A[j]) == int:
                    A_matrix[A[i] - 1][A[j] - 1] = 1
                else:
                    for x in A[j]:
                        A_matrix[A[i] - 1][x - 1] = 1
        else:
            for x in A[i]:
                for y in A[i]:
                    A_matrix[x-1][y-1] = 1
                for j in range(i+1, len(A)):
                    if type(A[j]) == int:
                        A_matrix[x-1][A[j] - 1] = 1
                    else:
                        for y in A[j]:
                            A_matrix[x-1][y-1] = 1
    return A_matrix

def logical_product(A, B):
    A_B = np.zeros((len(A), len(A)))
    for i in range(len(A_B)):
        for j in range(len(A_B)):
            A_B[i][j] = A[i][j] * B[i][j]
    return A_B

def logical_sum(A,B):
    sum = np.zeros((len(A), len(A)))
    for i in range(len(sum)):
        for j in range(len(sum)):
            if A[i][j] + B[i][j] == 0:
                sum[i][j] = 0
            else:
                sum[i][j] = 1
    return sum

def main(A, B): #Принимает json-строки
    A_matrix = making_matrix(A)
    B_matrix = making_matrix(B)

    A_B = logical_product(A_matrix, B_matrix)
    A_B_T = np.transpose(A_B)

    sum = logical_sum(A_B, A_B_T)

    contradiction = []
    for i in range(len(sum) - 1):
        for j in range(i+1, len(sum)):
            if sum[i][j] == 0:
                contradiction.append([i+1, j+1])
    return(contradiction)
    

print(main(A, B))

