# sla-model-postprocessing-playground
Testing various approaches for postprocessing 3d model for SLA printer to achieve better print quality

## Installation
```
# clone this repository
git clone https://github.com/standa42/sla-model-postprocessing-playground.git

# switch to project folder
cd sla-model-postprocessing-playground

# install dependencies
pipenv install 

# install local package
pipenv install -e .
```

## Running the script

```
# put .sl1 file into folder //sla-model-postprocessing-playground/sl1_files/

# activate environment
pipenv shell

# run the script with model and method parameters
# --model is the name of the model in //sl1_files/ folder
# --method is one of the following model transformations: ["identity", "antialising_supersampling", "median_filter"]
# the output will be in folder //sla-model-postprocessing-playground/output/ in a folder with logged name containing model_method_random_hash
python .\bin\sl1_transform.py --model="Aliaser.sl1" --method="identity"
```

## Adding .sl1 model for processing

At the moment, only files located in ./sl1_files/ are loaded into application