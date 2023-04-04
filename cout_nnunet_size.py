
import os
import torch
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
from nnunetv2.training.nnUNetTrainer.nnUNetTrainer import nnUNetTrainer
from nnunetv2.utilities.plans_handling.plans_handler import PlansManager, ConfigurationManager
from nnunetv2.utilities.get_network_from_plans1 import get_network_from_plans
from batchgenerators.utilities.file_and_folder_operations import load_json
#import tensorflow as tf
#physical_devices = tf.config.list_physical_devices('GPU')
#tf.config.experimental.set_memory_growth(physical_devices[0],True)
#from nnunet.training.model_restore import restore_model

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

#pkl = "/home/hln0895/nnUNet/nnUNet_trained_models/nnUNet/3d_fullres/Task666_LA/nnUNetTrainerV2__nnUNetPlansv2.1/fold_4/model_best.model.pkl"
#checkpoint = pkl[:-4]
#train = False
#trainer = restore_model(pkl, checkpoint, train)
#a=count_parameters(trainer.network)/1000000   
#model_path = "/home/hln0895/nnUNet/nnUNet_results/Dataset666_LA/nnUNetTrainer__nnUNetPlans__3d_fullres/fold_1/checkpoint_best.pth"
#content= torch.load(model_path)
#print(content['network_weights'].keys())
plan_path = "/home/hln0895/nnUNet/nnUNet_results/Dataset666_LA/nnUNetTrainer__nnUNetPlans__3d_fullres/plans.json"
plans = PlansManager(plan_path)
configuration='3d_fullres'
configuration_manager = plans.get_configuration(configuration)
#trainer = nnUNetTrainer(plans="/home/hln0895/nnUNet/nnUNet_results/Dataset666_LA/nnUNetTrainer__nnUNetPlans__3d_fullres/plans.json",dataset_json="/home/hln0895/nnUNet/nnUNet_results/Dataset666_LA/nnUNetTrainer__nnUNetPlans__3d_fullres/dataset.json",configuration='3d_fullres',fold =2)
#a=count_parameters(model)/1000000 
#a=model.num_parameters()
#a=count_parameters(trainer.network)/1000000
#print(a)
dataset_json_path="/home/hln0895/nnUNet/nnUNet_results/Dataset666_LA/nnUNetTrainer__nnUNetPlans__3d_fullres/dataset.json"
dataset_json = load_json(dataset_json_path)
model=get_network_from_plans(plans, dataset_json, configuration_manager,
                                      num_input_channels=1)
a=count_parameters(model)/1000000
print(a)