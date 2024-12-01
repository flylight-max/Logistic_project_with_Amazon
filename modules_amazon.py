from geopy.geocoders import Nominatim
class Location :
    def __init__(self, Latitude, Longitude) :
        self.Latitude = Latitude
        self.Longitude = Longitude
    def address(self):
        geolocator = Nominatim(user_agent="my_loc_app")
        location = geolocator.reverse(f"{self.Latitude},{self.Longitude}")
        ad = location.raw["address"]
        return ad
    def city(self):
        address = self.address()
        city = address.get("city","")
        return city
    def country(self):
        address = self.address()
        country = address.get("country","")
        return country
