import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Dot product A·B:\n", np.dot(A, B))


print("Transpose of A:\n", A.T)


print("Determinant of A:", np.linalg.det(A))


eigvals, eigvecs = np.linalg.eig(A)
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)
