import pandas as pd
SIZE = 10 ** 5
file = "train.csv"

def process(data):
    data['pickup_datetime'] = pd.to_datetime(data['pickup_datetime'])
    data_f = data[data['pickup_datetime'].dt.year == 2014]
    return data_f

def main():
    i = 1
    data = pd.DataFrame()
    for chunck in pd.read_csv(file, chunksize=SIZE):
        print("Iteration: ", i)
        if len(data) == 0:
            data = process(chunck)
        elif len(data) > 0:
            data = data.append(process(chunck))
        i += 1
    data = data.reset_index(drop=True)
    data.to_csv("2014_nyc_taxi_trips.csv")
    return data

if __name__ == "__main__":
    test = main()
