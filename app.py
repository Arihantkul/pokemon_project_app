import streamlit as st
import pickle
import numpy as np
with open ("C:\\Users\\aa\\Desktop\\Coding\\python\\pokemon\\model.pkl", "rb") as f:
    model=pickle.load(f)
st.title("Pokemon Legendary Predictor")
HP=st.slider("HP",1,255,50)
Attack=st.slider("Attack",1,255,50)
Defense=st.slider("Defense",1,255,50)
Sp_Atk=st.slider("Sp. Atk",1,255,50)
Sp_Def=st.slider("Sp. Def",1,255,50)
Speed=st.slider("Speed",1,255,50)
if st.button("Predict"):
  input_data=np.array([[HP,Attack,Defense,Sp_Atk,Sp_Def,Speed]])
  prediction=model.predict(input_data)
  if prediction[0]:
      st.success("This Pokemon is Legendary!")
  else:
      st.info("This Pokemon is not Legendary.")

