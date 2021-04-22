import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 

#machine learning package
#from pycaret.classification import *


st.write("""
# Employee Churn Prediction App

This app predicts the  **Employee** Churn!

Data obtained from [Susanli2016 repo](https://github.com/susanli2016/Machine-Learning-with-Python) in Github.

""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://github.com/LangatGilbert/100daysofcode/tree/master/Employee%20turnover%20prediction/data/HR.csv)
""")

#collect user input feaures into dataframe
uploaded_file = st.sidebar.file_uploader("Upload the csv")


