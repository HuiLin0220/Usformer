# Usformer: A Small Network for Left Atrium Segmentation of 3D LGE MRI
Mode details are presented in the following papers, [Video](https://www.youtube.com/watch?v=4Mu5rgfUwoE), and [Slides](https://drive.google.com/file/d/1pWzuMKeXzwozWLsFPUuOCRv1JYvT-KXy/view): 

(1) [Usformer: A Light Neural Network for Left Atrium Segmentation of 3D LGE MRI](https://ieeexplore.ieee.org/abstract/document/10289839)

(2) [Usformer: A Small Network for Left Atrium Segmentation of 3D LGE MRI](https://doi.org/10.1016/j.heliyon.2024.e28539)






## Dataset

[To obtain the 2018 Atria Segmentation challenge dataset](https://www.cardiacatlas.org/atriaseg2018-challenge/atria-seg-data/)


## Instructions
- [Installation]

        git clone https://github.com/HuiLin0220/Usformer.git
        cd Usformer
        pip install -e.
- Usformer's [architecture](nnunetv2/dynamic_network_architectures/architectures/unet.py) and [plan](network_plan/Usformer_5M.json).
- [Training]
- [Test]

## Median Performance
<img align="left" width="252" height="180" src="/results/challenge_dataset.gif"> A case with median performance in terms of Dice scores in the challenge dataset.

Green lines: prediction

Red lines: groundtruth

Yellow: slice index

More results in two datasets:
[challenge dataset](https://ars.els-cdn.com/content/image/1-s2.0-S2405844024045705-mmc1.mp4)
[NU dataset](https://ars.els-cdn.com/content/image/1-s2.0-S2405844024045705-mmc2.mp4)

## References and Acknowledgements:
Usformer is developed on the [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) framework. The  Left Atrium Segmentation project is funded by
     

