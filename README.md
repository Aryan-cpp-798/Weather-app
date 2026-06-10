# 🌤️ Weather App

A real-time weather web app built with **Python**, **Flask**, and the **OpenWeatherMap API**. Search any city and instantly get current temperature, weather conditions, humidity, and wind speed.


---

## ✨ Features

- 🔍 Search weather by city name
- 🌡️ Displays temperature, humidity, wind speed, and weather condition
- ⚡ Real-time data from OpenWeatherMap API
- 🌐 Clean web interface with HTML/CSS frontend

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Frontend | HTML |
| API | OpenWeatherMap REST API |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- OpenWeatherMap API key — free at [openweathermap.org](https://openweathermap.org/api)

### Installation

```bash
# Clone the repo
git clone https://github.com/Aryan-cpp-798/Weather-app.git
cd Weather-app

# Install dependencies
pip install flask requests

# Add your API key
# Open app.py and set your API key, or create a .env file:
# API_KEY=your_api_key_here

# Run the app
python app.py
```

Then open `http://localhost:5000` in your browser.

---

## 📁 Project Structure

```
Weather-app/
├── app.py          # Flask backend — API calls and routing
├── templates/
│   ├── index.html  # Search page
│   └── result.html # Weather results page
├── .gitignore
└── README.md
```

---

## 📄 License

MIT License
