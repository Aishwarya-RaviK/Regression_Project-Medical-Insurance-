import pandas as pd
import numpy as np
import streamlit as st
import pickle 

loaded_model=pickle.load(open("C:/Users/ASUS/Downloads/dt_regression_model (2).sav","rb"))

def premium_prediction(input_data):
    input_data=np.asarray(input_data)
    input_data_reshape=input_data.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshape)
    print(prediction)

def main():
    st.title('Health Insurance Premium ')

    Age=st.text_input('Age')
    Gender=st.text_input('Gender')
    Bmi=st.text_input('Bmi')
    Children=st.text_input('Children')
    Smoker=st.text_input('Smoker')
    Region=st.text_input('Region')

    premium_prediction=" "
    

    if st.button('Result'):
        premium_prediction=premium_prediction([Age,Gender,Bmi,Children,Smoker,Region])

    st.success(premium_prediction)

if __name__ == '__main__':
    main()