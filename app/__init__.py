from flask import Flask
from .utils import load_and_prepare_data

# Cria a instância da aplicação
app = Flask(__name__)

# Carrega os dados usando a função do arquivo utils
df_prepared = load_and_prepare_data()

# Importa as rotas para que sejam registradas na aplicação
from app import routes