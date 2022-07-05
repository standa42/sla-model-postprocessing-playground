# sla_model_postprocessing_playground
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

## Running the app

```
# run the gui
python ./bin/app.py
```

## Adding .sl1 model

At the moment, only files located in ./sl1_files/ are loaded into application