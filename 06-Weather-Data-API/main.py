from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station>/<date>')
def data(station, date):
    station_id = str(station).zfill(6)
    file_name = f'data_small/TG_STAID{station_id}.txt'
    df = pd.read_csv(file_name, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return {
        'station': station,
        'date': date,
        'temperature': temperature
    }

if __name__ == '__main__':
    app.run(debug=True)
