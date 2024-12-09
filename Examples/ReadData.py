import pandas as pd

def read_data() :
    df = pd.read_pickle('../tripdata.pkl')
    df['duration'] = (df['lpep_dropoff_datetime'] - df['lpep_pickup_datetime']).dt.total_seconds()/60
    df.drop(columns=['VendorID', 'store_and_fwd_flag', 'RatecodeID', 'passenger_count',
                  'payment_type', 'fare_amount', 'extra', 'mta_tax', 'tolls_amount', 
                  'improvement_surcharge', 'congestion_surcharge', 'tip_amount', 'ehail_fee', 
                  'total_amount', 'trip_type', 'lpep_pickup_datetime','lpep_dropoff_datetime'], inplace=True)
    
    
    df = df[(df.duration > 1) & (df.duration < 60)]
    return df
