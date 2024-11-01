# weather_forecast.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import requests, datetime, sys
import matplotlib.pyplot as plt

# Get closest lattitude, longitude coords from ArcGIS given a street address
# Returns {'x': ..., 'y': ...} or None
def get_position(address):
    url = f'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?f=json&singleLine={address}'
    resp = requests.get(url)            # Perform request
    if resp.status_code == 200:         # Test success
        data = resp.json()              # Convert to JSON
        if len(data['candidates']) > 0: # Verify at least one candidate
            return data['candidates'][0]['location']
    return None                         # Request failed

# Convert °C to °F
def C2F(C):
    F = 1.8 * C + 32
    return F

# Get closest weather forecast URL for latitude, longitude
def get_forecast_url(lat, lon):
    url  = f'https://api.weather.gov/points/{lat},{lon}'
    resp = requests.get(url)                    # Get office info
    if resp.status_code != 200: return None     # Return None if failed
    prop = resp.json()['properties']            # Parse and get properties
    return prop['forecastGridData']             # Return forecast URL

# Fetch and compute relative temperature forecast at geolocation
# Returns a list of (delta-hours, temp °F) tuple pairs
def get_temperature_forecast(lat, lon):
    url  = get_forecast_url(lat, lon)           # Get forecast URL
    if not url: return None                     # Return None if failed
    resp = requests.get(url)                    # Get forecast data
    if resp.status_code != 200: return None     # Return None if failed
    
    prop = resp.json()['properties']            # Parse and get properties
    vals = prop['temperature']['values']        # Extract time-temperature pairs
                                                # Current time in UTC timezone
    now  = datetime.datetime.now(datetime.timezone.utc)
    data = []
    for pair in vals:                           # Convert all pairs
        iso = pair['validTime'].split('/')[0]   # Remove any suffix
        d = datetime.datetime.fromisoformat(iso)# Convert to datetime
        h = (d - now).total_seconds()/3600      # Future time in hours
        t = C2F(pair['value'])                  # Convert temp to °F
        data.append((h,t))                      # Accumulate data
    return data

# Fetch temperature forecast data and plot
def plot_temperature_forecast(data):
    hours = [pt[0] for pt in data]              # Extract hours
    temps = [pt[1] for pt in data]              # Extract temperature
    plt.plot(hours, temps)                      # Plot
    plt.title('Temperature Forecast')           # Title and axis labels
    plt.xlabel('Future Time (hrs)')
    plt.ylabel('Temperature (°F)')
    plt.grid()                                  # Add grid
    plt.show()                                  # Show

# Fetch and plot forecast
if __name__ == '__main__':
    # Check command line arguments
    if len(sys.argv) < 3:
        print('Please enter latitude and longitude')
        sys.exit()
    
    # Convert latitude and longitude and get forecast data
    lat, lon = float(sys.argv[1]), float(sys.argv[2])
    data = get_temperature_forecast(lat, lon)
    if not data:
        print("Forecast data fetch failed")
        sys.exit()

    # Plot data
    plot_temperature_forecast(data)
    
    # Print result
    # for point in data:
    #     print(f'{point[1]}°F in {point[0]:.1f} hours')
