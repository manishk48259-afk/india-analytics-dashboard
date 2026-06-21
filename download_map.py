import requests

# India States GeoJSON URL
url = "https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson"

print("📥 Downloading India map data...")
response = requests.get(url)

with open('data/raw/india_states.geojson', 'wb') as f:
    f.write(response.content)

print("✅ Map downloaded successfully!")
print("📁 Saved to: data/raw/india_states.geojson")
