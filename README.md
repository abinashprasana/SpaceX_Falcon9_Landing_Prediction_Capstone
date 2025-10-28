# 🚀 SpaceX Falcon 9 — First Stage Landing Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A complete end‑to‑end data science workflow to **predict whether the Falcon 9 first stage will land successfully**.  
Built as the **Applied Data Science Capstone (IBM/Coursera)** using real SpaceX launch records, SQL exploration, Folium maps, a Plotly Dash mini‑app, and machine learning.

---

## 📄 Description
This project explores public SpaceX launch data (Falcon 9 & Falcon Heavy) to understand what factors drive first‑stage landing outcomes and to build a classification model.  
The repository includes: data collection (web scraping & APIs), data wrangling, visual/SQL EDA, a Folium map, a minimal Plotly Dash dashboard, and a final ML model with evaluation plots.

---

## 🎯 Benefits
- Practice an **end‑to‑end ML workflow** with reproducible notebooks.
- Strengthen understanding of **EDA (visual + SQL)** and **feature engineering**.
- Learn to build a **lightweight interactive dashboard** with Plotly Dash.
- Produce a **portfolio‑ready** project with clear structure and run steps.

---

## 🔑 Features
- **Data Collection:** Web scraping + API requests (pandas, requests, BeautifulSoup).
- **Data Cleaning/Wrangling:** Type fixes, missing/outlier handling, joins, feature engineering.
- **Visual EDA:** Distributions, correlations, site comparisons (matplotlib/seaborn/plotly).
- **SQL EDA:** Insightful queries with aggregations, joins, and window functions.
- **Geo Insights:** Folium interactive map (markers/choropleth/heatmap).
- **Dashboard:** Plotly Dash app with filters (Launch Site, Payload range) and two charts.
- **Modeling:** Classification (LogReg/Tree/RandomForest/KNN/SVM as needed) with metrics (Accuracy/F1/ROC‑AUC), confusion matrix, ROC curve.

---

## 📁 File Structure
```
SpaceX_Falcon9_Landing_Prediction_Capstone/
├─ Notebook/                     # Jupyter notebooks (data collection, EDA, ML)
├─ app/
│  └─ dash_app.py                # Interactive dashboard
├─ requirements.txt              # Project dependencies
└─ README.md                     # Project documentation (this file)
```

---

## ⚙️ How to Run

1️⃣ **Clone the repo**
```bash
git clone https://github.com/abinashprasana/SpaceX_Falcon9_Landing_Prediction_Capstone.git
cd SpaceX_Falcon9_Landing_Prediction_Capstone
```

2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Open notebooks (recommended order)**
- Data Collection and Wrangling  
- EDA and SQL Exploration  
- Folium Interactive Map  
- Machine Learning Model

4️⃣ **Run the Plotly Dash app (optional, for screenshots)**
```bash
python app/dash_app.py
```
Open the local URL in your browser to interact with the dashboard.

---

## 🧰 Tech Stack
- **Python:** pandas, numpy, matplotlib, seaborn, scikit‑learn, requests, BeautifulSoup  
- **Visualization:** plotly, Folium  
- **Dashboard:** Plotly Dash  
- **SQL:** SQLite (or your local engine via SQL APIs)

---

## 📚 References
SpaceX launch records compiled from public sources (Wikipedia, SpaceX data).  
Educational use only for Coursera IBM Data Science Capstone.

---

## 👤 Author
**Abinash Prasana**  
MSc Artificial Intelligence | Data Science & Software Projects  
📧 abinashprasana400@gmail.com
