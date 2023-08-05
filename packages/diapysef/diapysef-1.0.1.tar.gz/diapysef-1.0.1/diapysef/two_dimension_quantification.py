import click
import logging

import pandas as pd
import numpy as np
import skimage as skimg
import skimage.filters
from scipy import ndimage as ndi

from skimage.segmentation import watershed, random_walker
from skimage.feature import peak_local_max
from skimage.measure import moments

import matplotlib.pyplot as plt

def enhanced_connected_components(image, blur='gaussian', sigma=1, truncate=0.5, t=None, connectivity=2, min_area=0):
    if blur=='gaussian':
      blurred_image = skimage.filters.gaussian(image, sigma=sigma, truncate=truncate)
      if False:
        fig = plt.figure(1, figsize=(12.75, 8.25))
        ax1 = plt.subplot(1, 2, 1)
        ax1.imshow(image, cmap="afmhot_r", aspect="auto")
        ax2 = plt.subplot(1, 2, 2)
        ax2.imshow(blurred_image, cmap="afmhot_r", aspect="auto")
        plt.show()
        plt.close()
    else:
      blurred_image = image.copy()
    if t is None:
      t = skimage.filters.threshold_otsu(blurred_image[np.logical_not(np.isnan(blurred_image))], nbins=256)
      print("Found automatic threshold t = {}.".format(t))
    binary_mask = blurred_image > t
    object_mask = skimage.morphology.remove_small_objects(binary_mask, min_area)
    if False:
      plt.imshow(object_mask, cmap="gray", aspect="auto")
      plt.show()
      plt.close()
    
    # Now we want to separate the two objects in image
    # Generate the markers as local maxima of the distance to the background
    distance = ndi.distance_transform_edt(object_mask)
    coords = peak_local_max(distance, min_distance=5, num_peaks=3, labels=object_mask)
    mask = np.zeros(distance.shape, dtype=bool)
    mask[tuple(coords.T)] = True
    markers, count = ndi.label(mask)
    print(f"Found {count} feature(s)")
    labels = watershed(-distance, markers, mask=object_mask)
    if False:
      plt.imshow(labels, cmap=plt.cm.nipy_spectral, aspect="auto")
      plt.show()
      plt.close()
    
    # convert the label image to color image
    colored_label_image = skimage.color.label2rgb(labels, bg_label=0)
    if False:
      plt.imshow(colored_label_image, cmap=plt.cm.nipy_spectral, aspect="auto")
      plt.show()
      plt.close()
    return blurred_image, object_mask, distance, labels, count, colored_label_image



filter_peptides = ["VS(UniMod:21)YDVTSAR"]#, "VSYDVT(UniMod:21)SAR"]
filter_charge_state = 2
ms_level=1

# Load data from tsv
data = pd.read_csv("extracted_data.tsv", sep="\t")

data_filt = data.loc[(data.peptide.isin(filter_peptides)) & (data.charge==filter_charge_state) & (data.ms_level==ms_level)]

image = data_filt.pivot_table(index='im', columns='rt', values='int').to_numpy()

plt.imshow(image, aspect='auto')

plt.show()

histogram, bin_edges = np.histogram(img, bins=256, range=(0, np.nanmax(img)))

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
# plt.xlim([0.0, 1.0])  # <- named arguments do not work here

plt.plot(bin_edges[0:-1], histogram)  # <- or here
plt.show()

sigma = 1.5

# apply Gaussian blur, creating a new image
blurred = skimage.filters.gaussian(img, sigma=(sigma, sigma), truncate=0.4)

# display blurred image
fig, ax = plt.subplots(figsize=(15, 15))
plt.imshow(blurred, aspect='auto')
plt.show()


# create a mask based on the threshold
t = 10000
t = skimage.filters.threshold_otsu(img[np.logical_not(np.isnan(img))], nbins=256)
print("Found automatic threshold t = {}.".format(t))
binary_mask = img > t

# use the binary_mask to select the "interesting" part of the image
selection = img.copy()
selection[~binary_mask] = 0

labeled_image, count = skimage.measure.label(binary_mask, return_num=True, connectivity=1)

# convert the label image to color image
colored_label_image = skimage.color.label2rgb(labeled_image, bg_label=0)

blurred_image, object_mask, \
distance, labeled_image, count, \
colored_label_image = enhanced_connected_components(image=image, blur=None, sigma=3, truncate=0.4, t=None, connectivity=1, min_area=200)


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9, 3), sharex=True, sharey=True)

ax1.imshow(image, aspect='auto', cmap="afmhot_r")
ax1.set_title('Original')
ax2.imshow(object_mask, aspect='auto', cmap="gray")
ax2.set_title('Mask')
ax3.imshow(-distance, aspect='auto', cmap=plt.cm.gray)
ax3.set_title('Distances')
ax4.imshow(colored_label_image, aspect='auto')
for label in unique_feature_labels:
  if label!=0:
    M = moments(labeled_image==label, order=3)
    centroid = (M[1, 0] / M[0, 0], M[0, 1] / M[0, 0])
    ax4.text(centroid[1], centroid[0], label, color="white", bbox=dict(fill=False, edgecolor='green', linewidth=2))
ax4.set_title('Watershed')
plt.tight_layout(rect=[0.03, 0.03, 1, 1])
plt.show()
plt.close()

unique_feature_labels = np.unique(labeled_image)

int_dict = {}
for label in unique_feature_labels:
  if label!=0:
    int_dict[label] = np.sum(image[labeled_image==label])



# compute object features and extract object areas
object_features = skimage.measure.regionprops(labeled_image)
object_areas = [objf["area"] for objf in object_features]
object_areas

min_area = 200
object_areas = np.array([objf["area"] for objf in object_features])
object_labels = np.array([objf["label"] for objf in object_features])
large_objects = object_labels[object_areas > min_area]
print("Found", len(large_objects), "objects!")

