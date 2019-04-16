import pandas as pd
from datetime import datetime
import csv
import rtree
import geopandas as gpd
import fiona
import pyproj
import shapely.geometry as geom

SIZE = 10 ** 4
file = '/Users/hemingyi/Documents/machine learning/MLC_Project/dataset/2014_nyc_taxi_trips_with_features.csv'
index = rtree.Rtree()
zones = gpd.read_file('/Users/hemingyi/Documents/machine learning/MLC_Project/dataset/neighborhoods.geojson').to_crs(fiona.crs.from_epsg(2263))
proj = pyproj.Proj(init="epsg:2263", preserve_units=True)

for idx,geometry in enumerate(zones.geometry):
    index.insert(idx, geometry.bounds)

def Neighbor(data):
	PO = geom.Point(proj(data['pickup_longitude'], data['pickup_latitude']))
	PD = geom.Point(proj(data['dropoff_longitude'], data['dropoff_latitude']))
	PickMatch = index.intersection((PO.x, PO.y, PO.x, PO.y))
	DropMatch = index.intersection((PD.x, PD.y, PD.x, PD.y))
	for idxO in PickMatch:
		for idxD in DropMatch:
			if zones.geometry[idxO].contains(PO) and zones.geometry[idxD].contains(PD):
				return(zones.neighborhood[idxO],zones.neighborhood[idxD],)
			else:return(None,None)

def main():
	i = 1
	data = pd.DataFrame()
	for chunck in pd.read_csv(file, chunksize=SIZE):
		print("Iteration: ", i)
		chunck['neighborhood'] = chunck.apply(Neighbor,axis=1)
		data = data.append(chunck)
		i += 1
	data = data.reset_index(drop=True)
	data.to_csv("2014_nyc_taxi_trips_neighbor.csv")
	return data

if __name__ == "__main__":
	main()

