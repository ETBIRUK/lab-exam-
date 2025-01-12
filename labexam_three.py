import numpy as np

def reconstruct_matrix(U, S, V):
   

    if S.ndim == 1:
        S = np.diag(S)
    
   
    A_reconstructed = np.dot(U, np.dot(S, V))
    return A_reconstructed

