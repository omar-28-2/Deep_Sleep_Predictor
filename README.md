# Deep_Sleep_Predictor
📌 Sleep Quality Prediction using Machine Learning 💤 This project aims to analyze and predict sleep quality based on various lifestyle and physiological factors. Using machine learning models, we explore relationships between sleep duration, stress levels, exercise, heart rate, and other key metrics.

# Sleep Quality - Phase 1: Data Preprocessing & Exploration

## 📁 Project Overview
This project explores various factors affecting sleep quality using machine learning. We are currently in **Phase 1**, focusing on **data preprocessing** and **exploratory data analysis (EDA)**.

---

## ✅ Preprocessing Summary

### 🧼 Cleaned Datasets
- `first(374).ipynb`, `second(560).ipynb`, `third(400).ipynb`, `sixth(1000).ipynb`
- Removed duplicate records using `drop_duplicates()`
- Checked and handled missing values
- Standardized column names for consistency (e.g. `Sleep Duration`)
- Categorical encoding applied (e.g., Gender as 0/1)

---

### 🔗 Dataset Merging
- Combined cleaned datasets using `pd.concat(...)`
- Resulting in a single merged dataset (`merge.csv`) with 1959 records
- Re-checked for missing values and duplicates post-merge

---

## 📊 Exploratory Data Analysis (`EDA.ipynb`)
- Created histogram plots for all features to visualize distributions
- Computed correlation matrix to evaluate feature relationships

### 🔍 Key Correlations
- Positive: `Sleep Duration` ↔ `Quality of Sleep` (+0.34)
- Negative: `Stress Level`, `BMI Category`, and `Daily Steps` showed slight negative influence
- Used heatmap to visualize all correlations

---

## 🎯 Ready for Modeling
- Dataset is clean and consistent
- Key features identified for use in ML models
- Next step: apply supervised models to predict `Quality of Sleep`

---

## 👥 Team Instructions
- Use this file as a Phase 1 reference
- Base your Phase 1 report sections on the steps summarized here
