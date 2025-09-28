from flask import render_template, request, jsonify
from app import app, df_prepared # Importa a instância do Flask e os dados

import plotly.express as px

@app.route('/')
def index():
    countries = sorted(df_prepared['Country/Region'].unique())
    return render_template('index.html', countries=countries)

@app.route('/data')
def get_data():
    country = request.args.get('country')
    chart_type = request.args.get('chart_type')
    
    if not country or not chart_type:
        return jsonify({'error': 'Missing country or chart type parameter'}), 400
    
    country_df = df_prepared[df_prepared['Country/Region'] == country]
    if country_df.empty:
        return jsonify({'error': 'Country not found'}), 404

    country_df = country_df.groupby('Date')['Confirmed'].sum().reset_index()
    
    if chart_type == 'line':
        fig = px.line(country_df, 
                      x='Date', 
                      y='Confirmed', 
                      title=f'Casos de COVID-19 Confirmados em {country}')
    elif chart_type == 'bar':
        fig = px.bar(country_df, 
                     x='Date', 
                     y='Confirmed', 
                     title=f'Casos de COVID-19 Confirmados em {country}')
    else:
        return jsonify({'error': 'Invalid chart type'}), 400

    graph_json = fig.to_json()
    return jsonify(graph_json)