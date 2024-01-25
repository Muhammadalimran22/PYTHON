import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium


key = "a05d090953074187a092a0f6cb2eca0b"
number = input("please giver your number: " )
new_number = phonenumbers.parse(number)
location = geocoder.description_for_number(new_number, "en")
print("Lokasi Anda:", location)

service_name = carrier.name_for_number(new_number,"en")
print("Provider Anda:",service_name)

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print("Kordinasi Anda:",lat,lng)

my_map = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat, lng], popup= location).add_to(my_map)

my_map.save("location.html")