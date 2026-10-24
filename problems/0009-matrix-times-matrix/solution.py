import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if not a or len(a[0]) != len(b):
        return -1
        
	return (np.array(a) @ np.array(b)).tolist()