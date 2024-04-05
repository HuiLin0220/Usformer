import torch
from nnunetv2.inference.predict_from_raw_data import predict_from_raw_data as predict


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # if torch.cuda.is_available() else 'cpu'
print(f'cuda is available' if torch.cuda.is_available() else 'cpu')


input_path = PATH_TO_INPUT
output_path = PATH_TO_OUTPUT
weight_path= PATH_TO_WEIGHT

config = "./dataset_model_config/" #where to store model plans and dataset json files

predict(input_path, output_path, config, [0], 0.5,use_gaussian=True,use_mirroring=True,perform_everything_on_gpu=True,verbose=True,save_probabilities=False,overwrite=False,checkpoint_name=weight_path,num_processes_preprocessing=1,num_processes_segmentation_export=1,device = device)
