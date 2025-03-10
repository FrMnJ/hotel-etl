from prefect import flow, task
import joblib
import pandas as pd

@task
def extract():
    return pd.read_csv("./data/X_test.csv"), pd.read_csv("./data/y_test.csv")

@task 
def transform(X_test, y_test):
    model = joblib.load('./data/model.bin')
    result = model.predict(X_test)
    return result

@task 
def load(result):
    pd.DataFrame(result, columns=['is_canceled']).to_csv("./data/predicted.csv", index=False)

@flow
def etl_predicting_pipeline():
    X_test, y_test = extract()
    result = transform(X_test, y_test)
    load(result)

if __name__ == '__main__':
    etl_predicting_pipeline()