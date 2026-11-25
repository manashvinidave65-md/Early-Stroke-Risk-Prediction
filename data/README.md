# Stroke Prediction Dataset

## Dataset Source

This project uses the publicly available Stroke Prediction Dataset from Kaggle.

**Source:** https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

## Dataset Overview

| Property | Value |
|---|---:|
| Total records | 5,110 |
| Total columns | 12 |
| Model input features | 10 |
| Non-stroke records | 4,861 |
| Stroke-positive records | 249 |
| Missing BMI values | 201 |
| Duplicate rows | 0 |
| Stroke-positive percentage | 4.87% |
| Non-stroke percentage | 95.13% |

## Dataset Attributes

| Attribute | Description |
|---|---|
| id | Unique record identifier |
| gender | Gender of the individual |
| age | Age in years |
| hypertension | Presence of hypertension |
| heart_disease | Presence of heart disease |
| ever_married | Marital status |
| work_type | Employment category |
| Residence_type | Urban or rural residence |
| avg_glucose_level | Average glucose level |
| bmi | Body Mass Index |
| smoking_status | Smoking history |
| stroke | Target variable (0 or 1) |

## Data Preprocessing

- Removal of the ID column
- Median imputation for numerical features
- Most-frequent imputation for categorical features
- One-hot encoding
- Standardization
- Stratified train-test splitting
- SMOTE-based class rebalancing on training data

## Download Instructions

1. Visit the Kaggle dataset link provided above.
2. Download and extract the dataset.
3. Place healthcare-dataset-stroke-data.csv inside this directory.
4. For Google Colab execution, upload the CSV when prompted by the notebook.

## Disclaimer

This dataset is used for educational and machine learning research purposes. Refer to the original dataset source for licensing and usage conditions.
