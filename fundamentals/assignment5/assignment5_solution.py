from czifile import CziFile
from matplotlib import pyplot as plt
from skimage import filters, morphology
import argparse
import numpy as np

def normalize_image(image, vmin=0, vmax=1):
    """
    Convenience function to normalize a numpy array to given bounds.  Default 0 \
    to 1.
    """
    return np.interp(image, (np.min(image), np.max(image)), (vmin, vmax))

# define arguments
parser = argparse.ArgumentParser()
parser.add_argument('image', type=str, nargs=1, help='Path to .CZI image file.')

# parse arguments
args = vars(parser.parse_args())
img_path = args['image'][0]

# open CZI image
with CziFile(img_path) as image_file:
    img_czi_format = image_file.asarray()
    # print(image_file.axes)
    # meta = image_file.metadata()
    # mtree = ElementTree.fromstring(meta)

img = img_czi_format[0,0,:,0,0,:,:,0]  # c, x, y
img_dapi = normalize_image(img[3,:,:])
img_fish = normalize_image(img[2,:,:])
img_dcas13 = img[1,:,:]

# fig, ax = plt.subplots(1,3)
# ax[0].imshow(img_dapi, cmap='binary_r')
# ax[0].set_title('DAPI')
# ax[1].imshow(img_fish, cmap='binary_r')
# ax[1].set_title('FISH')
# ax[2].imshow(img_dcas13, cmap='binary_r')
# ax[2].set_title('dCas13-GFP')
# plt.show()
# plt.close()

# threshold nuclei using Otsu's method
img_dapi_blurxy = filters.gaussian(img_dapi, (10, 10))
thresh_dapi = filters.threshold_otsu(img_dapi_blurxy)*0.85
mask_dapi = (img_dapi_blurxy > thresh_dapi)

for i in range(10):
    mask_dapi = morphology.binary_erosion(mask_dapi)

# fig, ax = plt.subplots(1,2)
# ax[0].imshow(img_dapi, cmap='binary_r')
# ax[1].imshow(mask_dapi, cmap='binary_r')
# plt.show()
# plt.close()


# threshold FISH manually
mask_fish = (img_fish > 0.3)

mask_fish = morphology.remove_small_objects(mask_fish, min_size=8)
mask_fish = morphology.remove_small_holes(mask_fish, area_threshold=8)

# fig, ax = plt.subplots(1,2)
# ax[0].imshow(img_fish, cmap='binary_r')
# ax[1].imshow(mask_fish, cmap='binary_r')
# plt.show()
# plt.close()

# iterate over nuclei
labeled_mask_dapi, n_nuc = morphology.label(mask_dapi, return_num=True)
for i in range(1, n_nuc+1):
    # screen out untransfected cells
    this_nucleus = (labeled_mask_dapi == i)
    if np.mean(img_dcas13[this_nucleus]) > 1.25*np.mean(img_dcas13):

        # calculate dCas13 enrichment
        mask_foci = np.logical_and(mask_fish, this_nucleus)
        mask_not_foci = np.logical_and(np.logical_not(mask_fish), this_nucleus)

        fig, ax = plt.subplots(1,2)
        ax[0].imshow(mask_foci, cmap='binary_r')
        ax[1].imshow(mask_not_foci, cmap='binary_r')
        plt.show()
        plt.close()

        signal_foci = np.mean(img_dcas13[mask_foci])
        signal_not_foci = np.mean(img_dcas13[mask_not_foci])
        enrichment = signal_foci / signal_not_foci

        print(signal_foci, signal_not_foci, enrichment)