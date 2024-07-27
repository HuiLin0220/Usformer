[![arXiv](https://img.shields.io/badge/arXiv-2311.12437-blue)]https://doi.org/10.1016/j.heliyon.2024.e28539)
 [![cite](https://img.shields.io/badge/cite-BibTex-yellow)]()
[![website](https://img.shields.io/badge/Challenge%20website-50d13d)](https://arcade.grand-challenge.org/)


[![arXiv]](https://doi.org/10.1016/j.heliyon.2024.e28539) [![video](https://img.shields.io/badge/video-YouTube-red)](https://www.youtube.com/watch?v=4Mu5rgfUwoE)
# Usformer: A Small Network for Left Atrium Segmentation of 3D LGE MRI
More details are presented in the following papers, [Video](https://www.youtube.com/watch?v=4Mu5rgfUwoE), and [Slides](https://drive.google.com/file/d/1pWzuMKeXzwozWLsFPUuOCRv1JYvT-KXy/view): 

If you find our work is useful in your research, please consider citing:

(1) [Usformer: A Light Neural Network for Left Atrium Segmentation of 3D LGE MRI](https://ieeexplore.ieee.org/abstract/document/10289839)
```bash
@inproceedings{lin2023usformer,
  title={Usformer: A Light Neural Network for Left Atrium Segmentation of 3D LGE MRI},
  author={Lin, Hui and Tapia, Santiago Lopez and Schiffers, Florian and Wu, Yunan and Yang, Huili and Iakovlev, Nikolay and Allen, Bradley D and Avery, Ryan and Lee, Daniel C and Kim, Daniel and others},
  booktitle={2023 31st European Signal Processing Conference (EUSIPCO)},
  pages={995--999},
  year={2023},
  organization={IEEE}
}
```
(2) [Usformer: A Small Network for Left Atrium Segmentation of 3D LGE MRI](https://doi.org/10.1016/j.heliyon.2024.e28539)
```bash
@article{lin2024usformer,
  title={Usformer: A Small Network for Left Atrium Segmentation of 3D LGE MRI},
  author={Lin, Hui and L{\'o}pez-Tapia, Santiago and Schiffers, Florian and Wu, Yunan and Gunasekaran, Suvai and Hwang, Julia and Bishara, Dima and Kholmovski, Eugene and Elbaz, Mohammed and Passman, Rod S and others},
  journal={Heliyon},
  publisher={Elsevier}
}
```



## Dataset

[To obtain the 2018 Atria Segmentation challenge dataset](https://www.cardiacatlas.org/atriaseg2018-challenge/atria-seg-data/)


## Instructions
- [Installation]
```bash
git clone https://github.com/HuiLin0220/Usformer.git
cd Usformer
pip install -e.
```
- Usformer's [architecture](nnunetv2/dynamic_network_architectures/architectures/unet.py), [plan](dataset_model_config/plan.json), and weight ([Google drive](https://drive.google.com/file/d/1CS6mGbT85mCE4MF28Guiic_G6d1r6oe1/view?usp=sharing)).
  
- [Test]
  
  Challenge dataset's [configuration plan](dataset_model_config/dataset.json)
```bash
  python ./test.py
```
  

## Median Performance
<img align="left" width="252" height="180" src="/results/challenge_dataset.gif"> A case with median performance in terms of Dice scores in the challenge dataset.

Green lines: prediction

Red lines: groundtruth

Yellow: slice index

More results in two datasets:
[challenge dataset](https://ars.els-cdn.com/content/image/1-s2.0-S2405844024045705-mmc1.mp4)
[NU dataset](https://ars.els-cdn.com/content/image/1-s2.0-S2405844024045705-mmc2.mp4)

## References and Acknowledgements:
Usformer is developed on the [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) framework. The  Left Atrium Segmentation project is funded by the American Heart Association and the National Institutes of Health. Any questions, please email huilin2023@u.northwestern.edu
     

