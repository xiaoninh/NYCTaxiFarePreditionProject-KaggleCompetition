import pandas as pd
import geopy.distance as gps
import numpy as np
file = "2014_nyc_taxi_trips.csv"
RUSH_HOUR = [7, 8, 9, 16, 17, 18, 19]

class dataLoader():

    def __init__(self, f):
        self.data = pd.read_csv(f, nrows=500, parse_dates=['pickup_datetime', 'key'])

    def calc_dist(self):
        pickup_loc = list((self.data.loc[i].pickup_longitude, self.data.loc[i].pickup_latitude) for i in range(0, len(self.data)))
        dropoff_loc = list((self.data.loc[i].dropoff_longitude, self.data.loc[i].dropoff_latitude) for i in range(0, len(self.data)))
        distance = list(gps.vincenty(cor1, cor2).miles for cor1, cor2 in zip(pickup_loc, dropoff_loc))
        self.data['distance'] = distance

    def get_weekday(self):
        self.data['weekday'] = self.data.pickup_datetime.dt.dayofweek

    def get_rush_hour(self):
        self.data['rush_hour'] = self.data.pickup_datetime.dt.hour.apply(lambda x: 1 if x in RUSH_HOUR else 0)

    def get_weekend(self):
        self.data['weekend'] = self.data.pickup_datetime.dt.dayofweek.apply(lambda x: 1 if x in [5,6] else 0)

    def get_day_night(self):
        self.data['day_night'] = self.data.pickup_datetime.dt.hour.apply(lambda x: 1 if x in range(6,19) else 0)

    def save(self):
        self.data.to_csv("2014_nyc_taxi_trips_processed_data.csv")
        return self.data

def driver(buffer):
    buffer.calc_dist()
    buffer.get_weekday()
    buffer.get_rush_hour()
    buffer.get_weekend()
    buffer.get_day_night()
    df = buffer.save()
    return df

if __name__ == '__main__':
    dt = dataLoader(file)
    result = driver(dt)
