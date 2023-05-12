from astropy.io import fits
import glob
import os
import pdb
import numpy as np

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
    print("length of mean vector", len(mean_vector))
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
    print("evalue_before_sort",eigenvalues)
    #c = np.savetxt('kl_unsorted_evectors_3.csv', (eigenvectors))
    sorted_indices = np.argsort(-eigenvalues)
    #print(sorted_indices)

    eigenvalues_2 = np.sort(eigenvalues)[::-1]
    print("evalue after sort",eigenvalues_2)
    eigenvectors = eigenvectors[:, sorted_indices]
    #c2=np.savetxt('kl_sorted_evectors_3.csv', (eigenvectors))
    transformed_data = np.dot(eigenvectors.T, data.T).T

    return transformed_data

#had to manually open the fits files
file1 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0427.fits')
gal1 = file1[1].data
file2 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0443.fits')
gal2 = file2[1].data
file3 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0444.fits')
gal3 = file3[1].data
file4 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0445.fits')
gal4 = file4[1].data
file5 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0459.fits')
gal5 = file5[1].data
file6 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0462.fits')
gal6 = file6[1].data
file7 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0463.fits')
gal7 = file7[1].data
file8 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0464.fits')
gal8 = file8[1].data
file9 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0470.fits')
gal9 = file9[1].data
file10 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0471.fits')
gal10 = file10[1].data
file11 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0475.fits')
gal11 = file11[1].data
file12 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0476.fits')
gal12 = file12[1].data
file13 = fits.open('sdss/spectro/redux/26/spectra/lite/1517/spec-1517-52934-0477.fits')
gal13 = file13[1].data

np.savetxt('firstgal.csv', gal1, delimiter='\t')
np.savetxt('2gal.csv', gal2, delimiter='\t')
np.savetxt('3gal.csv', gal3, delimiter='\t')
np.savetxt('4gal.csv', gal4, delimiter='\t')
np.savetxt('5gal.csv', gal5, delimiter='\t')
np.savetxt('6gal.csv', gal6, delimiter='\t')
np.savetxt('7gal.csv', gal7, delimiter='\t')
np.savetxt('8gal.csv', gal8, delimiter='\t')
np.savetxt('9gal.csv', gal9, delimiter='\t')
np.savetxt('10gal.csv', gal10, delimiter='\t')
np.savetxt('11gal.csv', gal11, delimiter='\t')
np.savetxt('12gal.csv', gal12, delimiter='\t')
np.savetxt('13gal.csv', gal13, delimiter='\t')


forgal1 = np.loadtxt('firstgal.csv')
transform_gal1 = kl_transform(forgal1)
print('transformed!')

forgal2 = np.loadtxt('2gal.csv')
transform_gal2 = kl_transform(forgal2)
print('transformed!')

forgal3 = np.loadtxt('3gal.csv')
transform_gal3 = kl_transform(forgal3)
print('transformed!')

forgal4 = np.loadtxt('4gal.csv')
transform_gal4 = kl_transform(forgal4)
print('transformed!')

forgal5 = np.loadtxt('5gal.csv')
transform_gal5 = kl_transform(forgal5)
print('transformed!')

forgal6 = np.loadtxt('6gal.csv')
transform_gal6 = kl_transform(forgal6)
print('transformed!')

forgal7 = np.loadtxt('7gal.csv')
transform_gal7 = kl_transform(forgal7)
print('transformed!')

forgal8 = np.loadtxt('8gal.csv')
transform_gal8 = kl_transform(forgal8)
print('transformed!')

forgal9 = np.loadtxt('9gal.csv')
transform_gal9 = kl_transform(forgal9)
print('transformed!')

forgal10 = np.loadtxt('10gal.csv')
transform_gal10 = kl_transform(forgal10)
print('transformed!')

forgal11 = np.loadtxt('11gal.csv')
transform_gal11 = kl_transform(forgal11)
print('transformed!')

forgal12 = np.loadtxt('12gal.csv')
transform_gal12 = kl_transform(forgal12)
print('transformed!')

forgal13 = np.loadtxt('13gal.csv')
transform_gal13 = kl_transform(forgal13)
print('transformed!')

#projections

def projection(v,u):
    v = np.array(v)
    u = np.array(u)
    v_norm = np.sqrt(sum(v**2))
    proj_of_u_on_v = (np.matmul(v, np.matmul(u.T, v)/(v_norm**2)))
    return proj_of_u_on_v

projgal1 = projection(forgal1,transform_gal1)
print('projected!')
projgal2 = projection(forgal2,transform_gal2)
print('projected!')
projgal3 = projection(forgal3,transform_gal3)
print('projected!')
projgal4 = projection(forgal4,transform_gal4)
print('projected!')
projgal5 = projection(forgal5,transform_gal5)
print('projected!')
projgal6 = projection(forgal6,transform_gal6)
print('projected!')
projgal7 = projection(forgal7,transform_gal7)
print('projected!')
projgal8 = projection(forgal8,transform_gal8)
print('projected!')
projgal9 = projection(forgal9,transform_gal9)
print('projected!')
projgal10 = projection(forgal10,transform_gal10)
print('projected!')
projgal11 = projection(forgal11,transform_gal11)
print('projected!')
projgal12 = projection(forgal12,transform_gal12)
print('projected!')
projgal13 = projection(forgal13,transform_gal13)
print('projected!')
