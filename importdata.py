import h5py
import numpy as np

def importdata(num_of_cases):
    data = []
    for i in range(num_of_cases):
        with h5py.File(f'data/case{i + 1}.mat', 'r')as mat_file:
            case = {key: mat_file[key][()] for key in mat_file.keys()}
            data.append(case)
    return data

data = importdata(24)


