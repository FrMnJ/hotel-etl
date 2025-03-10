from prefect import flow, task
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

@task
def extract():
    return pd.read_csv("./data/X_train.csv"), pd.read_csv("./data/y_train.csv")

@task 
def transform(X_train, y_train):
    model = RandomForestClassifier(class_weight='balanced')
    model.fit(X_train, y_train)    
    return model

@task
def load(model):
    filename = './data/model.bin'
    joblib.dump(model, filename)

@flow
def etl_training_pipeline():
    X_train, y_train = extract()
    model = transform(X_train, y_train)
    load(model)

if __name__ == '__main__':
    etl_training_pipeline()