import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("data/tumor.csv")

features = ['Clump Thickness', 'Uniformity of Cell Size',
       'Uniformity of Cell Shape', 'Marginal Adhesion',
       'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
       'Normal Nucleoli', 'Mitoses']
target = 'Class'

X = df[features]
Y = df[target] 
X_train,X_test,Y_train,Y_test = train_test_split(
    X,Y,test_size=0.2,random_state=42,stratify=Y)

scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)

model = LogisticRegression(
    solver='lbfgs',
    class_weight='balanced',
    random_state=42
)
model.fit(X_train_scale,Y_train)
Y_pred = model.predict(X_test_scale)

with open ("models/Logistic/breast_cancer_model.pkl",'wb') as file :
    joblib.dump(model,file)

with open("models/Logistic/scaler.pkl",'wb') as file:
    joblib.dump(scaler,file)
