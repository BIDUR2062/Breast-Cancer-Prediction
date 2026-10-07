# Breast Cancer Prediction System

A machine learning-based web application that predicts whether a breast tumor is **Benign** or **Malignant** based on input cell characteristics.

The application is built with **Python, Scikit-learn, and Streamlit** and provides an easy-to-use interface for making predictions from medical diagnostic features.

> **Disclaimer:** This project is intended for educational and demonstration purposes only. It is not a medical diagnostic tool and should not be used as a substitute for professional medical advice.

## Live Demo

**[Breast Cancer Prediction System](https://breast-cancer-prediction-nye6dubed58xkmegfvey24.streamlit.app/)**

## Project Overview

Breast cancer is one of the most common types of cancer. Machine learning can be used to analyze patterns in diagnostic data and assist in classifying tumors.

This project uses a supervised machine learning classification model to classify a tumor as:

* **Benign** — Non-cancerous
* **Malignant** — Cancerous

The application allows users to enter the required diagnostic values and receive a prediction through a simple web interface.

## Features

* Breast tumor classification using Machine Learning
* Predicts **Benign** or **Malignant**
* Interactive Streamlit web interface
* Input validation
* Trained machine learning model
* Feature scaling
* Simple and user-friendly dashboard
* Deployed online using Streamlit Community Cloud

## Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Data Preprocessing
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Streamlit Application
   ↓
Prediction
```

## Dataset Features

The model uses diagnostic features describing characteristics of cell nuclei.

| Feature                     | Description                         |
| --------------------------- | ----------------------------------- |
| Clump Thickness             | Thickness of the cell clumps        |
| Uniformity of Cell Size     | Uniformity of cell size             |
| Uniformity of Cell Shape    | Uniformity of cell shape            |
| Marginal Adhesion           | Adhesion of cells at their margins  |
| Single Epithelial Cell Size | Size of individual epithelial cells |
| Bare Nuclei                 | Number/appearance of bare nuclei    |
| Bland Chromatin             | Chromatin characteristics           |
| Normal Nucleoli             | Characteristics of normal nucleoli  |
| Mitoses                     | Number of mitotic figures           |

The original dataset contains diagnostic values generally ranging from **1 to 10** for these characteristics.

## Model

This project uses a **Logistic Regression** classification model.

Logistic Regression is suitable for binary classification problems where the output belongs to one of two classes.

In this project:

```text
Input Features
      ↓
Feature Scaling
      ↓
Logistic Regression
      ↓
Prediction
      ↓
Benign / Malignant
```

## Model Evaluation

The trained model was evaluated using classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-score
* Classification Report

Example classification performance from the model evaluation:

```text
              precision    recall    f1-score

Class 2          0.99       0.96       0.97
Class 4          0.92       0.98       0.95

Accuracy                              0.96
```

The exact performance may vary depending on preprocessing, training data, and model configuration.

## Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Logistic Regression
* Train-Test Split
* Feature Scaling
* Classification Metrics

### Data Processing

* Pandas
* NumPy

### Web Application

* Streamlit

### Model Storage

* Pickle

### Deployment

* Streamlit Community Cloud

## Project Structure

```text
Breast-Cancer-Prediction/
│
├── app.py
│
├── model/
│   ├── breast_cancer_model.pkl
│   └── scaler.pkl
│
├── dataset/
│   └── breast_cancer.csv
│
├── requirements.txt
│
└── README.md
```

> The actual project structure may differ depending on your current repository organization.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Navigate to the Project

```bash
cd Breast-Cancer-Prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Requirements

Example `requirements.txt`:

```text
streamlit
pandas
numpy
scikit-learn
```

## How to Use

1. Open the **live application**.
2. Enter the required diagnostic values.
3. Submit the input.
4. The trained model processes the input.
5. The application displays the predicted result:

   * **Benign**
   * **Malignant**

## Example

```text
Clump Thickness          → 2
Uniformity of Cell Size  → 1
Uniformity of Cell Shape → 1
Marginal Adhesion        → 1
Single Epithelial Size   → 2
Bare Nuclei              → 1
Bland Chromatin          → 2
Normal Nucleoli          → 1
Mitoses                  → 1

Prediction → Benign
```

The example values are for demonstrating the application and should not be interpreted as medical guidance.

## Why This Project?

This project was developed to gain practical experience with:

* Machine learning classification
* Data preprocessing
* Model training
* Model evaluation
* Saving trained ML models
* Building interactive ML applications
* Deploying machine learning applications
* Connecting a trained model with a web interface

## Future Improvements

Possible improvements include:

* Add multiple machine learning models
* Compare model performance
* Add prediction probability
* Improve data visualization
* Add model explainability
* Add feature importance visualization
* Improve UI/UX
* Add automated model retraining
* Add comprehensive input validation

## Disclaimer

This application is created for **educational and demonstration purposes**.

The predictions generated by this system should **not be considered medical advice, diagnosis, or treatment recommendations**. Real-world breast cancer diagnosis should be performed by qualified healthcare professionals using appropriate clinical examinations, imaging, laboratory tests, and medical expertise.

## Author

**Bidur Khanal**

BSc CSIT Student
Python Developer | Data Analyst | AI Enthusiast

### Live Project

**[Open Breast Cancer Prediction System](https://breast-cancer-prediction-nye6dubed58xkmegfvey24.streamlit.app/)**
