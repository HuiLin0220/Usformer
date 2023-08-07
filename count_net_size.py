
from ptflops import get_model_complexity_info

import os
import torch
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
from nnunetv2.utilities.plans_handling.plans_handler import PlansManager, ConfigurationManager
from nnunetv2.utilities.get_network_from_plans1 import get_network_from_plans
from batchgenerators.utilities.file_and_folder_operations import load_json

#plan_path = "/home/hln0895/nnUNet/nnUNet_preprocessed/Dataset666_LA/nnUNetPlans.json"#"/home/hln0895/nnUNet/nnUNet_results/Dataset666_LA/nnUNetTrainer__nnUNetPlans__3d_fullres/fold_4_5M/result/plans.json"#"/home/hln0895/nnUNet/nnUNet_preprocessed/Dataset666_LA/nnUNetPlans.json"
plan_path="/home/hln0895/nnUNet/nnUNet_results/Dataset777_LA/nnUNetTrainer__nnUNetPlans__3d_fullres/fold_0/result/plans.json"#"/home/hln0895/nnUNet/nnUNet_preprocessed/Dataset888_LA/nnUNetPlans.json"
plans = PlansManager(plan_path)
configuration='3d_fullres'
configuration_manager = plans.get_configuration(configuration)

dataset_json_path="/home/hln0895/nnUNet/nnUNet_results/Dataset666_LA/nnUNetTrainer__nnUNetPlans__3d_fullres/dataset.json"
dataset_json = load_json(dataset_json_path)
model=get_network_from_plans(plans, dataset_json, configuration_manager,
                                      num_input_channels=1)
macs, params = get_model_complexity_info(model, (1,32, 320,320), as_strings=True,
                                           print_per_layer_stat=False, verbose=True)
print('{:<30}  {:<8}'.format('Computational complexity: ', macs))
print('{:<30}  {:<8}'.format('Number of parameters: ', params))
