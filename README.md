# 🌍 Weather Intelligence Pro Dashboard

A professional Python + Streamlit weather application that provides real-time weather data, global map visualization, smart alerts, and forecast analytics for multiple countries and cities.

---

## 🚀 Project Overview

The Weather Intelligence Pro Dashboard is an interactive weather monitoring system that allows users to:
```
- 🌍 Select from 30+ countries and multiple cities
- 🗺️ View interactive world map with location marker
- 🌡️ Get real-time weather (temperature, wind, humidity)
- ⚠️ Receive smart alerts (Heatwave, Cold Wave, Storm)
- 📊 View 24-hour forecast trends
- 📈 Visualize temperature graph
- 🕒 Live system time display
```
This project is built using Python, Streamlit, and Open-Meteo API.

---

## 🎯 Problem Statement

Weather conditions affect travel, agriculture, logistics, and outdoor planning.  
Most basic weather apps lack:

- Data visualization
- Smart alert system
- Interactive UI
- Multi-country support

This project solves these issues by building a **professional weather intelligence dashboard**.

---

## ✨ Features

### 🌍 Global Support
- 30+ countries included
- Multiple cities per country
- Dynamic dropdown selection

### 🗺️ Interactive Map
- World map view
- Selected city marked with pointer

### 🌡️ Weather Data
- Temperature (°C / °F toggle)
- Wind speed (km/h)
- Humidity (%)

### ⚠️ Smart Alerts
```
- 🔥 Heatwave Alert (≥ 40°C)
- ❄️ Cold Wave Alert (≤ 5°C)
- 🌪️ Storm Alert (High wind speed)
```
### 📊 Analytics
- 24-hour forecast table
- Temperature trend graph

### 🕒 Live Time
- Real-time system clock

---

## 🛠️ Tech Stack
```
- Python 
- Streamlit (UI Framework)
- Folium (Maps)
- Open-Meteo API (Weather Data)
- Pandas (Data handling)
- Requests (API calls)
```
---

## 📁 Project Structure
```
Weather-Intelligence-Platform/
│
├── app.py                          # Main Streamlit dashboard (ENTRY POINT)
├── requirements.txt               # All dependencies
├── README.md                      # Full documentation
├── .gitignore                     # Ignore venv, cache, etc.
│
├── assets/                        # UI assets (images, icons, logos)
│   ├── logo.png
│   ├── weather_icons/
│   └── screenshots/
│
├── components/                    # UI modules (frontend logic)
│   ├── world_map.py              # Map rendering (Folium)
│   ├── weather_cards.py          # Weather UI cards
│   ├── alerts_panel.py           # Alert UI
│   ├── forecast_chart.py         # Graphs & curves
│   ├── city_selector.py         # Country → City logic
│   └── header.py                # UI header design
│
├── services/                     # Backend logic (API + processing)
│   ├── weather_service.py       # Open-Meteo API calls
│   ├── geocode_service.py       # City → Lat/Lon conversion
│   ├── alert_service.py         # Heat/Storm/Cold logic
│   └── time_service.py          # Time & timezone handling
│
├── models/                       # Data structures
│   ├── weather_model.py
│   └── alert_model.py
│
├── data/                         # Cached / stored data
│   ├── cities.json
│   ├── countries.json
│   └── sample_weather.json
│
├── outputs/                      # Generated outputs
│   ├── reports/
│   ├── charts/
│   └── pdf_exports/
│
├── utils/                        # Helper functions
│   ├── helpers.py
│   ├── constants.py
│   └── formatters.py
│
├── styles/                       # Custom UI styling
│   └── style.css
│
└── venv/                         # Virtual environment 
```

---

## ⚠️ Alert Logic
```
|    Condition   |      Alert    |
|----------------|---------------|
|     ≥ 40°C     | 🔥 Heatwave  |
|     ≤ 5°C      | ❄️ Cold Wave |
| Wind > 50 km/h |   🌪️ Storm   |
```
---

## 📊 Sample Output

- City: Kolkata  
- Temperature: 23.4°C  
- Wind: 4.3 km/h  
- Humidity: 93%  
- Alerts: Heatwave (if triggered)

---

## 📈 Learning Outcomes
```
- API integration
- Data visualization
- UI development using Streamlit
- Weather forecasting logic
- Alert system design
- Real-world project structuring
```
---

## 🚀 Future Improvements
```
- 🌫️ AQI monitoring
- 🌪️ Weather radar animation
- 🔔 Push notifications
- 📱 Mobile responsive UI
- 📄 PDF report export
- 🌐 Cloud deployment
```
---

## 👨‍💻 Author

Shresthaa Maiti
