# Consumer Price Index (CPI) Interactive Dashboard

This repository contains an interactive dashboard displaying the Consumer Price Index (CPI) data from [Hagstofan](https://www.statice.is/) using their PxWeb API. The dashboard is coded in Python and hosted on GitHub Pages. You can look at the dashboard on: https://sverrirhd.is/Maelabord-VNV/

## Features

- Fetches the CPI data from Hagstofan's PxWeb API
- Generates an interactive dashboard using plotly
- Hosted on GitHub Pages for easy access and maintenance

## Getting Started

To set up the project locally, follow these steps:

1. Clone the repository:
<pre>
git clone https://github.com/sverrirhd/Maelabord-VNV.git
</pre>


2. Create a virtual environment and activate it with virtualenv:
<pre>
python -m virtualenv python3.8.10 venv
venv/bin/activate.ps1
</pre>


3. Install the required packages:
<pre>
pip install -r requirements.txt
</pre>


4. Run the `fetch_data.py` script to fetch the CPI data and save it as a CSV file:
<pre>
python fetch_data.py
</pre>


5. Run the `generate_dashboard.py` script to generate the interactive dashboard and save it as an `index.html` file:
<pre>
python generate_dashboard.py
</pre>


6. Open the `index.html` file in your browser to view the interactive dashboard.

## Deployment

The interactive dashboard is hosted on GitHub Pages. To update the dashboard, simply push the latest `index.html` file to the repository, and GitHub Pages will automatically update the live dashboard.

## Custom Domain

The dashboard can be accessed from a custom domain (e.g., "sverrirhd.is" or "sverrirhd.is/VNV") by updating the domain's DNS settings and configuring the GitHub Pages repository to use the custom domain.

## Built With

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/)
- [GitHub Pages](https://pages.github.com/)

## Author

- Sverrir Heiðar Davíðsson - (Github: [SverrirHD](https://github.com/sverrirhd))

## License

This project is licensed under the MIT License