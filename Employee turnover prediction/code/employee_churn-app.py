import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 

from pycaret.classification import load_model, predict_model
from pycaret.utils import check_metric

#machine learning package
#from pycaret.classification import *


st.write("""
# Employee Churn Prediction App

This app predicts the  **Employee** Churn!

Data obtained from [Susanli2016 repo](https://github.com/susanli2016/Machine-Learning-with-Python) in Github.

""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://github.com/LangatGilbert/100daysofcode/blob/master/Employee%20turnover%20prediction/data/example_hr.csv)
""")

#collect user input feaures into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type =["csv"])
input_df = pd.read_csv(uploaded_file)

#Displays the user input features
st.subheader('User Input features')

if uploaded_file is not None:
    st.write(input_df)
else :
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters(shown below)')
    st.write(input_df)

#reading the saved classification model
deployment_28042020 = load_model('../model/employees_churn_model')

#predict the uploaded data
new_prediction = predict_model(deployment_28042020, data=uploaded_file)


check_metric(new_prediction['left'], new_prediction['Label'], metric = 'AUC')

