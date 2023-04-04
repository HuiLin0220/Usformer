# nnUNet_transformer


Please cite the [following paper](https://www.google.com/url?q=https://www.nature.com/articles/s41592-020-01008-z&sa=D&source=docs&ust=1677235958581755&usg=AOvVaw3dWL0SrITLhCJUBiNIHCQO) when using nnU-Net:

    Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., & Maier-Hein, K. H. (2021). nnU-Net: a self-configuring 
    method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.

## Instructions
- Follow https://github.com/MIC-DKFZ/nnUNet to install nnU-Net
- [UNetrasformer3D](nnUNet_transformer/nnunetv2/dynamic_network_architectures/architectures/unet.py) A new architecture 'UNetrasformer3D' is created
- [Architecture hyperparameters](nnunetv2/utilities/get_network_from_plans.py) Edit architecture hyperparameters in Function 'get_network_from_plans'
- [Edit nnU-Net](documentation/extending_nnunet.md)

