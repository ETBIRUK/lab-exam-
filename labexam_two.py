import numpy as np

def compute_cross_product(vec1, vec2):
   
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    
   
    if vec1.shape != (3,) or vec2.shape != (3,):
        raise ValueError("Both input vectors must be 3-dimensional.")
    
    return np.cross(vec1, vec2)

