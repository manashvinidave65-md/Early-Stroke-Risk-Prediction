# Trained Model Files

This folder contains the trained machine learning model
and preprocessing files used for stroke classification.

## Selected Model

- Algorithm: XGBoost
- Resampling: None
- Decision Threshold: 0.05

## Files

- model.pkl - Trained XGBoost classifier
- preprocessor.pkl - Data preprocessing pipeline
- threshold.pkl - Selected decision threshold
- model_name.pkl - Name of the selected model

## Final Model Performance

| Metric | Score |
|---|---:|
| Accuracy | 77.89% |
| Precision | 15.63% |
| Recall | 80.00% |
| F1-score | 0.2614 |
| ROC-AUC | 0.8469 |

These files will be used for integration with the
Streamlit web application.

## Disclaimer

This model is developed for educational purposes only.
It is not intended for medical diagnosis or clinical use.
