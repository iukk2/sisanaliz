import json
import numpy as np


def main(temperature_functions, control_functions, logical_functions, t):
    
    def mu_temp(id, t):
        for x in temperature_functions['температура']:
            if x['id'] == id:
                if t <= x['points'][0][0]:
                    return x['points'][0][1]
                if t >= x['points'][-1][0]:
                    return x['points'][-1][1]
                for i in range(len(x['points']) - 1):
                    if t >= x['points'][i][0] and t <= x['points'][i+1][0]:
                        return x['points'][i][1] + (t - x['points'][i][0]) / (x['points'][i+1][0] - x['points'][i][0]) * (x['points'][i + 1][1] - x['points'][i][1])

    def mu_control(id, s):
        for x in control_functions['температура']:
            if x['id'] == id:
                if s <= x['points'][0][0]:
                    return x['points'][0][1]
                if s >= x['points'][-1][0]:
                    return x['points'][-1][1]
                for i in range(len(x['points']) - 1):
                    if s >= x['points'][i][0] and s <= x['points'][i+1][0]:
                        return x['points'][i][1] + (s - x['points'][i][0]) / (x['points'][i+1][0] - x['points'][i][0]) * (x['points'][i + 1][1] - x['points'][i][1])

    
    mu_opts = []
    for s in np.linspace(0, 26, 10000):
        mu_C = []
        for x in logical_functions:
            #print(mu_temp(x[0],t), mu_control(x[1],s))
            mu_C.append(min(mu_temp(x[0],t), mu_control(x[1],s)))
            #print(x)
        mu_opts.append(max(mu_C))
    
    first_max = 0
    for i in range(len(mu_opts)):
        if mu_opts[i] > first_max:
            first_max = mu_opts[i]
        if mu_opts[i] < first_max:
            break
    
    for i in range(len(mu_opts)):
        if first_max == mu_opts[i]:
            #print(mu_opts)
            return 26 / (10000-1) * i
            break
