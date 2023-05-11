mport numpy as np

def kl_transform(data):
    mat_t = data.T
    n = 0
    mean_vector = []
    for n in range(len(mat_t)):
        mean_point = np.mean(mat_t[n])
        mean_vector.append(mean_point)
        n += 1

#covarience matrix time
    covariance_matrix = []
    for i in range(len(mean_vector)):
        row = []
        for j in range(len(mean_vector)):
            # Compute the covariance between columns i and j
            covariance = sum(
                (data[k][i] - mean_vector[i]) * (data[k][j] - mean_vector[j]) for k in range(len(data))) / (
                                 len(data) - 1)
            row.append(covariance)
        covariance_matrix.append(row)

    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]
    transformed_data = np.dot(eigenvectors.T, data.T).T

    return transformed_data

SIGMA_1 = np.array([[4.0, 2.0,.60], [4.2, 2.1,.59],[3.9,2.0,.58],[4.3,2.1,.62],[4.1,2.2,.63]])
func_test=kl_transform(SIGMA_1)
print("FUNC_TEST", func_test)


#big_data=np.genfromtxt('/Users/jtturner/Dropbox/My Mac (Jacqueline’s MacBook Pro (3))/Downloads/304galaxiesreal.csv',delimiter=';'[0,:25])
big_data=np.loadtxt('/Users/jtturner/Dropbox/My Mac (Jacqueline’s MacBook Pro (3))/Downloads/galaxy_edited_2.csv', delimiter=',', usecols=range(5))
print(big_data)
bd_test=kl_transform(big_data)
print("process complete", bd_test)
c = np.savetxt('kl_galaxies_v1.txt', (bd_test))
