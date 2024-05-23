import requests
import webbrowser
url=requests.get("https://api.wheretheiss.at/v1/satellites/25544")
url.raise_for_status()
iss=url.json()
while True:
    iss_latitude=iss['latitude']
    iss_longitude=iss['longitude']
    maps = f'https://www.google.com/maps/@{iss_latitude},{iss_longitude},14.43z?entry=ttu'
    webbrowser.open(maps)
    print(iss_latitude)
    print(iss_longitude)
    break