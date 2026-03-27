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

what is lin_reg_bin , when it is created

Will ML Engineer change the code , is he a production support ?


#### day 2 steps
mkdir day_2 ; cd day_2
uv init --lib --python 3.10 duration_pred_serve
cd duration_pred_serve



add dependices from day 1:
uv add scikit-learn==1.2.2 numpy==1.26.4

add testing and loggin dependencide

uv add pytest loguru

add webserver dependency : `uv add "fastapi[standard]"`
- add requests dependence `uv add --dev requests`
- copy model over from day 



### ping example for fastAPI
- create a ping.py file inside of src/duration_pred_serve and open it
- change the python virtual env to use the correct day 2 env ( assume python plugin is installed , bottom right there is python evn , click browse select day2.../bin/python)


-- run fastapi and click on the url provided in the 

uv run fastapi dev src/duration_pred_serve/ping.py

create file serve.py under src/dur...


uv run python src/duration_pred_serve/serve.py

uv run python src/duration_pred_serve/serve.py