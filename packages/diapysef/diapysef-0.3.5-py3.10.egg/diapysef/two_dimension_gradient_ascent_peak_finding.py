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
arr = [ [ 10, 8, 10, 10 ],
        [ 14, 13, 12, 11 ],
        [ 15, 9, 11, 21 ],
        [ 16, 17, 19, 20 ] ]
        
filter_peptides = ["VS(UniMod:21)YDVTSAR"]#, "VSYDVT(UniMod:21)SAR"]
filter_charge_state = 2
ms_level=1

# Load data from tsv
data = pd.read_csv("extracted_data.tsv", sep="\t")

data_filt = data.loc[(data.peptide.isin(filter_peptides)) & (data.charge==filter_charge_state) & (data.ms_level==ms_level)]

arr = data_filt.pivot_table(index='im', columns='rt', values='int').to_numpy()

plt.close()
plt.imshow(arr, aspect='auto')
plt.colorbar()
plt.plot(np.concatenate(x_list),np.concatenate(y_list),'ro') 
plt.show()
 
# Number of Columns
rows = arr.shape[0]
columns = arr.shape[1]
peaks = findPeak(arr, rows, columns)

int_list = []
x_list = []
y_list = []
for pk in peaks:
  int_list.append(pk[0])
  x_list.append(pk[1])
  y_list.append(pk[2])

