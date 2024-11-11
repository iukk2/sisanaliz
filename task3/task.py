import pandas as pd
import numpy as np

def main(path): # Функция из второго задания
    example = pd.read_csv(path, header = None)
    
    number_of_nodes = example.max().max()
    example_number_of_raws = example.shape[0]
    example_number_of_columns = example.shape[1]

    final = pd.DataFrame(columns = ["r_1", "r_2", "r_3", "r_4", "r_5"], index = range(1, number_of_nodes + 1))
    
    # r_1: отношение непосредственного управления

    for i in range(1, number_of_nodes + 1): 
        r_1 = 0
        for j in range(example_number_of_raws):
            if i == example[0][j]:
                r_1 += 1
        final["r_1"][i] = r_1
    
    #r_2: отношение непосредственного подчинения

    for i in range(1, number_of_nodes + 1):
        r_2 = 0
        for j in range(example_number_of_raws):
            if i == example[1][j]:
                r_2 += 1
        final["r_2"][i] = r_2
        
    #r_3: отношение опосредственного управления

    for i in range(1, number_of_nodes + 1):
        r_3 = 0
        for j in range(example_number_of_raws):
            if i == example[0][j]:
                r_3 += final["r_1"][example[1][j]]
        final["r_3"][i] = r_3
        
    #r_4: отношение опосредственного подчинения

    for i in range(1, number_of_nodes + 1):
        r_4 = 0
        for j in range(example_number_of_raws):
            if i == example[1][j]:
                r_4 += final["r_2"][example[0][j]]
        final["r_4"][i] = r_4
        
    #r_5: отношение соподчинения на одном уровне
    
    for i in range(1, number_of_nodes + 1):
        # Для начала найдем узел которому подчиняется i. 
        boss = 0
        for j in range(example_number_of_raws):
            if i == example[1][j]:
                boss = example[0][j]
        if boss == 0:
            final["r_5"][i] = 0
        else:
            final["r_5"][i] = final["r_1"][boss] - 1

    return final


def entropy(path): #подсчет энтропии
    lenght_matrix = main(path)
    H = 0
    n = lenght_matrix.shape[0]
    k = lenght_matrix.shape[1]
    lenght_matrix_numpy = np.array(lenght_matrix)
    for i in range(n):
        for j in range(k):
            if lenght_matrix_numpy[i][j] != 0: # Если элемент матрицы нулевой, то это не дает вклад в энтропию (x * log x -> 0, при x->0)
                H += -lenght_matrix_numpy[i][j] / (n-1) * np.log2(lenght_matrix_numpy[i][j] / (n-1))
