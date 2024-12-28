import pandas as pd
import numpy as np

def main(var):
    example = np.array(var)
    
    number_of_nodes = example.max().max()
    example_number_of_raws = example.shape[0]
    example_number_of_columns = example.shape[1]

    final = pd.DataFrame(columns = ["r_1", "r_2", "r_3", "r_4", "r_5"], index = range(1, number_of_nodes + 1))
    
    # r_1: отношение непосредственного управления

    for i in range(1, number_of_nodes + 1):
        r_1 = 0
        for j in range(example_number_of_raws):
            if i == example[j][0]:
                r_1 += 1
        final["r_1"][i] = r_1
    
    #r_2: отношение непосредственного подчинения

    for i in range(1, number_of_nodes + 1):
        r_2 = 0
        for j in range(example_number_of_raws):
            if i == example[j][1]:
                r_2 += 1
        final["r_2"][i] = r_2
        
    #r_3: отношение опосредственного управления

    for i in range(1, number_of_nodes + 1):
        r_3 = 0
        for j in range(example_number_of_raws):
            if i == example[j][0]:
                r_3 += final["r_1"][example[j][1]]
        final["r_3"][i] = r_3
        
    #r_4: отношение опосредственного подчинения

    for i in range(1, number_of_nodes + 1):
        r_4 = 0
        for j in range(example_number_of_raws):
            if i == example[j][1]:
                r_4 += final["r_2"][example[j][0]]
        final["r_4"][i] = r_4
        
    #r_5: отношение соподчинения на одном уровне
    
    for i in range(1, number_of_nodes + 1):
        # Для начала найдем узел которому подчиняется i.
        boss = 0
        for j in range(example_number_of_raws):
            if i == example[j][1]:
                boss = example[j][0]
        if boss == 0:
            final["r_5"][i] = 0
        else:
            final["r_5"][i] = final["r_1"][boss] - 1
    
    final = np.array(final)
    return final

var = [[1,2],[1,3],[3,4],[3,5]]
print(main(var))
