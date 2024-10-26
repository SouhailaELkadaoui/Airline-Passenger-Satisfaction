

# Classification of Airline Passenger Satisfaction

This project aims to explore airline passenger satisfaction factors. It encompasses data cleaning to ensure data quality, followed by data analysis to familiarize ourselves with the dataset. We identify how passenger satisfaction can change across multiple features, such as food delivery, seat comfort, gender, and departure/arrival delays.

To enhance our findings, the project includes the creation of a satisfaction model based on various factors. This phase involves data engineering to identify significant features, applying transformations, and developing three models based on logistic regression, Lasso regularization, and decision trees.

I have added a Streamlit app container in the Dockerfile to predict client satisfaction due to multiple features. 

## Project Workflow

To enhance our findings, the project includes the creation of a satisfaction model based on various factors. This phase involves:

- **Data Engineering**: Identifying significant features and applying necessary transformations.
- **Model Development**: Developing three models based on:
  - Logistic Regression
  - Lasso Regularization
  - Decision Trees 
  -Streamlit application 
  -Docker
## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/SouhailaELkadaoui/Airline-Passenger-Satisfaction.git

## Run docker container
docker run -p 8501:8501 client-satisfaction-prediction-app7
on the browser,write  localhost:8501 (to make it work  locally)

## run streamlit app
localhost:8501

## Dataset: 
The dataset was initially combined before being divided into training and testing sets. We later resplit it during the feature engineering phase to prepare it for modeling. In total, the dataset contains 2,848,714 rows and 23 columns.

[Dataset Link](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)


## Results 
| **Modèle**                          | **Accuracy** | **Precision** | **Recall** | **F1 Score** | **AUC** |
|-------------------------------------|--------------|---------------|------------|--------------|---------|
| **Régression Logistique**            | 0.62         | 0.54          | 0.81       | 0.65         | 0.72    |
| **Régression Logistique avec Lasso** | 0.72         | 0.63          | 0.86       | 0.73         | 0.83    |
| **Arbre de Décision (Critère Gini)** | 0.90         | 0.88          | 0.90       | 0.89         | 0.96    |

**Author:**  
- Souhaila El Kadaoui  






