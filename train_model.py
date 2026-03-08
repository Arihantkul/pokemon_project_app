#train_model.py 
# random forest regression model to predict pokemon 

import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import  RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
# Load the dataset
df = pd.read_csv('C:\\Users\\aa\\Desktop\\Coding\\python\\pokemon\\Pokemon.csv')
#Select features and target variable
features=["HP","Attack","Defense","Sp. Atk","Sp. Def","Speed"]
X=df[features]
y=df['Legendary']
#train test split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
#train the model
model=RandomForestClassifier(n_estimators=100)
model.fit(X_train,y_train)
#evaluate
preds=model.predict(X_test)
print("Accuracy:", accuracy_score(y_test,preds))

#Save the model
with open("model.pkl","wb") as f:
    pickle.dump(model,f)
#python train_model.py

    



