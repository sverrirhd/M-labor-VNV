import pandas as pd
import plotly.express as px

def generate_dashboard():
    data = pd.read_csv('cpi_data.csv')
    fig = px.line(data, x='date', y='cpi', title='CPI Interactive Dashboard')
    fig.write_html('index.html', auto_open=True)

if __name__ == '__main__':
    generate_dashboard()
