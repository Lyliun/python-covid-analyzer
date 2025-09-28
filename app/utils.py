import pandas as pd

def load_and_prepare_data():
    """
    Carrega os dados de COVID-19 do CSSE e os prepara para uso.
    """
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    df = pd.read_csv(url)
    
    # Derrete o DataFrame para converter as datas de colunas para linhas
    df_melted = df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
                        var_name='Date', 
                        value_name='Confirmed')
    
    # Converte a coluna 'Date' para o tipo datetime
    df_melted['Date'] = pd.to_datetime(df_melted['Date'], format='%m/%d/%y')
    
    return df_melted