import os
from typing import Tuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import ceil
import copy
import click
import plotting 
import util

DEBUG=False
if DEBUG:
  filter_peptides = ["VS(UniMod:21)YDVTSAR"]#, "VSYDVT(UniMod:21)SAR"]
  filter_peptides = ["T(UniMod:21)ELISVSEVHPSR"]
  filter_peptides = ["Y(UniMod:21)VC(UniMod:4)EGPSHGGLPGASSEK"]
  filter_charge_state = 2
  ms_level=1
  
  # Load data from tsv
  data = pd.read_csv("extracted_data.tsv", sep="\t")
  
  data_filt = data.loc[(data.peptide.isin(filter_peptides)) & (data.charge==filter_charge_state) & (data.ms_level==ms_level)]
  
  arr = data_filt.pivot_table(index='im', columns='rt', values='int').to_numpy()
  
def get_std(two_d_array: np.array) -> float:
  """Compute standard deviation of flattened 2D array"""
  # See: https://stackoverflow.com/questions/16842823/peak-detection-in-a-noisy-2d-array
  return np.std(two_d_array)

def get_max(two_d_array: np.array, sigma: float, alpha: int=3.5, size: int=20) -> tuple[list, list]:
  """
  Identify peaks in a 2D array

  Parameters:
    two_d_array: (np.array) A 2D array of intensities
    sigma: (float) A value representing amount of noise in the 2D array
    alpha: (int) A scalar to multiply by sigma (noise) for thresholding when searching for peaks
    size: (int) A scalar to generate a square function for removing a found peak +/- size around to avoid finding the same peak again

  Return:
    Returns a tuple of two lists, containing coordinates of identified peaks.
  """
  # See: https://stackoverflow.com/questions/16842823/peak-detection-in-a-noisy-2d-array
  # From stackoverflow: Alejandro
  # The first part is to get some information about the noise in the image. I did it by computing the standard deviation of the full image (actually is better to select an small rectangle without signal). This is telling us how much noise is present in the image. The idea to get the peaks is to ask for successive maximums, which are above of certain threshold (let's say, 3, 4, 5, 10, or 20 times the noise). This is what the function get_max is actually doing. It performs the search of maximums until one of them is below the threshold imposed by the noise. In order to avoid finding the same maximum many times it is necessary to remove the peaks from the image. In the general way, the shape of the mask to do so depends strongly on the problem that one want to solve. for the case of stars, it should be good to remove the star by using a Gaussian function, or something similar. I have chosen for simplicity a square function, and the size of the function (in pixels) is the variable "size". I think that from this example, anybody can improve the code by adding more general things. 
  
  i_out = []
  j_out = []
  two_d_array_temp = copy.deepcopy(two_d_array)
  while True:
      k = np.argmax(two_d_array_temp)
      j, i = np.unravel_index(k, two_d_array_temp.shape)
      if(two_d_array_temp[j,i] >= alpha*sigma):
          i_out.append(i)
          j_out.append(j)
          x = np.arange(i-size, i+size)
          y = np.arange(j-size, j+size)
          xv,yv = np.meshgrid(x,y)
          two_d_array_temp[yv.clip(0,two_d_array_temp.shape[0]-1), xv.clip(0,two_d_array_temp.shape[1]-1) ] = 0
          # print(xv)
      else:
          break
  return i_out, j_out

def compute_otsu_threshold(arr: np.array) -> float:
  """
  Compute Otsu's threshold
  Implementation adapted from: https://learnopencv.com/otsu-thresholding-with-opencv/

  Parameters:
    arr: (np.array) A 2D array of intensities
  
  Return:
    (float) Otsu's threshold
  """
  hist, bin_edges = np.histogram(arr, bins=256, range=(0, np.nanmax(arr)))
  
  # Get normalized histogram if it is required
  is_normalized = True
  if is_normalized:
      hist = np.divide(hist.ravel(), hist.max())

  # Calculate centers of bins
  bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.

  # Iterate over all thresholds (indices) and get the probabilities w1(t), w2(t)
  weight1 = np.cumsum(hist)
  weight2 = np.cumsum(hist[::-1])[::-1]

  # Get the class means mu0(t)
  mean1 = np.cumsum(hist * bin_mids) / weight1
  # Get the class means mu1(t)
  mean2 = (np.cumsum((hist * bin_mids)[::-1]) / weight2[::-1])[::-1]

  inter_class_variance = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

  # Maximize the inter_class_variance function val
  index_of_max_val = np.argmax(inter_class_variance)

  threshold = bin_mids[:-1][index_of_max_val]
  
  return threshold

def check_connection(bool_vector: np.array, gaps: int, seed: tuple[int, int]) -> np.array:
  """
  Check the connection between values of true in logical vector

  Parameters:
    bool_vector: (np.array) A 1D logcal array  representing a single slice of the 2D mask array.
    gaps: (int) The number of gaps allowed between consecutive true values in bool_vector, to separate between noise or another potential feature.
    seed: (tuple[int, int]) A tuple of two intergers representing x and y coordindates for seed starting point.

  Return:
    (np.array) Returns an array of intergers representing indexes that belong to current seed feature
  """
  # Get all indices where true
  feature_indices = np.where(bool_vector)[0]
  # Compute whether indices are sequential
  indice_lag_difference = feature_indices[list(range(1, feature_indices.shape[0]))] - feature_indices[list(range(0, feature_indices.shape[0]-1))]
  # Compute a list of sequential true feature indexes
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
  # TODO: Find the max diagonal indexes in either direction?
  current_feature_indices = [seed[1] in single_feature_list or abs(seed[1] - np.max(single_feature_list)) < 10 for single_feature_list in feature_index_list]
  if any(current_feature_indices):
    indice_list = feature_index_list[int(np.where(current_feature_indices)[0])]
  else:
    indice_list = []
  return np.array(indice_list)

def check_adjacent_feature_connection(mask_subset: np.array, label_mask_subset: np.array, gaps: int, seed: tuple[int, int]) -> bool:
  """
  Check whether adjacent logical values are true and connected to current

  Paramaters:
    mask_subset: A subset (n x m') logical mask array
    label_mask_subset: A subset (n x m') array with nans and labels, to check if adjacent cells are labelled
    gaps: (int) The number of gaps allowed between consecutive true values in bool_vector, to separate between noise or another potential feature.
    seed: (tuple[int, int]) A tuple of two intergers representing x and y coordindates for seed starting point.

  Return:
    (logical) Whether adjacent features are connected to the current assessed feature vector or not.
  """
  # Get the first boolean True index, where there is at least x consecutive true, and not a random noise true
  first_index = check_connection(mask_subset[:, ceil(mask_subset.shape[1]/2)-1], gaps, seed)
  if first_index.shape[0]==0:
    return False
  target_coord_mask_surroundings = mask_subset[list(range(first_index[0]-gaps, first_index[0]+gaps+1)), :]
  target_coord_label_mask_surroundings = label_mask_subset[list(range(first_index[0]-gaps, first_index[0]+gaps+1)), :]
  return (np.logical_not(np.sum(target_coord_mask_surroundings, 1)[0]==0) or \
          np.logical_not(np.all(np.isnan(target_coord_label_mask_surroundings)))) and \
          np.logical_not(np.all([np.all(coord_mask==coord_label) for coord_mask, coord_label in zip(np.where(target_coord_mask_surroundings), np.where(np.logical_not(np.isnan(target_coord_label_mask_surroundings))))]))

def check_dim_constraint(buffer_size: int, arr_shape: int) -> int:
  """
  Check whether a padding buffer end point is within the shape range of the 2D shape

  Parameters:
    buffer_size: (int) The padding size to take a small subset of an array.
    arr_shape: (int) The dimension size of one side of the array.

  Return:
    Either return the buffer size if still in constraint of arr shape, or return the shape of the array as the max padding size
  """
  if (arr_shape > 0 and buffer_size > arr_shape ) | (arr_shape==0 and buffer_size < arr_shape):
    return(arr_shape)
  else:
    return(buffer_size)

def mask_feature_labeller(mask: np.array, i: list[int], j: list[int], gaps: int=5) -> np.array:
  """
  Label features in a boolean mask

  Parameters:
    mask:  (np.array) A (n x m) 2D  array of trues and falses. 
    i: (list) list of x values for seeds. Obtained from get_max method.
    j: (list) list of y values for seeds. Obtained from get_max method.
    gaps: (int) The number of gaps allowed between consecutive true values in bool_vector, to separate between noise or another potential feature.

  Return:
    (np.array) Return an np.array with labels separating unique features in mask
  """
  # Iterate over seeds
  label_mask = np.empty(mask.shape)
  label_mask.fill(np.nan)
  tag_id = 0
  for x, y in zip(j, i):
    click.echo(f"INFO: Working on seed {x}, {y}")
    
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
    # Label feature for current seed point
    current_feature_indice_list = np.array(feature_list_indices[np.where([True if x in sub_feature_index_list else False for sub_feature_index_list in feature_list_indices ])[0][0]])
    # Check if current_feature_indice_list is already labelled, if this is the case, then it's likely two seeds are present for one feature. So skip this seed
    if np.all(np.isnan(label_mask[current_feature_indice_list, y])):
      label_mask[current_feature_indice_list, y] = tag_id
    else:
      break
        
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
          # click.echo(f"right: y_walker: {y_walker}")
          label_mask[feature_indices, y_walker] = tag_id

    # Walk to the left
    continue_walking_left = True
    y_walker = y-1
    while continue_walking_left:
      if np.sum(mask[:, list(range(check_dim_constraint(y_walker-gaps, 0), y_walker-1))])==0:
        continue_walking_left = False
      if np.any(mask[:, y_walker]):
        feature_indices = check_connection(mask[:,y_walker], gaps, (y,x))
        mask_subset = mask[:,list(range(y_walker-gaps, check_dim_constraint(y_walker+gaps+1, label_mask.shape[1])))]
        label_mask_subset = label_mask[:, list(range(y_walker-gaps, check_dim_constraint(y_walker+gaps+1, label_mask.shape[1])))]
        if check_adjacent_feature_connection(mask_subset, label_mask_subset, gaps, (y,x)):
          # click.echo(f"left: y_walker: {y_walker}")
          label_mask[feature_indices, y_walker] = tag_id
      y_walker-=1
    # Update feature tag id  
    tag_id+=1
  return label_mask

def _two_dimension_quantification(arr: np.array, box_pts: int=6, alpha: int=3, size: int=20, percent_noise: float=0.5, gaps: int=3, fname: str="2D_Quantification_check.png"):
  
  # Smooth data
  arr[np.isnan(arr)] = 0
  kernel = np.ones(box_pts)/box_pts 
  arr_blur = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 0, arr)
  arr_blur = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 1, arr_blur)
  
  # Compute how much noise is in the smoothed 2D array
  sigma = get_std(arr_blur)

  # Get Seeds for features
  # TODO: it seems size plays a big part in deciding how many seeds is in a feature. Need to figure a way to automatically detect this somehow
  
  # max_ints_size = np.concatenate([np.sum(mask, 0).ravel(), np.sum(mask, 1).ravel()])
  # size = ceil(np.mean(max_ints_size[ max_ints_size!=0]))
  i, j = get_max(arr_blur, sigma, alpha=alpha, size=size)
  
  mask_method = 'percent_max_int_noise'
  if mask_method=='percent_max_int_noise':
    # Generate a mask based on thresholding on noise
    max_int = np.mean(arr[j, i])
    threshold = max_int*percent_noise
  elif mask_method=='otsu':
    threshold = compute_otsu_threshold(arr_blur)
    threshold = compute_otsu_threshold(arr)
    # import skimage.filters
    # skimage.filters.threshold_otsu(img[np.logical_not(np.isnan(img))], nbins=256)
  elif mask_method=='hist':
    plt.close("all");
    n, bins, patches = plt.hist(arr, bins=3); 
    # plt.show()
    plt.close("all");
    threshold = np.median(arr[ (arr > bins[1]) & (arr < bins[2]) ])
  mask = arr >= threshold
  kernel = np.ones(box_pts)/box_pts # Here you would insert your actual kernel of any size
  mask_blur = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 0, mask)
  mask_blur = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 1, mask_blur)
  mask_blur[mask_blur>=0.5] = True
  mask_blur[mask_blur<0.5] = False
  mask = mask_blur
  masked = np.ma.masked_where(mask==0, mask)
  
  # Get labelled features
  label_mask = mask_feature_labeller(mask, i, j, gaps)

  for label_id in np.unique(label_mask)[np.logical_not(np.isnan(np.unique(label_mask)))]:
    click.echo(f"INFO: Feature {label_id} has a total intensity of {np.sum(arr[label_mask==label_id])}")

  # Generate a report plot to assess performance
  plotting.plot_2d_qaunt_results_check(arr, arr_blur, i, j, masked, mask, label_mask, fname)


@util.method_timer
def compute_two_dimension_qunatifications():
  data = pd.read_csv("/media/justincsing/ExtraDrive1/Documents2/Roest_Lab/Github/PTMs_Project/synthetic_pool_timstoff/results/thesis_results/diapasef_openswathworkflow_5_scored/extracted_data.tsv", sep="\t")
  ms_level=1

  # Filter for ms1 level data
  data_ms1 = data.loc[(data.ms_level==ms_level)]
  data_ms1['peptide_group'] = data_ms1.peptide.astype(str) + "_" + data_ms1.charge.astype(str)

  unique_peptide_charge = np.unique(data_ms1['peptide_group'])

  for filter_peptides in unique_peptide_charge:
    click.echo(f"INFO: Processing {filter_peptides}...")
    data_filt = data_ms1.loc[(data_ms1.peptide_group.isin([filter_peptides]))]
    arr = data_filt.pivot_table(index='im', columns='rt', values='int').to_numpy()
    # masked_arr = np.ma.masked_equal(arr, 0.0, copy=False)
    # min_nonzero_val = masked_arr.min()
    min_nonzero_val = np.nanmin(arr)
    arr[arr[:,] >= min_nonzero_val]
    _two_dimension_quantification(arr, fname=f"report/{filter_peptides}_2D_Quant_check.png")


compute_two_dimension_qunatifications()
