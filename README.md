# 🌦️ Weather Checker (Python + API)
### About the Project

This is a simple command-line Weather App built in Python.
It uses the WeatherStack API to fetch real-time weather information for any city in the world.
The goal of this project is to practice API integration, JSON parsing, and user interaction through input prompts.

### 🔍 Features

- Get current weather data for any city
- Displays temperature, humidity, and wind speed
- Includes weather description and UV index
- User-friendly command-line interaction

### 💭 What I Learned

- How to connect to and use a public API with the requests library
- How to handle user input in loops
- How to extract and display data from a JSON response
- How to write cleaner and more readable Python code

### ⚙️ How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/weather-checker.git
cd weather-checker
```

2. **Install dependencies:**
```bash
pip install requests
```

3. **Get a free API key:**
- Go to WeatherStack API
- Sign up and copy your API key

4. **Update your code:**
Replace 'your_api_key' in the script with your actual key.

5. **Run the program:**
```bash
python main.py
```
### Example
```yaml
Would you like to check the weather in a specific city?(y/n) y
Enter the city name: Paris
City: Paris
Weather: Partly cloudy
Current temperature: 22
Feels like: 21
Wind speed: 10
Humidity: 65
UV index: 4
```

### 💻 Tech Stack

- Python 3
- Requests library
- WeatherStack API

### 📈 Next Steps

- Add error handling for invalid city names
- Store recent weather searches in a file
- Build a Streamlit dashboard version
