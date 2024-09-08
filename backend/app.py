from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from weather_service import get_weather_data 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    temperatura = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

with app.app_context():
    db.create_all()

@app.route('/weather', methods=['GET'])
def get_weather():
    city = requests.args.get('city')
    if not city:
        return jsonify({'error': 'Cidade não encontrada'}), 400
    
    weather_data = get_weather_data(city)
    if weather_data.get("error"):
        return jsonify(weather_data), 400
    
    new_location = Location(city=city, temperature=weather_data['temp'])
    db.session.add(new_location)
    db.session.commit()

    return jsonify(weather_data)

@app.route('/history', methods = ['GET'])
def get_history():
    history = Location.query.all()
    results = [
        {
            "city": loc.city,
            "temperature": loc.temperature,
            "timestamp": loc.timestamp
        } for loc in history
    ]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)