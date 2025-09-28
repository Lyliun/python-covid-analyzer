from flask import render_template, request, jsonify
from app import app, df_prepared # Importa a instância do Flask e os dados

import plotly.express as px

@app.route('/')
def index():
    countries = sorted(df_prepared['Country/Region'].unique())
    return render_template('index.html', countries=countries)

# app/routes.py
@app.route('/data')
def get_data():
    country = request.args.get('country')
    chart_type = request.args.get('chart_type')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    if not country or not chart_type:
        return jsonify({'error': 'Missing country or chart type parameter'}), 400
    
    country_df = df_prepared[df_prepared['Country/Region'] == country]
    if country_df.empty:
        return jsonify({'error': 'Country not found'}), 404

    # Lógica do filtro de data
    if start_date:
        country_df = country_df[country_df['Date'] >= start_date]
    if end_date:
        country_df = country_df[country_df['Date'] <= end_date]

    # ... o restante da sua função continua aqui ...
    country_df = country_df.groupby('Date')['Confirmed'].sum().reset_index()

    import plotly.express as px
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