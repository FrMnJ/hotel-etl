from prefect import flow, task
import pandas as pd

@task
def extract(): 
   return pd.read_csv("./data/init_hotel_bookings.csv")

@task
def transform(df):
    df.drop(columns=['company'], inplace=True)
    df['agent'] = df['agent'].fillna(-1)
    df['children'] = df['children'].fillna(df['children'].mean())
    df = df.dropna(how='any',axis=0) 
    df['hotel'] = df['hotel'].astype('category').cat.codes
    df['customer_type'] = df['customer_type'].astype('category').cat.codes
    df['market_segment'] = df['market_segment'].astype('category').cat.codes
    # TODO: Add more transformations from categorical to numerical if needed
    df['arrival_date_month'] = df['arrival_date_month'].astype('category').cat.codes
    df['meal'] = df['meal'].astype('category').cat.codes
    df['country'] = df['country'].astype('category').cat.codes
    df['distribution_channel'] = df['distribution_channel'].astype('category').cat.codes
    df['reserved_room_type'] = df['reserved_room_type'].astype('category').cat.codes
    df['assigned_room_type'] = df['assigned_room_type'].astype('category').cat.codes
    df['deposit_type'] = df['deposit_type'].astype('category').cat.codes
    df.drop(columns=['reservation_status', 'reservation_status_date',
                      'name', 'email', 'phone-number', 'credit_card'],
                        inplace=True)
    return df

@task 
def load(df):
    df.to_csv("./data/cleaned_hotel_bookings.csv", index=False)

@flow
def etl_cleaning_pipeling():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == '__main__':
    etl_cleaning_pipeling()