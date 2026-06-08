from flask import Flask, render_template, request
import requests

app = Flask(__name__)  

API_KEY = "API key here"  

@app.route('/') 
def home():
    return render_template('index.html')  

@app.route('/weather')
def weather():
    city = request.args.get('city')
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    print(data) 
    
    if data.get('cod') != 200:
        return f"Error: {data.get('message', 'something went wrong')}"
    
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    
    return render_template('result.html',
                           city=city,
                           temperature=temperature,
                           humidity=humidity,
                           description=description)

if __name__ == '__main__':
    app.run(debug=True)  