# Usformer
A new architecture, Usformer, based on the [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) framework for LA segmentation.

Please cite the following papers when using Usformer:

    [1] Hui Lin, Santiago Lopez Tapia, Florian Schiffers, Yunan Wu, Huili Yang, Nikolay Iakovlev, Bradley D. Allen, Ryan Avery, Daniel C. Lee, Daniel Kim, Aggelos K. Katsaggelos. 
    Usformer: A Light Neural Network for Left Atrium Segmentation of 3D LGE MRI. EUSIPCO, 2023.  (waiting to be online)
    
    [2] Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., & Maier-Hein, K. H. (2021). 
    nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature Methods, 18(2), 203-211.  
    
        @article{isensee2021nnu,
          title={nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation},
          author={Isensee, Fabian and Jaeger, Paul F and Kohl, Simon AA and Petersen, Jens and Maier-Hein, Klaus H},
          journal={Nature methods},
          volume={18},
          number={2},
          pages={203--211},
          year={2021},
          publisher={Nature Publishing Group US New York}
        }

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

## Results
<img align="left" width="346" height="247" src="/results/P20.gif"> A case with median performance in terms of Dice scores in the challenge dataset.
Green lines: prediction
Red lines: groundtruth
Yellow: slice index
     

