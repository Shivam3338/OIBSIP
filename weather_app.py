import requests
import json

def get_weather(api_key, location):
    """
    Fetches current weather data for a given location (city or ZIP code)
     using the OpenWeatherMap API.

    Args:
        api_key (str): Your OpenWeatherMap API key.
        location (str): The name of the city or ZIP code to get weather for.

    Returns:
        dict or None: A dictionary containing weather data if successful,
                      otherwise None.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Check if the location is likely a ZIP code (e.g., all digits)
    if location.isdigit():
        # For ZIP codes, OpenWeatherMap often requires country code,
        # but for simplicity, we'll try without first.
        # A more robust solution would ask for country code or use a geocoding API.
        complete_url = f"{base_url}appid={api_key}&zip={location}&units=metric"
    else:
        complete_url = f"{base_url}appid={api_key}&q={location}&units=metric" # units=metric for Celsius

    try:
        response = requests.get(complete_url)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        # Check if the request was successful (cod 200 means OK)
        if data["cod"] == 200:
            main_data = data["main"]
            weather_data = data["weather"][0]
            city_name_returned = data["name"] # Get the official city name returned by API

            temperature = main_data["temp"]
            humidity = main_data["humidity"]
            weather_description = weather_data["description"]

            return {
                "city": city_name_returned,
                "temperature": temperature,
                "humidity": humidity,
                "description": weather_description
            }
        else:
            # OpenWeatherMap returns a message for errors (e.g., city not found)
            error_message = data.get("message", "Unknown error")
            print(f"Error: Could not find weather data for '{location}'. API message: {error_message.capitalize()}")
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} (Status Code: {response.status_code})")
        print("Please double-check your API key and the location name/ZIP code.")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
        print("Please check your internet connection.")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
        print("The request timed out. Please try again.")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected request error occurred: {req_err}")
        return None
    except json.JSONDecodeError:
        print("Error: Could not decode JSON response from the API. The API might have returned invalid data.")
        return None
    except KeyError as ke:
        print(f"Error: Missing expected data in API response ({ke}). The API response structure might have changed or data is incomplete.")
        return None


def main():
    """
    Main function to run the weather application.
    """
    # IMPORTANT: Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key.
    # You can get one for free from https://openweathermap.org/api
    api_key = "YOUR_API_KEY" # <--- REPLACE THIS WITH YOUR API KEY

    if api_key == "YOUR_API_KEY":
        print("WARNING: Please replace 'YOUR_API_KEY' in the script with your actual OpenWeatherMap API key.")
        print("You can get a free API key from: https://openweathermap.org/api")
        print("Exiting...")
        return

    location = input("Enter city name or ZIP code (e.g., London, 90210): ")

    weather_info = get_weather(api_key, location)

    if weather_info:
        print(f"\n--- Current Weather in {weather_info['city']} ---")
        print(f"  Temperature: {weather_info['temperature']:.1f}°C")
        print(f"  Humidity: {weather_info['humidity']}%")
        print(f"  Conditions: {weather_info['description'].capitalize()}")
        print("-----------------------------------")
    else:
        print("Failed to retrieve weather information. Please try again with a valid location.")

if __name__ == "__main__":
    main()