# Usformer
A new architecture, Usformer, based on the [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) framework for LA segmentation.

## References and Acknowledgements:

Hui Lin, Santiago Lopez Tapia, Florian Schiffers, Yunan Wu, Huili Yang, Nikolay Iakovlev, Bradley D. Allen, Ryan Avery, Daniel C. Lee, Daniel Kim, Aggelos K. Katsaggelos. Usformer: A Light Neural Network for Left Atrium Segmentation of 3D LGE MRI. EUSIPCO, 2023.  (waiting to be online)

## Instructions
- [Installation instructions]  
      Refer to nnU-Net's [Installation instructions](documentation/installation_instructions.md).

      git clone git clone https://github.com/HuiLin0220/Usformer.git
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

Yellow: slice index




## To-do lists
     

