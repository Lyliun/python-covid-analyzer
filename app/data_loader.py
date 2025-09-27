from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Carregar os dados do CSSE COVID-19 Data Repository
def load_data():
    # URL do arquivo CSV mais recente do CSSE
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    df = pd.read_csv(url)
    return df

df = load_data()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    country = request.args.get('country')
    chart_type = request.args.get('chart_type')
    
    # Filtrar os dados pelo país
    country_df = df[df['Country/Region'] == country]
    
    if country_df.empty:
        return jsonify({'error': 'Country not found'}), 404

    # Agrupar os dados por data
    country_df = country_df.groupby('Date').sum().reset_index()
    
    if chart_type == 'line':
        fig = px.line(country_df, x='Date', y=country_df.columns[1:], title=f'COVID-19 Cases in {country}')
    elif chart_type == 'bar':
        fig = px.bar(country_df, x='Date', y=country_df.columns[1:], title=f'COVID-19 Cases in {country}')
    else:
        return jsonify({'error': 'Invalid chart type'}), 400

    graph_json = fig.to_json()
    return jsonify(graph_json)

if __name__ == '__main__':
    app.run(debug=True)
