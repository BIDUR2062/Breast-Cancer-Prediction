import streamlit as st
from models import read_logistic_files
import numpy as np

logistic_model,logistic_scaler = read_logistic_files()

st.set_page_config(
    page_title='Breast Cancer Prediction'
)

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

def Home():
    st.header("Breast Cancer Prediction")
    st.write("This application predicts whether a breast tumor is benign or malignant based on input features")

Home()
# 'Clump Thickness', 'Uniformity of Cell Size',
#'Uniformity of Cell Shape', 'Marginal Adhesion',
#'Single Epithelial Cell Size', 'Bare Nuclei', 
# 'Bland Chromatin',
#'Normal Nucleoli', 'Mitoses', 'Class'

st.header(
    'Input Features'
)

Clump_Thickness =st.slider(
    'Clump Thickness',
    max_value=10,
    min_value=1,
    value=1,
    step=1
)

Uniformity_of_Cell_Size = st.slider(
    'Uniformity of Cell Size',
    max_value=10,
    min_value=1,
    step=1,
    value = 1
)

Uniformity_of_Cell_Shape = st.slider(
    'Uniformity of Cell Shape',
    max_value=10,
    min_value=1,
    step=1,
    value=1
)

Marginal_Adhesion = st.slider(
    "Marginal Adhesion",
    max_value=10,
    min_value=1,
    value=1,
    step=1
)

Single_Epithelial_Cell_Size = st.slider(
    "Single Epithelial Cell Size",
    max_value=10,
    min_value=1,
    value=1,
    step=1
)

Bare_Nuclei = st.slider(
    "Bare Nuclei",
    max_value=10,
    min_value=1,
    value=1,
    step=1
)

Bland_Chromatin = st.slider(
    "Bland Chromatin",
    max_value=10,
    min_value=1,
    step=1,
    value=1
)

Normal_Nucleoli = st.slider(
    "Normal Nucleoli",
    max_value=10,
    min_value=1,
    value=1,
    step=1
)

Mitoses = st.slider(
    "Mitoses",
    max_value=10,
    min_value=1,
    step=1,
    value=1
)

if st.button('Predict Breast Cancer'):
    input_data = np.array([[
  Clump_Thickness,Uniformity_of_Cell_Size,Uniformity_of_Cell_Shape,Marginal_Adhesion,Single_Epithelial_Cell_Size,Bare_Nuclei,Bland_Chromatin,Normal_Nucleoli,Mitoses
    ]])
    input_scale = logistic_scaler.transform(input_data)
    prediction = logistic_model.predict(input_scale)[0]
    
    if prediction == 2:
        st.write('Prediction: Benign(non cancerous)')
    else:
        st.warning('prediction: malignant(Cancerous)')