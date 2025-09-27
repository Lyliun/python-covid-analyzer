# COVID-19 Data Explorer

Um dashboard interativo para explorar e visualizar dados globais de casos confirmados de COVID-19. Este projeto web é construído com **Python** e utiliza as bibliotecas **Flask** para o servidor, **Pandas** para o processamento de dados e **Plotly** para a criação de gráficos interativos.

---

### 💻 Tecnologias Utilizadas

* **Python 3.x:** A linguagem de programação principal.
* **Flask:** Um microframework para criar a aplicação web.
* **Pandas:** Usado para manipulação e análise dos dados.
* **Plotly Express:** Biblioteca para a criação de visualizações de dados dinâmicas.

---

### 🚀 Instalação e Execução

Siga os passos abaixo para configurar e rodar o projeto localmente.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```
    *Lembre-se de substituir `seu-usuario/seu-repositorio` pelos seus dados.*

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install Flask pandas plotly
    ```

4.  **Execute a aplicação:**
    ```bash
    python data_loader.py
    ```

5.  **Acesse o dashboard:**
    Abra seu navegador e acesse `http://127.0.0.1:5000`.

---

### 📚 Uso

O dashboard permite selecionar um país em um menu suspenso para visualizar o número de casos de COVID-19 confirmados ao longo do tempo. Você pode alternar entre gráficos de linha e de barra para diferentes visualizações.

---

### 📄 Fonte de Dados

Os dados utilizados neste projeto são extraídos do repositório CSSE (Center for Systems Science and Engineering) da **Johns Hopkins University**.

* **URL da fonte:** `https://github.com/CSSEGISandData/COVID-19`

---

### 🤝 Contribuição

Contribuições são bem-vindas! Se tiver alguma ideia ou encontrar um bug, por favor, abra uma _issue_ ou envie um _pull request_.
