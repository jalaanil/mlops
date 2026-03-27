
import pandas as pd

import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from loguru import logger


from datetime import date

import argparse



def read_dataframe(filename):
    """
    Reads a Parquet file into Pandas dataframe

    Returns a DataFrame

    Parameters:
    -----------
    filename : str
        The path to the parquet file to be read.

    Returns:
    --------
    pd.DataFrame
        The transformed df

    Notes:
    Function assumes that ...
    """

    try:
        print(f"reading file {filename}")
        df = pd.read_parquet(filename)

        df['duration'] = df.lpep_dropoff_datetime - df.lpep_pickup_datetime
        df.duration = df.duration.dt.total_seconds() / 60

        df = df[(df.duration >= 1) & (df.duration <= 60)]

        categorical = ['PULocationID', 'DOLocationID']
        df[categorical] = df[categorical].astype(str)
        
        return df
    except Exception as e:
        logger.error(f"ERROR : reading {filename} failed")
        logger.error(e)
        raise

def train(train_date: date , val_date: date , out_path: str) -> float:

    base_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year}-{month:02d}.parquet'
    train_url = base_url.format(year=train_date.year , month=train_date.month)
    val_url = base_url.format(year=val_date.year , month=val_date.month)

    df_train = read_dataframe(train_url)
    df_val = read_dataframe(val_url)


    print ( len(df_train), len(df_val) )
    logger.info(f"df_train length is: {len(df_train)}")
    logger.info(f"df_val length is: {len(df_val)}")

    categorical = ['PULocationID', 'DOLocationID']
    numerical = ['trip_distance']

    dv = DictVectorizer()

    train_dicts = df_train[categorical + numerical].to_dict(orient='records')
    val_dicts = df_val[categorical + numerical].to_dict(orient='records')

    target = 'duration'
    y_train = df_train[target].values
    y_val = df_val[target].values

    lr = LinearRegression()
    dv = DictVectorizer()

    pipeline = Pipeline( steps=[("vector" , dv) , ("predictor" , lr)])
    pipeline.fit(train_dicts , y_train )
    y_pred = pipeline.predict ( val_dicts)

    mse= mean_squared_error(y_val, y_pred, squared=False) 
    logger.info( f"mse is {mse}" )

    with open(out_path, 'wb') as f_out:
        #pickle.dump((dv, lr), f_out)
        pickle.dump(pipeline, f_out)

    return mse
