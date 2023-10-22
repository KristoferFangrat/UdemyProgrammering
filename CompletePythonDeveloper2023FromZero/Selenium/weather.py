from selenium import webdriver
import requests
import pandas as pd

# Set up Selenium WebDriver to scrape weather data
driver = webdriver.Firefox()
driver.get('https://www.openweathermap.org')
latitude = 59.30996
longitude = 18.0215

# Fetch weather data from OpenWeatherMap API
api_key = '6c30307c52451d4451b9cad034fb8cb0'
weather_api_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&exclude=current,minutely,daily,alerts&appid={api_key}&units=metric"
response = requests.get(weather_api_url)
weather_data = response.json()

# extraherar temperatur och nederbörd data
temperature = weather_data['main']['temp']
precipitation = weather_data['rain']['1h'] if rain in weather_data else 0.0
# skapar en Pandas "dataframe"
weather_df = pd.DataFrame({'Latitude': [latitude], 'Longitude': [longitude], 'Temperature (Celsius)': [temperature], 'Precipitation': [precipitation]})
# sparar datan i en excel-fil
weather_df.to_excel('weather_data.xlsx', index=False)

# Stänger ner selenium Webdriver
driver.quit()