import os
import nibabel as nib
import nrrd
import pandas as pd 
import numpy as np
from medpy.metric import asd, hd, dc, specificity, sensitivity, true_positive_rate, true_negative_rate

val_path_data = "/home/hln0895/nnUNet/nnUNet_raw/Dataset666_LA/labelsTs/"
_3D_results_path = "/home/hln0895/nnUNet/nnUNet_results/Dataset666_LA/nnUNetTrainer__nnUNetPlans__3d_fullres/fold_4/result/"
#val_path_data = "/mnt/Shared/Corelab_Group/Hui/0LA/data/LA2018/dataset/3D/Testing Set/"   
#_3D_results_path="/mnt/Shared/Corelab_Group/Hui/0LA/trainprocess/3DLA2018/version_50/3D_nrrd/"
a=os.listdir(val_path_data)
a.sort()
name_list = []
num=54
dice_array = np.zeros(num+2)
hd_array=np.zeros(num+2)
specificity_array = np.zeros(num+2)
sensitivity_array = np.zeros(num+2)
asd_array = np.zeros(num+2)

for i in range(num):

    patient_id = 'P'+ str(i+1).zfill(2)
    name_list.append(patient_id)
    print('-----'+patient_id+'-----') 
    #print(a[i])
    patient_label_path = val_path_data + a[i]
    imgfile = nib.load(patient_label_path)#h, w, z
    mask = imgfile.get_fdata()
    
    prediction_path = _3D_results_path + a[i]
    imgfile = nib.load(prediction_path)#h, w, z
    prediction_bsl = imgfile.get_fdata()
    
    dice_array[i]=dc(prediction_bsl, mask)*100
    
    hd_array[i] = hd(prediction_bsl, mask,voxelspacing=[1, 1, 1])
    specificity_array[i] = specificity(prediction_bsl, mask)*100
    sensitivity_array[i] = sensitivity(prediction_bsl, mask)*100
    asd_array[i] = asd(prediction_bsl, mask,voxelspacing=[1, 1, 1])
'''

for i in range(num):

    patient_id = 'P'+ str(i+1).zfill(2)
    name_list.append(patient_id)
    print('-----'+patient_id+'-----') 
    
    patient_label_path = val_path_data + a[i]+'/laendo.nrrd'
    mask, mask_header  = nrrd.read(patient_label_path)

    prediction_path = _3D_results_path + a[i]+'_pre.nrrd'
    prediction_bsl, prediction_bsl_header  = nrrd.read(prediction_path)
    
    dice_array[i]=dc(prediction_bsl, mask)*100
    
    hd_array[i] = hd(prediction_bsl, mask,voxelspacing=[1, 1, 1])
    specificity_array[i] = specificity(prediction_bsl, mask)*100
    sensitivity_array[i] = sensitivity(prediction_bsl, mask)*100
    asd_array[i] = asd(prediction_bsl, mask,voxelspacing=[1, 1, 1])
'''
name_list.append('mean')
name_list.append('std')
    
dice_array[num]=np.mean(dice_array[:num])
dice_array[num+1]=np.std(dice_array[:num])
  
hd_array[num]=np.mean(hd_array[:num])
hd_array[num+1]=np.std(hd_array[:num])
    
    
specificity_array[num]=np.mean(specificity_array[:num])
specificity_array[num+1]=np.std(specificity_array[:num])
    
    
sensitivity_array[num]=np.mean(sensitivity_array[:num])
sensitivity_array[num+1]=np.std(sensitivity_array[:num])
    
asd_array[num]=np.mean(asd_array[:num])
asd_array[num+1]=np.std(asd_array[:num])
  
df = pd.DataFrame({'name':name_list, 'dice(%)':dice_array, 'specificity(%)':specificity_array, 'sensitivity':sensitivity_array,'hd(mm)':hd_array,'average surface to surface distance(mm)':asd_array})

print("DICE: %.2f +-%.2f%%" % (dice_array[-2],dice_array[-1]))
df.to_csv("/home/hln0895/nnUNet/nnUNet_results/Dataset666_LA/nnUNetTrainer__nnUNetPlans__3d_fullres/fold_4/" +  'results.csv')
