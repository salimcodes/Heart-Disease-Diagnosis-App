# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:00:32 2020

@author: OYINLOLA SALIM O
"""

import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in = open('Heart Disease Algorithm.pkl', 'rb')
Classifier = pickle.load(pickle_in)

def welcome():
    return "Welcom all to Oyinlola Salim Olanrewaju's algorithm"

def heart_diagnosis(age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal):
    prediction= Classifier.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    print(prediction)
    return "Given that patients with heart disease have an output of 1 and those without have an output of 0, the patient's output is" + str(prediction)

def main():
    st.title("Heart Disease Diagnosis Model")
    html_temp= """ 
    <div style ="background-colour: tomato; padding: 10px"
    <h2 style = "color:white; text-align:center;">Streamlit Heart Disease Diagnostic App </h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html = True)
    age = st.text_input("Age","TYPE HERE: ")
    sex = st.text_input("Sex","TYPE HERE: ")
    cp = st.text_input("Level of the CPK enzyme in the blood", "TYPE HERE: ")
    trestbps = st.text_input(" Level of TRESTBPS", "TYPE HERE: ")
    chol = st.text_input("Cholestrol Level ", "TYPE HERE: ")
    fbs = st.text_input("FBS Level", "TYPE HERE: ")
    restecg = st.text_input("REST ECG", "TYPE HERE: ")
    thalach = st.text_input("THALACH Level ", "TYPE HERE: ")
    exang = st.text_input("EXANG Level", "TYPE HERE: ")
    oldpeak = st.text_input("OLD Peak", "TYPE HERE: ")
    slope = st.text_input("SLOPE", "TYPE HERE: ")
    ca = st.text_input("CA","TYPE HERE: ")
    thal = st.text_input("THAL","TYPE HERE: ")
    result = ""
    if st.button("Predict"):
        result = heart_diagnosis(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    st.success("The patient's diagnosis is {}".format(result))
    if st.button("Prediction Note"):
        st.text("0 = Patient tested Negative, 1 = Patient tested Positive")
        
if __name__=='__main__':
    main()