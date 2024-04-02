# Usformer: A Small Network for Left Atrium Segmentation of 3D LGE MRI
Usformer is developed based on the [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) framework.

## References and Acknowledgements:

      @article{Usformer,
      title = {Usformer: A Small Network for Left Atrium Segmentation of 3D LGE MRI},
      journal = {Heliyon},
      pages = {e28539},
      year = {2024},
      issn = {2405-8440},
      doi = {https://doi.org/10.1016/j.heliyon.2024.e28539},
      url = {https://www.sciencedirect.com/science/article/pii/S2405844024045705},
      author = {Hui Lin and Santiago López-Tapia and Florian Schiffers and Yunan Wu and Suvai Gunasekaran and Julia Hwang and Dima Bishara and Eugene Kholmovski and Mohammed             Elbaz and Rod S. Passman and Daniel Kim and Aggelos K. Katsaggelos},
      }

## Instructions
- [Installation instructions]  
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
     

