import googlemaps
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()  

api_key = os.getenv("Google_API_KEY")
print("Your API key is:", api_key)


gmaps = googlemaps.Client(
    key=os.getenv("Google_API_KEY")
)  

# Define origin and destination
origin = "192 Evelyn Rd, Waban, MA"
destination = "Belmont Hill School, Belmont, MA"

# Get directions (driving mode, current time)
now = datetime.now()
directions_result = gmaps.directions(
    origin, destination, mode="driving", departure_time=now
)

# Extract and print drive duration
if directions_result:
    duration = directions_result[0]["legs"][0]["duration"]["text"]
    print(f"Estimated drive time from {origin} to {destination}: {duration}")
else:
    print("Could not get directions.")
