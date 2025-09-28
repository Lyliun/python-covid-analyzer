# app/utils.py

import pandas as pd

def load_and_prepare_data():
    """
    Carrega os dados de COVID-19 do Our World in Data e os prepara para uso.
    """
    # Nova URL para a base de dados do Our World in Data
    url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
    df = pd.read_csv(url)

    # Nota: a nova base de dados já está "derretida" e não precisa do .melt()
    # A coluna de país se chama 'location' e a de data se chama 'date'
    df_prepared = df.rename(columns={'location': 'Country/Region', 'total_cases': 'Confirmed', 'date': 'Date'})
    df_prepared = df_prepared[['Country/Region', 'Date', 'Confirmed']]
    
    # Converte a coluna 'Date' para o tipo datetime
    df_prepared['Date'] = pd.to_datetime(df_prepared['Date'])
    
    return df_prepared