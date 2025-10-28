# Capstone: SpaceX Falcon 9 First Stage Landing Prediction

This repository contains all notebooks and artifacts for the Applied Data Science Capstone.

## How to run locally
1. Create a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the notebooks in Jupyter and run in order:
   - 01_data_collection.ipynb (web scraping + API)
   - 02_wrangling_eda.ipynb (cleaning + visual EDA)
   - 03_sql_eda.ipynb (SQL-based EDA)
   - 04_folium_map.ipynb (interactive map)
   - 05_plotly_dash.ipynb or app/dash_app.py (interactive dashboard)
   - 06_classification_model.ipynb (model training and evaluation)

## Contents
- `notebooks/` — all analysis notebooks.
- `app/dash_app.py` — minimal Plotly Dash app that loads the processed dataset and offers interactive charts.
- `figs/` — images exported for the presentation.
- `slides/capstone_presentation.pdf` — final slides for peer review.

## Dataset
SpaceX Falcon 9 & Falcon Heavy launch records scraped from Wikipedia + additional data collected via API where applicable.

