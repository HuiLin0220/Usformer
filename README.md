# Usformer
A new architecture, Usformer, based on the nnU-Net framework for LA segmentation

Please cite the [following papers](https://www.google.com/url?q=https://www.nature.com/articles/s41592-020-01008-z&sa=D&source=docs&ust=1677235958581755&usg=AOvVaw3dWL0SrITLhCJUBiNIHCQO) and when using Usformer:

    Hui Lin, Santiago Lopez Tapia, Florian Schiffers, Yunan Wu, Huili Yang, Nikolay Iakovlev, Bradley D. Allen, Ryan Avery, Daniel C. Lee, Daniel Kim, Aggelos K. Katsaggelos. 
    Usformer: A Light Neural Network for Left Atrium Segmentation of 3D LGE MRI. EUSIPCO, 2023.
    Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., & Maier-Hein, K. H. (2021). 
    nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.

## Instructions
- [Installation instructions](documentation/installation_instructions.md) to install nnU-Net.
- [UNetrasformer3D](nnunetv2/dynamic_network_architectures/architectures/unet.py) A new architecture 'UNetrasformer3D' is created here.
- [Architecture hyperparameters](nnunetv2/utilities/get_network_from_plans.py) Edit architecture hyperparameters in Function 'get_network_from_plans'.
- [Edit nnU-Net](documentation/extending_nnunet.md)

## Oversampling
-oversample_foreground_percent of patches must contain LA
-num_iterations_per_epoch * batch_size * oversample_foreground_percent patches must contain LA
