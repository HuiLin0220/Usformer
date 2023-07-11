import os
import torch
from ptflops import get_model_complexity_info

from nnunetv2.utilities.plans_handling.plans_handler import PlansManager, ConfigurationManager
from nnunetv2.utilities.get_network_from_plans1 import get_network_from_plans
from batchgenerators.utilities.file_and_folder_operations import load_json

#os.environ["CUDA_VISIBLE_DEVICES"] = "0"

plan_path = 'path_to_network_plan_file'
plans = PlansManager(plan_path)
configuration = '3d_fullres'
configuration_manager = plans.get_configuration(configuration)
dataset_json_path = 'path_to_dataset_json_file'
dataset_json = load_json(dataset_json_path)

model = get_network_from_plans(plans, dataset_json, configuration_manager,
                                      num_input_channels=1)
macs, params = get_model_complexity_info(model, (1,32, 320,320), as_strings=True,
                                           print_per_layer_stat=False, verbose=True)#input size(1,32, 320,320)
print('{:<30}  {:<8}'.format('Computational complexity: ', macs))
print('{:<30}  {:<8}'.format('Number of parameters: ', params))
