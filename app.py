from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    df = pd.read_csv('cars.csv')
    budget = float(request.form['budget'])
    location = request.form['location'].strip().lower()

    filtered = df[df['Price'] <= budget]
    if location:
        filtered = filtered[filtered['Location'].str.lower() == location]

    return render_template('results.html', cars=filtered.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
