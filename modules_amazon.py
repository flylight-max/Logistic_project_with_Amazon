from geopy.geocoders import Nominatim
class Location :
    def __init__(self, Latitude, Longitude) :
        self.Latitude = Latitude
        self.Longitude = Longitude
    def address(self):
        geolocator = Nominatim(user_agent="my_loc_app")
        try:
            location = geolocator.reverse(f"{self.Latitude},{self.Longitude}")
            if location and "address" in location.raw:
                return location.raw["address"]
            else:
                return {}
        except GeocoderTimeOut:
            print(f"Geocoding timed out for {self.Latitude},{self.Longitude}")
            return {}
        except Exception as e:
            print(f"Error for coordinates {self.Latitude},{self.Longitude}: {e}")
            return {}
    def city(self):
        address = self.address()
        city = address.get("city","")
        return city
    def country(self):
        address = self.address()
        country = address.get("country","")
        return country


