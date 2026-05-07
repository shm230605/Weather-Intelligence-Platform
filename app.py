import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
from datetime import datetime
import pandas as pd

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Weather Intelligence Pro", layout="wide")

st.title("🌍 Weather Intelligence Pro Dashboard")
st.caption("Live Weather • Global Map • Alerts • Forecast Trends")

# =========================
# CLEAN UI STYLE
# =========================
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}
h1 {
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 30 COUNTRIES
# =========================
CITY_DB = {
    "Argentina": ["Buenos Aires", "Córdoba", "Rosario"],
    "Australia": ["Sydney", "Melbourne", "Brisbane"],
    "Bangladesh": ["Dhaka", "Chittagong", "Sylhet"],
    "Brazil": ["São Paulo", "Rio de Janeiro", "Brasília"],
    "Canada": ["Toronto", "Vancouver", "Montreal"],
    "China": ["Beijing", "Shanghai", "Shenzhen"],
    "Egypt": ["Cairo", "Alexandria", "Giza"],
    "France": ["Paris", "Lyon", "Marseille"],
    "Germany": ["Berlin", "Munich", "Hamburg"],
    "India": ["Kolkata", "Delhi", "Mumbai", "Chennai", "Bangalore"],
    "Indonesia": ["Jakarta", "Bali", "Surabaya"],
    "Italy": ["Rome", "Milan", "Naples"],
    "Japan": ["Tokyo", "Osaka", "Kyoto"],
    "Malaysia": ["Kuala Lumpur", "Penang", "Johor Bahru"],
    "Mexico": ["Mexico City", "Guadalajara", "Monterrey"],
    "Netherlands": ["Amsterdam", "Rotterdam", "Utrecht"],
    "Nigeria": ["Lagos", "Abuja", "Kano"],
    "Pakistan": ["Karachi", "Lahore", "Islamabad"],
    "Philippines": ["Manila", "Cebu", "Davao"],
    "Russia": ["Moscow", "Saint Petersburg", "Novosibirsk"],
    "Saudi Arabia": ["Riyadh", "Jeddah", "Mecca"],
    "South Africa": ["Cape Town", "Johannesburg", "Durban"],
    "South Korea": ["Seoul", "Busan", "Incheon"],
    "Spain": ["Madrid", "Barcelona", "Valencia"],
    "Thailand": ["Bangkok", "Phuket", "Chiang Mai"],
    "Turkey": ["Istanbul", "Ankara", "Izmir"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah"],
    "United Kingdom": ["London", "Manchester", "Birmingham"],
    "United States": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Vietnam": ["Hanoi", "Ho Chi Minh City", "Da Nang"]
}

# =========================
# CITY COORDINATES
# =========================
CITY_COORDS = {
    "Kolkata": (22.5726, 88.3639),
    "Delhi": (28.7041, 77.1025),
    "Mumbai": (19.0760, 72.8777),
    "Chennai": (13.0827, 80.2707),
    "Bangalore": (12.9716, 77.5946),
    "New York": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "Chicago": (41.8781, -87.6298),
    "Houston": (29.7604, -95.3699),
    "London": (51.5072, -0.1276),
    "Paris": (48.8566, 2.3522),
    "Berlin": (52.5200, 13.4050),
    "Tokyo": (35.6762, 139.6503),
    "Seoul": (37.5665, 126.9780),
    "Dubai": (25.2048, 55.2708),
}

# =========================
# WEATHER API
# =========================
def get_weather(lat, lon):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&current=temperature_2m,wind_speed_10m,relative_humidity_2m"
        "&hourly=temperature_2m,precipitation_probability"
    )
    return requests.get(url).json()

# =========================
# ALERT ENGINE
# =========================
def get_alerts(temp, wind):
    alerts = []
    if temp >= 40:
        alerts.append("🔥 Heat Wave Alert")
    if temp <= 5:
        alerts.append("❄️ Cold Wave Alert")
    if wind > 50:
        alerts.append("🌪️ Storm Alert")
    return alerts

# =========================
# SIDEBAR
# =========================
country = st.sidebar.selectbox("🌍 Select Country", sorted(CITY_DB.keys()))
city = st.sidebar.selectbox("🏙️ Select City", CITY_DB[country])
unit = st.sidebar.radio("🌡️ Temperature Unit", ["Celsius", "Fahrenheit"])

st.sidebar.success("🕒 " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# =========================
# LOCATION
# =========================
lat, lon = CITY_COORDS.get(city, (20, 0))

# =========================
# WEATHER DATA
# =========================
data = get_weather(lat, lon)
current = data["current"]
hourly = data["hourly"]

temp_c = current["temperature_2m"]
wind = current["wind_speed_10m"]
humidity = current["relative_humidity_2m"]

alerts = get_alerts(temp_c, wind)

# =========================
# MAP
# =========================
st.subheader("🗺️ Global Map")

m = folium.Map(location=[20, 0], zoom_start=2)

folium.Marker(
    [lat, lon],
    popup=f"{city}, {country}",
    tooltip="Selected Location"
).add_to(m)

st_folium(m, width=1100, height=450)

# =========================
# WEATHER METRICS
# =========================
st.subheader("🌦️ Current Weather")

if unit == "Fahrenheit":
    temp = (temp_c * 9/5) + 32
    label = "°F"
else:
    temp = temp_c
    label = "°C"

col1, col2, col3 = st.columns(3)

col1.metric("🌡️ Temperature", f"{round(temp,1)} {label}")
col2.metric("💨 Wind Speed", f"{wind} km/h")
col3.metric("💧 Humidity", f"{humidity}%")

# =========================
# ALERTS
# =========================
st.subheader("⚠️ Alerts")

if alerts:
    for a in alerts:
        st.error(a)
else:
    st.success("No Weather Alerts")

# =========================
# CLEAN INSIGHT PANEL (NO RAW JSON)
# =========================
st.subheader("📊 Weather Insights")

st.markdown(f"""
- 🌍 **Country:** {country}  
- 🏙️ **City:** {city}  
- 📍 **Coordinates:** {lat}, {lon}  

- 🌡️ **Temperature:** {round(temp,1)} {label}  
- 💨 **Wind Speed:** {wind} km/h  
- 💧 **Humidity:** {humidity}%  

- 🕒 **System Time:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
""")

# =========================
# FORECAST TABLE
# =========================
st.subheader("📈 24-Hour Forecast")

df = pd.DataFrame({
    "Time": hourly["time"][:24],
    "Temperature": hourly["temperature_2m"][:24],
    "Rain Probability": hourly["precipitation_probability"][:24]
})

st.dataframe(df, use_container_width=True)

# =========================
# CURVE GRAPH
# =========================
st.subheader("📉 Temperature Trend")

st.line_chart(df.set_index("Time")["Temperature"])