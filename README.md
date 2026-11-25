# Early Stroke Risk Prediction Using Machine Learning and Class Rebalancing

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600)
![Google Colab](https://img.shields.io/badge/Google-Colab-F9AB00?logo=googlecolab&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

## Project Overview

Stroke is a serious health condition that presents significant challenges in healthcare. This project investigates machine learning techniques for identifying patterns associated with stroke occurrence using demographic, lifestyle and health-related attributes.

The project focuses on addressing class imbalance, improving minority-class detection, comparing machine learning algorithms and investigating decision threshold optimization.

This project is aligned with United Nations Sustainable Development Goal 3: Good Health and Well-Being.

## Problem Statement

Healthcare datasets often contain significantly fewer positive cases than negative cases. This imbalance can cause traditional machine learning models to favour the majority class, resulting in poor detection of stroke-positive records despite achieving high overall accuracy.

This project investigates class rebalancing and threshold selection techniques to address this challenge.

## Project Objectives

- Perform comprehensive exploratory data analysis.
- Handle missing values and preprocess input features.
- Address class imbalance using SMOTE.
- Implement Random Forest and XGBoost classifiers.
- Compare models using multiple evaluation metrics.
- Investigate decision threshold optimization.
- Analyse feature importance and classification errors.
- Develop an interactive machine learning prototype.
- Deploy a publicly accessible demonstration website.

## Dataset

The project uses the Stroke Prediction Dataset available on Kaggle.

Dataset source:
https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

| Property | Value |
|---|---:|
| Total records | 5,110 |
| Total columns | 12 |
| Input features | 10 |
| Non-stroke records | 4,861 |
| Stroke-positive records | 249 |
| Missing BMI values | 201 |
| Stroke-positive percentage | 4.87% |

## Input Features

- Gender
- Age
- Hypertension
- Heart disease
- Marital status
- Work type
- Residence type
- Average glucose level
- Body Mass Index (BMI)
- Smoking status

## Project Methodology

1. Dataset collection and inspection
2. Exploratory Data Analysis (EDA)
3. Missing-value handling
4. Stratified train-test splitting
5. One-hot encoding
6. Feature standardization
7. SMOTE-based class rebalancing
8. Random Forest classification
9. XGBoost classification
10. Model performance evaluation
11. Validation-based threshold analysis
12. Feature importance analysis
13. Confusion matrix and error analysis
14. Model serialization
15. Prototype development and deployment (planned)

## Machine Learning Models

### Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve classification performance.

### XGBoost

XGBoost is a gradient boosting algorithm that builds decision trees sequentially to improve predictions by learning from previous errors.

### SMOTE

Synthetic Minority Oversampling Technique (SMOTE) is used to generate synthetic minority-class samples and address class imbalance in the training dataset.

## Initial Model Comparison

| Evaluation Metric | Random Forest | XGBoost |
|---|---:|---:|
| Accuracy | 92.17% | 85.91% |
| Precision | 12.50% | 17.36% |
| Recall | 10.00% | 50.00% |
| F1-score | 0.1111 | 0.2577 |
| ROC-AUC | 0.7529 | 0.8159 |

XGBoost demonstrated better stroke-class recall and ROC-AUC in the initial model comparison.

## Corrected Milestone 2 Evaluation

The selected XGBoost model was evaluated using a decision threshold of 0.30 and its matching fitted preprocessing pipeline.

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 75.73% |
| Precision | 13.33% |
| Recall | 72.00% |
| F1-score | 0.2250 |
| ROC-AUC | 0.8122 |
| Decision threshold | 0.30 |

### Confusion Matrix

| Actual / Predicted | No Stroke | Stroke |
|---|---:|---:|
| No Stroke | 738 | 234 |
| Stroke | 14 | 36 |

The model identified 36 out of 50 stroke-positive test records.

These are corrected Milestone 2 experimental results, not clinically validated performance estimates. Further validation is planned.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- XGBoost
- Joblib
- Google Colab
- GitHub

## Repository Structure

- notebooks/ - Machine learning implementation
- data/ - Dataset documentation and source

Additional folders for model artifacts, visualizations, application code and project reports will be added during further development.

## How to Run

1. Download the dataset from the Kaggle link.
2. Open the notebooks directory.
3. Download the Milestone 2 Jupyter notebook.
4. Open the notebook in Google Colab.
5. Upload the dataset when prompted.
6. Execute all notebook cells sequentially.

## Project Status

### Completed

- [x] Dataset collection and inspection
- [x] Exploratory data analysis
- [x] Data preprocessing
- [x] SMOTE-based class rebalancing
- [x] Random Forest implementation
- [x] XGBoost implementation
- [x] Model comparison
- [x] Decision threshold analysis
- [x] Feature importance analysis
- [x] Error analysis
- [x] Model serialization
- [x] Prediction function
- [x] Preprocessing consistency correction

### Upcoming

- [ ] SMOTENC experimentation
- [ ] Further model validation
- [ ] Final evaluation and model selection
- [ ] Interactive prediction interface
- [ ] Data visualization dashboard
- [ ] Website development
- [ ] Prototype testing
- [ ] Public deployment
- [ ] Final project documentation

## Limitations

- The dataset contains a limited number of stroke-positive records.
- Recall-focused threshold selection increases false-positive predictions.
- Standard SMOTE after one-hot encoding may generate fractional categorical indicators.
- Earlier experiments examined multiple thresholds on the test dataset, limiting its independence as a final evaluation set.
- Further independent validation is required.
- The model has not been clinically validated.

## References

- Stroke Prediction Dataset - Kaggle
- Scikit-learn Documentation
- XGBoost Documentation
- Imbalanced-learn Documentation

## Disclaimer

This project is an educational machine learning research prototype. It is not a clinically validated diagnostic tool and must not be used for medical diagnosis, treatment decisions or individual medical risk assessment.
