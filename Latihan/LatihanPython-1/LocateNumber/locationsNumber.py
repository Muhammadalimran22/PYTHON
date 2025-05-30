import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode
import folium


api_key = "a05d090953074187a092a0f6cb2eca0b"

# fungsi untuk mendapatkan koordinat dari lokasi menggunakan OpenCageGeocode
def get_coordinates(location, api_key):
    geocoder = OpenCageGeocode(api_key)
    query = str(location)
    result = geocoder.geocode(query)
    
    if result and result[0]['geometry']:
        lat = result[0]['geometry']['lat']
        lng = result[0]['geometry']['lng']
        return lat, lng
    else:
        return None, None

# fungsi untuk mendapatkan informasi pengguna
def get_user_info(parsed_number, api_key):
    country_code = parsed_number.country_code
    region_code = geocoder.region_code_for_number(parsed_number)
    country_name = geocoder.country_name_for_number(parsed_number, "en")
    time_zone = timezone.time_zones_for_number(parsed_number)
    
    # menggunakan OpenCage API untuk mendapatkan informasi lebih lanjut
    opencage_geocoder = OpenCageGeocode(api_key)
    query = str(parsed_number.national_number)
    result = opencage_geocoder.geocode(query)
    
    if result and result[0]['components']:
        user_info = result[0]['components']
        return country_name, region_code, time_zone, user_info
    else:
        return country_name, region_code, time_zone, {}

# meminta pengguna memasukkan nomor telepon
number = input("Masukkan nomor telepon: ")

# parsing nomor telepon menggunakan pustaka phonenumbers
parsed_number = phonenumbers.parse(number, "ID")

# mendapatkan informasi lokasi, penyedia layanan, nama pengguna, dan negara
location = geocoder.description_for_number(parsed_number, "en")
service_provider = carrier.name_for_number(parsed_number, "en")
country_name, region_code, time_zone, user_info = get_user_info(parsed_number, api_key)
lat,lng = get_coordinates(location, api_key)

print("Provider Anda:", service_provider)
print("Negara:", country_name)
print("Kode Wilayah:", region_code)
print("Zona Waktu:", time_zone)
print("Kordinasi Anda:",lat,lng)

# menampilkan informasi tambahan dari OpenCage API
if user_info:
    print("Informasi Pengguna:", user_info)

# mendapatkan koordinat dari lokasi menggunakan OpenCageGeocode
api_key = "a05d090953074187a092a0f6cb2eca0b"  # ganti dengan kunci API OpenCageGeocode Anda
lat, lng = get_coordinates(location, api_key)

# membuat peta dengan marker di lokasi yang ditemukan
if lat is not None and lng is not None:
    my_map = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(my_map)

    # menyimpan peta sebagai file HTML
    my_map.save("location.html")
    print("peta telah disimpan sebagai location.html")
else:
    print("tidak dapat menemukan koordinat untuk lokasi tersebut.")
