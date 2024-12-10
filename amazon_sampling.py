import pandas as pd
import numpy as np
import pickle
with open("amazon_del.pkl","rb") as f:
    amazon_del = pickle.load(f)
print(amazon_del.info())
print(amazon_del["Distance_Store_Drop_km"].describe())
with open("Store_LatLong_null.pkl","rb") as f:
    null_Store_coord = pickle.load(f)

amazon_del = amazon_del[~(amazon_del["abs_Store_Latitude"].\
                          isin(null_Store_coord["Store_Latitude"]))]
#New sampling
amazon_del = amazon_del.sample(frac=1, replace=False, random_state=2013)
amazon_400Samples = amazon_del.sample(n=400, replace=False, random_state=1984)
from geopy.geocoders import Nominatim
from modules_amazon import Location
import time
cities = []
for lat,long in zip(amazon_400Samples["abs_Store_Latitude"],amazon_400Samples["abs_Store_Longitude"]):
    loc = Location(lat,long)
    try:
        cities.append(loc.city())
    except Exception as e:
        print(f"Error for coordinates lat {lat}, long {long}: {e}")
        cities.append(None)
    time.sleep(1)
amazon_400Samples["City"] = cities
with open("amazon_new400_samples.pkl","wb") as f:
    pickle.dump(amazon_400Samples,f)


