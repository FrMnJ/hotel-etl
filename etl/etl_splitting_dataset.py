from prefect import flow, task
import pandas as pd
from sklearn.model_selection import train_test_split

@task 
def extract(): 
    return pd.read_csv("./data/cleaned_hotel_bookings.csv")

@task
def transform(df):
    features = [column for column in df.columns if column != 'is_canceled']
    X = df.loc[:, features]
    y = df.loc[:, ['is_canceled']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=37)
    return X_train, X_test, y_train, y_test

@task 
def load(X_train, X_test, y_train, y_test):
    X_train.to_csv("./data/X_train.csv", index=False)
    X_test.to_csv("./data/X_test.csv", index=False)
    y_train.to_csv("./data/y_train.csv", index=False)
    y_test.to_csv("./data/y_test.csv", index=False)

@flow
def etl_splitting_dataset_pipeline():
    df = extract()
    X_train, X_test, y_train, y_test = transform(df)
    load(X_train, X_test, y_train, y_test)

if __name__ == '__main__':
    etl_splitting_dataset_pipeline()