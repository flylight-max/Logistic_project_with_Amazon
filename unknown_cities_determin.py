import pandas as pd
import pickle
import numpy as np
from geopy.geocoders import Nominatim
from modules_amazon import Location
import time

with open("amazon_new400_samples.pkl","rb") as f:
    amazon_del400 = pickle.load(f)

unknown_cities = amazon_del400[amazon_del400["City"] == ""]

drop_cities = []
for lat,long in zip(unknown_cities["Drop_Latitude"],unknown_cities["Drop_Longitude"]):
    loc = Location(lat,long)
    drop_cities.append(loc.city())
    time.sleep(1)

unknown_cities["Drop_city"] = drop_cities

with open("Drop_cities_UStore_cities.pkl", "wb") as f:
    pickle.dump(unknown_cities,f)
