import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Finding peak element in a 2D Array.
MAX = 100
from math import ceil
 
# Function to find the maximum in column 'mid'
# 'rows' is number of rows.
def findMax(arr, rows, mid,max):
 
    max_index = []
    mid_index = []
    for i in range(rows):
        if (np.logical_not(np.isnan(arr[i][mid]))) and ((len(max)==0) or np.any((arr[i][mid] > max))):
            # Saving global maximum and its index
            # to check its neighbours
            max = np.append(max, [arr[i][mid]])
            max_index.append(i)
            mid_index.append(mid)
    print(f"INFO: Max intensity ({max}) found at row index ({max_index}) at mid ({mid})")
 
    return max,mid_index,max_index
 
# Function to find a peak element
def findPeakRec(arr, rows, columns,mid):
 
    # Evaluating maximum of mid column.
    # Note max is passed by reference.
    max = np.array([])
    max,mid_index,max_index = findMax(arr, rows, mid, max)
 
    # # If we are on the first or last column,
    # # max is a peak
    # if (mid == 0 or mid == columns - 1):
    #     return max
    # 
    # # If mid column maximum is also peak
    # if (max >= arr[max_index][mid - 1] and
    #     max >= arr[max_index][mid + 1]):
    #     return max
    # 
    # # If max is less than its left
    # if (max < arr[max_index][mid - 1]):
    #     return findPeakRec(arr, rows, columns,
    #                        mid - ceil(mid / 2.0))
    # 
    # # If max is less than its left
    # # if (max < arr[max_index][mid+1])
    # return findPeakRec(arr, rows, columns,
    #                    mid + ceil(mid / 2.0))
    return mid, mid_index, max_index

# A wrapper over findPeakRec()
def findPeak(arr, rows, columns):
    return [ findPeakRec(arr, rows, columns, i) for i in range(0, columns) ]
 

# Driver Code
arr = np.array([  [  0.5, 0, 0, 2, 1, 0, 0.5, 0.1],
                  [  0.1, 0, 0, 3, 4, 0, 0.5, 0],
                  [ 1, 3, 10, 12, 15, 10, 1, 0.8 ],
                  [ 2, 4, 14, 19, 17, 11, 5, 1 ],
                  [ 0.9, 3, 12, 21, 19, 14, 4, 2 ],
                  [ 0.8, 2, 14, 15, 16, 15, 4, 0.5 ],
                  [  2, 0, 0, 2, 3, 0, 0.5, 0.1],
                  [  1, 0, 0, 2, 1, 0, 0.5, 0]
                ])

kernel = np.array([1.0, 2.0, 1.0]) # Here you would insert your actual kernel of any size
arr_blur = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 0, arr)
arr_blur = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 1, arr_blur)

filter_peptides = ["VS(UniMod:21)YDVTSAR"]#, "VSYDVT(UniMod:21)SAR"]
filter_peptides = ["T(UniMod:21)ELISVSEVHPSR"]
filter_peptides = ["YVC(UniMod:4)EGPSHGGLPGASS(UniMod:21)EK"]
filter_charge_state = 2
ms_level=1

# Load data from tsv
data = pd.read_csv("extracted_data.tsv", sep="\t")

data_filt = data.loc[(data.peptide.isin(filter_peptides)) & (data.charge==filter_charge_state) & (data.ms_level==ms_level)]

arr = data_filt.pivot_table(index='im', columns='rt', values='int').to_numpy()

# Number of Columns
rows = arr.shape[0]
columns = arr.shape[1]
peaks = findPeak(arr, rows, columns)

int_list = []
x_list = []
y_list = []
for pk in peaks:
  int_list.append(pk[0])
  # x_list.append(np.unique(pk[1])[0])
  # y_list.append(np.unique(pk[2])[0])
  x_list.append(pk[1])
  y_list.append(pk[2])

plt.close()
plt.imshow(arr, aspect='auto')
plt.colorbar()
# plt.plot(np.concatenate(x_list),np.concatenate(y_list),'ro')
plt.show()

import copy

def get_std(image):
    return np.std(image)

def get_max(image,sigma,alpha=20,size=10):
    i_out = []
    j_out = []
    image_temp = copy.deepcopy(image)
    while True:
        k = np.argmax(image_temp)
        j, i = np.unravel_index(k, image_temp.shape)
        if(image_temp[j,i] >= alpha*sigma):
            i_out.append(i)
            j_out.append(j)
            x = np.arange(i-size, i+size)
            y = np.arange(j-size, j+size)
            xv,yv = np.meshgrid(x,y)
            image_temp[yv.clip(0,image_temp.shape[0]-1), xv.clip(0,image_temp.shape[1]-1) ] = 0
            # print(xv)
        else:
            break
    return i_out,j_out

def isValidPos(i, j, n, m):
    # See: https://www.geeksforgeeks.org/find-all-adjacent-elements-of-given-element-in-a-2d-array-or-matrix/
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1
 
 
# Function that returns all adjacent elements
def _getAdjacent(arr, i, j, extender=0):
    # See: https://www.geeksforgeeks.org/find-all-adjacent-elements-of-given-element-in-a-2d-array-or-matrix/
    # Size of given 2d array
    n = len(arr)
    m = len(arr[0])
 
    # Initialize 1 cell adjacent check
    position_check = 1
    # Extend number of cells to check adjacency
    position_check = position_check + extender
    
    # Initialising a vector array
    # where adjacent element will be stored
    v = []
    # Store value and coordinates in dictionary
    x = []
    y = []
    
    # Checking for all the possible adjacent positions
    if (isValidPos(i - position_check, j - position_check, n, m)):
        v.append(arr[i - position_check][j - position_check])
        x.append(i - position_check)
        y.append(j - position_check)
    if (isValidPos(i - position_check, j, n, m)):
        v.append(arr[i - position_check][j])
        x.append(i - position_check)
        y.append(j)
    if (isValidPos(i - position_check, j + position_check, n, m)):
        v.append(arr[i - position_check][j + position_check])
        x.append(i - position_check)
        y.append(j + position_check)
    if (isValidPos(i, j - position_check, n, m)):
        v.append(arr[i][j - position_check])
        x.append(i)
        y.append(j - position_check)
    if (isValidPos(i, j + position_check, n, m)):
        v.append(arr[i][j + position_check])
        x.append(i)
        y.append(j + position_check)
    if (isValidPos(i + position_check, j - position_check, n, m)):
        v.append(arr[i + position_check][j - position_check])
        x.append(i + position_check)
        y.append(j - position_check)
    if (isValidPos(i + position_check, j, n, m)):
        v.append(arr[i + position_check][j])
        x.append(i + position_check)
        y.append(j)
    if (isValidPos(i + position_check, j + position_check, n, m)):
        v.append(arr[i + position_check][j + position_check])
        x.append(i + position_check)
        y.append(j + position_check)
    # print(d)
    # Returning the vector
    return v, x, y
 
# Wrapper for getAdjacent
def getAdjacent(arr, i, j, extender=2):
  
  return [_getAdjacent(arr, i, j, extend) for extend in range(0, extender)]

# Smooth data
arr[np.isnan(arr)] = 0
box_pts = 6
kernel = np.ones(box_pts)/box_pts # Here you would insert your actual kernel of any size
arr_blur = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 0, arr)
arr_blur = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 1, arr_blur)

#computing the standard deviation of the image
sigma = get_std(arr_blur)
#getting the peaks
i, j = get_max(arr_blur, sigma, alpha=2.5, size=20)

max_int = np.mean(arr[j, i])
mask = arr >= max_int*0.49

kernel = np.ones(box_pts)/box_pts # Here you would insert your actual kernel of any size
mask_blur = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 0, mask)
mask_blur = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 1, mask_blur)
mask_blur[mask_blur>=0.5] = True
mask_blur[mask_blur<0.5] = False
mask = mask_blur
masked = np.ma.masked_where(mask_blur==0, mask_blur)

import scipy.ndimage.measurements as mnts
import cv2
s = [[1,1,1],
       [1,1,1],
       [1,1,1]]
labeled, clusters = mnts.label(mask, s)

def check_connection(bool_vector, gaps, seed):
    # indice_list = []
    # for bool_check, indice in zip(bool_vector, range(0, bool_vector.shape[0])):
    #   if bool_check and  len(indice_list)==0:
    #     indice_list.append(indice)
    #   elif bool_check and indice - indice_list[-1] <=  gaps:
    #     indice_list.append(indice)
    # Get all indices where true
    feature_indices = np.where(bool_vector)[0]
    # Compute whether indices are sequential
    indice_lag_difference = feature_indices[list(range(1, feature_indices.shape[0]))] - feature_indices[list(range(0, feature_indices.shape[0]-1))]
  
    feature_index_list = []
    single_feature_index_list = []
    for indice, lag_diff in zip(feature_indices, indice_lag_difference):
      if lag_diff < gaps:
        single_feature_index_list.append(indice)
      else:
        if len(single_feature_index_list)!=0:
          feature_index_list.append(single_feature_index_list)
        single_feature_index_list = []
      if indice==feature_indices[-2]:
        feature_index_list.append(single_feature_index_list)
    feature_index_list = [x for x in feature_index_list if x != []]
    # Get feature indices for current seed
    # Based on the current true feature index list, which is closest to the current seed
    # TODO: Find the max diagonal indexes in either direction?
    current_feature_indices = [seed[1] in single_feature_list or abs(seed[1] - np.max(single_feature_list)) < 10 for single_feature_list in feature_index_list]
    if any(current_feature_indices):
      indice_list = feature_index_list[int(np.where(current_feature_indices)[0])]
    else:
      indice_list = []

    return np.array(indice_list)

def check_adjacent_feature_connection(mask_subset, label_mask_subset, gaps, seed):
  # Get the first boolean True index, where there is at least x consecutive true, and not a random noise true
  # indexes_where_true = np.where(mask_subset[:, ceil(mask_subset.shape[1]/2)-1])[0]
  
  first_index = check_connection(mask_subset[:, ceil(mask_subset.shape[1]/2)-1], gaps, seed)
  # first_index = indexes_where_true[np.where(indexes_where_true[list(range(0,len(indexes_where_true)-1))]-indexes_where_true[list(range(1,len(indexes_where_true)))]==-1)[0]]
  if first_index.shape[0]==0:
    return False
  # TODO: Instead of using gaps, for each current x axis vector, should I start from the centre?
  target_coord_mask_surroundings = mask_subset[list(range(first_index[0]-gaps, first_index[0]+gaps+1)), :]
  target_coord_label_mask_surroundings = label_mask_subset[list(range(first_index[0]-gaps, first_index[0]+gaps+1)), :]
  return (np.logical_not(np.sum(target_coord_mask_surroundings, 1)[0]==0) or \
          np.logical_not(np.all(np.isnan(target_coord_label_mask_surroundings)))) and \
          np.logical_not(np.all([np.all(coord_mask==coord_label) for coord_mask, coord_label in zip(np.where(target_coord_mask_surroundings), np.where(np.logical_not(np.isnan(target_coord_label_mask_surroundings))))]))

def check_dim_constraint(buffer_size, arr_shape):

  if buffer_size > arr_shape:
    return(arr_shape)
  else:
    return(buffer_size)

# Iterate over seeds
gaps = 3 # 2 is good
label_mask = np.empty(mask.shape)
label_mask.fill(np.nan)
id_tag_dict = {'0':0}
tag_id = 0
fig = plt.figure()
ims = []
for x, y in zip(j, i):
  print(f"INFO: Working on seed {x}, {y}")
  
  # Get indexes where true, representing a feature
  indices_where_true = np.where(mask[:, y])[0]
  # Get the sequential difference to identify breaks/spaces between features
  difference_between_indices = indices_where_true[list(range(1, indices_where_true.shape[0]))] - indices_where_true[list(range(0, indices_where_true.shape[0]-1))]
  # Get the feature that is closet to current seed feature
  feature_list_indices = []
  one_feature_list = []
  for boolean_index, feature_index in zip(difference_between_indices<gaps, indices_where_true):
    if boolean_index:
      one_feature_list.append(feature_index)
    else:
      if len(one_feature_list)!=0:
        feature_list_indices.append(one_feature_list)
      one_feature_list = []
    if feature_index==indices_where_true[-2]:
      one_feature_list.append(indices_where_true[-1])
      feature_list_indices.append(one_feature_list)
  
  current_feature_indice_list = np.array(feature_list_indices[np.where([True if x in sub_feature_index_list else False for sub_feature_index_list in feature_list_indices ])[0][0]])
  
  label_mask[current_feature_indice_list, y] = tag_id
  
  # # plt.close()
  # myplot = plt.imshow(mask, aspect='auto')
  # # plt.plot(21, 54,'ro')
  # plt.scatter(np.where(label_mask==0)[1], np.where(label_mask==0)[0],c='r', s=2)
  # plt.scatter(np.where(label_mask==1)[1], np.where(label_mask==1)[0],c='g', s=2)
  # ims.append([myplot])
  
  # Walk to the right
  for y_walker in range(y-1, label_mask.shape[1]): #range(y-1, 21):#
    ## TODO: If there is a feature further away, stop checking, because it's a separate feature.
    if np.sum(mask[:, list(range(y_walker+1, check_dim_constraint(y_walker+gaps, label_mask.shape[1])))])==0:
      break 
    if np.any(mask[:, y_walker]):
      feature_indices = check_connection(mask[:,y_walker], gaps, (y,x))
      mask_subset = mask[:, list(range(y_walker-gaps,check_dim_constraint(y_walker+gaps+1, label_mask.shape[1])))]
      label_mask_subset = label_mask[:, list(range(y_walker-gaps, check_dim_constraint(y_walker+gaps+1, label_mask.shape[1])))]
      if check_adjacent_feature_connection(mask_subset, label_mask_subset, gaps, (y,x)):
        print(f"right: y_walker: {y_walker}")
        label_mask[feature_indices, y_walker] = tag_id
        # # plt.close()
        # myplot = plt.imshow(mask, aspect='auto')
        # # plt.plot(21, 54,'ro')
        # plt.scatter(np.where(label_mask==0)[1], np.where(label_mask==0)[0],c='r', s=2)
        # plt.scatter(np.where(label_mask==1)[1], np.where(label_mask==1)[0],c='g', s=2)
        # ims.append([myplot])
  # Walk to the left
  for y_walker in range(0, y-1):
    if np.sum(mask[:, list(range(y_walker-1, check_dim_constraint(y_walker-gaps, label_mask.shape[1])))])==0:
      break
    if np.any(mask[:, y_walker]):
      feature_indices = check_connection(mask[:,y_walker], gaps, (y,x))
      mask_subset = mask[:,list(range(y_walker-gaps, check_dim_constraint(y_walker+gaps+1, label_mask.shape[1])))]
      label_mask_subset = label_mask[:, list(range(y_walker-gaps, check_dim_constraint(y_walker+gaps+1, label_mask.shape[1])))]
      if check_adjacent_feature_connection(mask_subset, label_mask_subset, gaps, (y,x)):
        print(f"left: y_walker: {y_walker}")
        label_mask[feature_indices, y_walker] = tag_id
        # # plt.close()
        # myplot = plt.imshow(mask, aspect='auto')
        # # plt.plot(21, 54,'ro')
        # plt.scatter(np.where(label_mask==0)[1], np.where(label_mask==0)[0],c='r', s=2)
        # plt.scatter(np.where(label_mask==1)[1], np.where(label_mask==1)[0],c='g', s=2)
        # ims.append([myplot])
  tag_id+=1


import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

class LoopingPillowWriter(PillowWriter):
    def finish(self):
        self._frames[0].save(
            self._outfile, save_all=True, append_images=self._frames[1:],
            duration=int(1000 / self.fps), loop=0)

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=500)

writer = PillowWriter(fps=20)
writer = 'imagemagick'
ani.save("demo2.gif", writer=writer)
ani.save('demo2.gif', writer=LoopingPillowWriter(fps=20)) 


for img in ims:
  img
  plt.show()

# Iterate over features to sum intensities
for label_id in np.unique(label_mask)[np.logical_not(np.isnan(np.unique(label_mask)))]:
  print(f"Feature {label_id} has a total intensity of {np.sum(arr[label_mask==label_id])}")

mask[np.ix_(range(59, 62), range(22, 25))]
mask[np.ix_(range(58, 63), range(18, 26))]
label_mask[np.ix_(range(58, 63), range(18, 26))]

mask[np.ix_(range(39, 53), range(9, 15))]
label_mask[np.ix_(range(39, 53), range(9, 20))]

mask[np.ix_(range(52, 58), range(8, 15))]
label_mask[np.ix_(range(40, 60), range(12, 23))]

mask[np.ix_(range(38, 56), range(10, 17))]
label_mask[np.ix_(range(39, 60), range(9, 20))]

pd.DataFrame({'x':mask[60,], 'y':label_mask[60,]})
pd.DataFrame({'x':mask[40,], 'y':label_mask[40,]})
pd.DataFrame({'x':mask[i,], 'y':label_mask[i,]})

plt.close()
plt.imshow(mask, aspect='auto')
# plt.plot(21, 54,'ro')
plt.scatter(np.where(label_mask==0)[1], np.where(label_mask==0)[0],c='r', s=2)
plt.scatter(np.where(label_mask==1)[1], np.where(label_mask==1)[0],c='g', s=2)
plt.show()

plt.close()
plt.imshow(mask[46:54,], aspect='auto')
plt.plot(21, 2,'ro')
plt.show()

plt.close()
plt.imshow(labeled, aspect='auto')
plt.show()

def start_stop(a, trigger_val):
    # "Enclose" mask with sentients to catch shifts later on
    mask = np.r_[False,np.equal(a, trigger_val),False]

    # Get the shifting indices
    idx = np.flatnonzero(mask[1:] != mask[:-1])

    # Get the start and end indices with slicing along the shifting ones
    return zip(idx[::2], idx[1::2]-1)




# for row in range(0,mask.shape[0]):
#     plt.close()
#     plt.imshow(mask[50:80,], aspect='auto')
#     plt.show()
#     
    
plot_2d_qaunt_results_check(arr, arr_blur, i, j, masked, mask, label_mask, fname=f"{filter_peptides[0]}_2D_Quant_check.png" )

def plot_2d_qaunt_results_check(arr, arr_blur, i, j, masked, mask, label_mask, fname ):
  """
  
  """
  # Get unique feature labels
  unique_feature_labels = np.unique(label_mask)[np.logical_not(np.isnan(np.unique(label_mask)))]
  # Generate a palette of n unique feature label colors
  palette = sns.color_palette("Dark2", len(unique_feature_labels))
  plt.close()
  fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2,3, figsize=(20, 20), sharex=True, sharey=True)
  ax1.imshow(arr, aspect='auto', cmap="afmhot_r")
  ax1.set_title('Original')
  ax2.imshow(arr_blur, aspect='auto', cmap="afmhot_r")
  ax2.set_title('Smoothed')
  ax3.imshow(arr, aspect='auto', cmap="afmhot_r")
  ax3.set_title('Seeds')
  # plt.imshow(image, origin='lower', aspect='auto')
  ax3.plot(i,j,'go', markersize=5, alpha=0.8)
  ax4.imshow(masked, 'jet', interpolation='none', alpha=0.7, aspect='auto')
  ax4.set_title('Smoothed\nMask')
  ax5.imshow(mask, aspect='auto')
  for label, col in zip(unique_feature_labels, palette):
    ax5.scatter(np.where(label_mask==label)[1], np.where(label_mask==label)[0],color=col, s=2)
  ax5.set_title('Labeled\nMask')
  ax6.imshow(arr, aspect='auto', cmap="afmhot_r")
  for label, col in zip(unique_feature_labels, palette):
    ax6.scatter(np.where(label_mask==label)[1], np.where(label_mask==label)[0],color=col, s=2)
  ax6.set_title('Labeled\nFeature')
  for y, x, label, col in zip(i, j, unique_feature_labels, palette):
      ax6.text(y, x, str(int(label)), color="white", fontsize=6, bbox=dict(fill=False, edgecolor="black", linewidth=1.5))
  plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.5)
  plt.show()
  # Save Figure
  fig.savefig(fname, dpi=fig.dpi)

data
filter_peptides = ["YVC(UniMod:4)EGPSHGGLPGASS(UniMod:21)EK"]
filter_charge_state = 2
ms_level=1

# Filter for ms1 level data
data_ms1 = data.loc[(data.ms_level==ms_level)]
data_ms1['peptide_group'] = data_ms1.peptide.astype(str) + "_" + data_ms1.charge.astype(str)

unique_peptide_charge = np.unique(data_ms1['peptide_group'])

for filter_peptides in unique_peptide_charge:
  data_filt = data_ms1.loc[(data_ms1.peptide_group.isin(filter_peptides))]
  
  arr = data_filt.pivot_table(index='im', columns='rt', values='int').to_numpy()
