#### MLOPS




#### day 1 seps

mkdir day_1
cd day_1
````
mkdir notebooks
cd notebooks
wget https://raw.githubusercontent.com/ynotzort/2025-07-mle-workshop/refs/heads/main/day_1/notebooks/duration-prediction-starter.ipynb

````

# how to install uv
curl -LsSf https://astral.sh/uv/install.sh | sh



We are given notebook from Datasceitinst
As machine learning engineer we need to make it production ready


cd .. 
( under day_1 folder)

uv init --python 3.10
run

fix the version 
-- select .py file , select the python from bottom right , browse .venv , python

### install dependencies
- `uv add scikit-learn==1.2.2 pandas pyarrow`
uv add --dev jupyter seaborn

uv run jupyter notebook


fix numpy issue
uv add numpy==1.26.4

uv run jupyter nbconvert --to-script notebooks/duration-prediction-starter.ipynb

#### question

what was the exact issue with python version 

install the python extension for version to be visible