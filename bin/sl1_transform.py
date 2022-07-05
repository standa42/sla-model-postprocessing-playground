import os
import sys
from time import sleep
import zipfile
import argparse
import uuid
from os import listdir
from os.path import isfile, join
from collections import namedtuple

from src.helper_functions import safe_mkdir, safe_mkdir_clean

from PIL import Image, ImageFilter 

# command line argument parsing
# two main arguments model and method
parser = argparse.ArgumentParser(description='Transformation script for .sl1 models')
parser.add_argument('--model', type=str, default="Prusa_SL1_Calibration_test_2H_40M_50um_Prusa_Orange.sl1", help='Transformed model file')
parser.add_argument('--method', type=str, default="median_filter", help='Method used for transformation')
args = parser.parse_args()

print(f"Script arguments are:")
print(f"{vars(args)}")

supported_methods = ["identity", "antialising_supersampling", "median_filter"] # "marching_cubes"
if args.method not in supported_methods:
    print("Value of argument method is no valid")
    print(f"Value is {args.method}, but should be in {supported_methods}")
    sys.exit()
    
# unzip model to working directory
model_name = args.model.split('.')[0]
original_model_path = join("./sl1_files/", args.model)
working_folder_path = join("./output/", f"{model_name}_{args.method}_{uuid.uuid4().hex[:6]}/")
safe_mkdir_clean(working_folder_path)

with zipfile.ZipFile(original_model_path, 'r') as zip_ref:
    zip_ref.extractall(working_folder_path)

print(f"Directory with modified model is {working_folder_path}")

# load model layers into memory
# --- list all files in folder
layers_files = [f for f in listdir(working_folder_path) if isfile(join(working_folder_path, f))] 
# --- ending with .png
layers_files = list(filter(lambda f: f[-4:] == ".png", layers_files))

# --- copy layer files into memory and delete them from disk
ModelLayer = namedtuple('ModelLayer', 'name image')
original_layers = []
for layer_file in layers_files:
    layer_file_path = join(working_folder_path, layer_file)
    with Image.open(layer_file_path) as image:
        layer = ModelLayer(layer_file, image.copy())
        original_layers.append(layer)
    os.remove(layer_file_path)

# do layer transformation
print("Transformation started")
counter = 0
transformed_layers = []
if args.method == "identity":
    transformed_layers = original_layers
elif args.method == "antialising_supersampling":
    for layer in original_layers:
        transformed_layer_image = layer.image.copy()
        width, height = transformed_layer_image.size
        transformed_layer_image = transformed_layer_image.resize((width * 3, height * 3), resample=Image.NEAREST )
        transformed_layer_image = transformed_layer_image.resize((width, height), resample=Image.ANTIALIAS)
        transformed_layers.append(ModelLayer(layer.name, transformed_layer_image))
        counter = counter + 1
        if counter % 100 == 0:
            print(f"{counter} images out of {len(original_layers)} transformed")
elif args.method == "median_filter":
    for layer in original_layers:
        transformed_layer_image = layer.image.copy()
        transformed_layer_image = transformed_layer_image.filter(ImageFilter.ModeFilter(size = 3))
        transformed_layers.append(ModelLayer(layer.name, transformed_layer_image))
        counter = counter + 1
        if counter % 100 == 0:
            print(f"{counter} images out of {len(original_layers)} transformed")

# save transformed files 
print("saving images")
for transformed_layer in transformed_layers:
    transformed_layer.image.save(join(working_folder_path, transformed_layer.name))
