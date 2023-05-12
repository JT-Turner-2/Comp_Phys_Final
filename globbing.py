import glob
from astropy.io import fits

galslist = glob.iglob('blindenbau@hopper/Downloads/dr16/sdss/spectro/redux/26/lite/**/*.fits', recursive=True)

print(galslist)

for gal in galslist:
    with fits.open(gal) as g:
        events = g[1].data
    events = table.read(gal)
    print(events)

# with open('download_rsync.txt', 'r') as file:
#     content = file.read()
#     fitsfiles = [] #empty array to store fits files in
#     delimiter = ' & \n'
#     start = 0
#     end = content.find(delimiter)
#
#     while end >= 0:
#         fitsdata = content[start:end]
#         hdulist = fits.open(fitsdata)
#
#         fitsfiles.append(hdulist)
#
#         start = end + len(delimiter)
#         end = content.find(delimiter, start)

# with open('download_rsync.txt', 'r') as file:
#     content = file.read()
#     i = 0
#     fitsfiles = [] #empty array to store fits files in
#
#     while True:
#         start_i = content.find('/sdss/', i)
#         if start_i == -1:
#             break
#         end_i = content.find('.fits', start_i)
#         if end_i == -1:
#             break
#
#         fitscontent = content[start_i:end_i]
#         thefile = fits.open(fitscontent)
#
#         fitsfiles.append(thefile)
#
#         i = end_i
