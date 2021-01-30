#modules/packages required
import os

import base64

#for data manipulation/wrangling
import numpy as np
from numpy import int64
import pandas as pd

#for data visualization
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

#for date manipulation
import datetime as datetime
import calendar

#dashboard creation
import streamlit as st


# #for pdf extraction as pdf
# import tabula

# Supress unnecessary warnings so that presentation looks clean
import warnings
warnings.filterwarnings('ignore')


#setting up the title
st.title("Analyse your MPESA usage")

st.markdown("""
This is an hobby project trying to understand my expenses|income during a specified period. The Goal is to answer the following:"
* Common Income streams 
* Common expenses
* Most common merchants
"""
)

#insert file uploading sidebar

uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"]) 

#@st.cache
#import data
mpesa_df = pd.read_csv(uploaded_file)


st.sidebar.header("Input A Specific Month of Interest")
selected_year = st.sidebar.selectbox('Transactions Year', list(reversed(range(2019,2021))))

# Sidebar - Group selection selection
sorted_unique_group = sorted(mpesa_df.transactions_group.unique())
selected_group = st.sidebar.multiselect('transactions_group', sorted_unique_group, sorted_unique_group)


#creating select box
st.sidebar.title("Transaction Month")
sorted_month_group = sorted(mpesa_df.month.unique())
month_group = st.sidebar.multiselect('month', sorted_month_group, sorted_month_group)

#Filtering data
df_selected_group = mpesa_df[(mpesa_df['year']==selected_year) & (mpesa_df.month.isin(month_group)) & (mpesa_df.transactions_group.isin(selected_group))]

st.header('Display Transactions Stats of Selected Group(s)')
st.write('Data Dimension: ' + str(df_selected_group.shape[0]) + ' rows and ' + str(df_selected_group.shape[1]) + ' columns.')
st.dataframe(df_selected_group)

# #filtering data per the month
# df_month_group = mpesa_df[(mpesa_df.month.isin(month_group))]


# st.header('Display the Monthly Stats of Selected Group(s)')
# st.write('Data Dimension: ' + str(df_month_group.shape[0]) + ' rows and ' + str(df_month_group.shape[1]) + ' columns.')
# st.dataframe(df_month_group)

#Download the csv file.
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href = "data:file/csv;base64,{b64}" download = "df_selected_group.csv">Download CSV File </a>'
    return href

st.markdown(filedownload(df_selected_group), unsafe_allow_html = True)


#select = st.sidebar.selectbox('month', ['January','February','March', 'April', 'May', 'June', 'July', 'August'], key='1')
