import requests

def get_weather_data():
    API_Key = 'your_api_key'
    url = f"https://api.weatherstack.com/current?access_key={API_Key}"

    while True:
        answer = input('Would you like to check the weather in a specific city?(y/n) ')
        if answer == 'y':   
            city_name = input("Enter the city name: ")
            querystring = {"query": city_name}
            response = requests.get(url, params=querystring)
                    
            if response.status_code == 200:
                data = response.json()
                print('City:', city_name)
                print('Weather:', data['current']['weather_descriptions'][0])
                print('Current temperature:', data['current']['temperature'])
                print('Feels like:', data['current']['feelslike'])
                print('Wind speed:', data['current']['wind_speed'])
                print('Humidity:', data['current']['humidity'])
                print('UV index:', data['current']['uv_index'])
                continue
        else:
            print('Thank you, goodbye!')
            break

if __name__ == '__main__':
    get_weather_data()