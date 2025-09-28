# COVID-19 Data Explorer

An interactive dashboard to explore and visualize global confirmed COVID-19 case data. This web project is built with **Python** and uses the **Flask** framework for the server, **Pandas** for data processing, and **Plotly** for creating interactive charts.

---

### 💻 Technologies Used

* **Python 3.x:** The main programming language.
* **Flask:** A micro-framework for building the web application.
* **Pandas:** Used for data manipulation and analysis.
* **Plotly Express:** A library for creating dynamic data visualizations.

---

### 🚀 Installation and Running

Follow the steps below to set up and run the project locally.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository.git](https://github.com/your-username/your-repository.git)
    cd your-repository
    ```
    *Remember to replace `your-username/your-repository` with your own details.*

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install Flask pandas plotly
    ```

4.  **Run the application:**
    ```bash
    python data_loader.py
    ```

5.  **Access the dashboard:**
    Open your browser and navigate to `http://127.0.0.1:5000`.

---

### 📚 Usage

The dashboard allows you to select a country from a dropdown menu to visualize the number of confirmed COVID-19 cases over time. You can switch between line and bar charts for different views.

---

### 📄 Data Source

The data used in this project is sourced from the CSSE (Center for Systems Science and Engineering) data repository at **Johns Hopkins University**.

* **Source URL:** `https://github.com/CSSEGISandData/COVID-19`

---
### 🤝 Contribution

Contributions are welcome! If you have an idea or find a bug, please open an _issue_ or submit a _pull request_.
