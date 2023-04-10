import pandas as pd
import requests
from io import StringIO

# API URL and request parameters
url = "https://px.hagstofa.is:443/pxis/api/v1/is/Efnahagur/visitolur/1_vnv/1_vnv/VIS01000.px"
params = {
  "query": [],
  "response": {
    "format": "csv"
  }
}


def fetch_data():
    response = requests.post(url, json=params)
    response.raise_for_status()
    response_text = response.text
    data = pd.read_csv(StringIO(response_text))
    
    data = data.loc[:, ['Mánuður', 'Vísitala neysluverðs Vísitala']]
    # Fix format: 1988M05
    data['Mánuður'] = pd.to_datetime(data['Mánuður'], format='%YM%m')
    # rename to date
    data = data.rename(columns={'Mánuður': 'date'})
    # rename to cpi
    data = data.rename(columns={'Vísitala neysluverðs Vísitala': 'cpi'})
    return data

if __name__ == '__main__':
    df = fetch_data()
    df.to_csv('cpi_data.csv', index=False)
