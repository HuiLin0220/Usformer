# Usformer: A Small Network for Left Atrium Segmentation of 3D LGE MRI
Code for two papers: 
(1) 
(2) Usformer: A Small Network for Left Atrium Segmentation of 3D LGE MRI.
[Video](https://www.youtube.com/watch?v=4Mu5rgfUwoE)
[Slides](https://drive.google.com/file/d/1pWzuMKeXzwozWLsFPUuOCRv1JYvT-KXy/view)

## Dataset


## Instructions
- [Installation instructions]

        git clone https://github.com/HuiLin0220/Usformer.git
        cd Usformer
        pip install -e.
- [Usformer](nnunetv2/dynamic_network_architectures/architectures/unet.py) A new architecture, Usformer, is created here.
- [Architecture hyperparameters](nnunetv2/utilities/get_network_from_plans.py) Edit architecture hyperparameters in Function 'get_network_from_plans'.
- [Edit Usformer]  
      Refer to nnU-Net's [Extending nnU-Net](documentation/extending_nnunet.md)  
      [Image normalization](documentation/explanation_normalization.md)

## Oversampling
-oversample_foreground_percent of patches must contain LA
-num_iterations_per_epoch * batch_size * oversample_foreground_percent patches must contain LA

## Example Results
<img align="left" width="252" height="180" src="/results/P20.gif"> A case with median performance in terms of Dice scores in the challenge dataset.

Green lines: prediction

Red lines: groundtruth

## References and Acknowledgements:
Usformer is developed on the [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) framework. The  Left Atrium Segmentation project is funded by

Yellow: slice index




## To-do lists
     

