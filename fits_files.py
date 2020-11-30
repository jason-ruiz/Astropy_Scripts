# Set up matplotlib and astropy
import matplotlib.pyplot as plt
from astropy.io import fits

# Download the fits file
from astropy.utils.data import download_file

file = 'http://data.astropy.org/tutorials/FITS-images/HorseHead.fits'

image = download_file(file, cache=True)

# simple image grabber
hdu_list = fits.open(image)
hdu_list.info()
new = hdu_list[0].data

# show the image
plt.imshow(new)
plt.colorbar()
plt.show()
