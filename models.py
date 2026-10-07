import joblib

LOGISTIC_MODEL_PATH = "models/Logistic/breast_cancer_model.pkl"
LOGISTIC_SCALER_PATH = "models/Logistic/scaler.pkl"


def read_logistic_files():
    model = joblib.load(LOGISTIC_MODEL_PATH)
    scaler = joblib.load(LOGISTIC_SCALER_PATH)

    return model, scaler