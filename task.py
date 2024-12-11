import numpy as np

def main():
    #Нахождение возможных значений суммы и произведения и их количество
    A = []
    B = []
    for i in range(1, 7):
        for j in range(1, 7):
            ind_A = 0
            for x in A:
                if i+j == x[0]:
                    x[1] += 1
                    ind_A += 1
            if ind_A == 0:
                A.append([i+j, 1])
    
            ind_B = 0
            for x in B:
                if i*j == x[0]:
                    x[1] += 1
                    ind_B += 1
            if ind_B == 0:
                B.append([i*j, 1])

    # Нахождение H(А) и H(B)
    H_A = 0
    for x in A:
        H_A += - (x[1]) / 36 * np.log2(x[1]/36)
    
    H_B = 0
    for x in B:
        H_B += - (x[1]) / 36 * np.log2(x[1]/36)

    # Нахождение матрицы событий
    AB_matrix = np.zeros((len(A), len(B))) #строки это события A, столбцы события B
    for i in range(1,7):
        for j in range(1,7):
            sum = i+j
            prod = i*j
            for m in range(len(A)):
                if A[m][0] == sum:
                    for n in range(len(B)):
                        if B[n][0] == prod:
                            AB_matrix[m][n] += 1

    # Матрица вероятности
    AB_matrix = AB_matrix / 36

    # Нахождение H(AB)
    H_AB = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if AB_matrix[i][j] != 0:
                H_AB += -AB_matrix[i][j] * np.log2(AB_matrix[i][j])

    # Нахождение H_a(B)
    Ha_B = H_AB - H_A

    # Нахождение I(A,B)
    I_AB = H_B - Ha_B

    result = [H_AB, H_A, H_B, Ha_B, I_AB]
    return result

print(main())