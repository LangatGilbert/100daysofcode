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

from mpesa_analyser import pdf_cleaner_wrangler

#for pdf extraction as pdf
import tabula
from tabula.io import read_pdf


# Supress unnecessary warnings so that presentation looks clean
import warnings
warnings.filterwarnings('ignore')


#setting up the title
st.title("Analyse your MPESA Transactions")

st.markdown("""
This is an hobby project trying to understand my expenses|income during a specified period. The Goal is to answer the following:"
* Common income streams 
* Common expenses
* Most common merchants
"""
)

st.sidebar.title("File Upload:")

#insert file uploading sidebar
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["pdf"]) 

#input the pdf password
password = st.sidebar.text_input("Input your pdf password","Type Here",type = 'password')

dfs = tabula.read_pdf(uploaded_file,pages="all",multiple_tables=True,password = password,stream=True, lattice=  True)

mpesa_df = pdf_cleaner_wrangler(dfs)

st.sidebar.title("Features Selection")
st.sidebar.text("Select Year of Interest")
selected_year = st.sidebar.selectbox('Transactions Year', list(reversed(range(2019,2021))))

#creating select box
st.sidebar.text("Select Month of Interest")
sorted_month_group = sorted(mpesa_df.month.unique())
month_group = st.sidebar.multiselect('month', sorted_month_group, sorted_month_group)


# Sidebar - Group selection selection
st.sidebar.text("Select the transactions group of interest")
sorted_unique_group = sorted(mpesa_df.transactions_group.unique())
selected_group = st.sidebar.multiselect('transactions_group', sorted_unique_group, sorted_unique_group)


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

#show bar of each cateory
agree = st.button("Click to a visualization")
if agree:
 st.bar_chart(df_selected_group['transactions_group'])

#select = st.sidebar.selectbox('month', ['January','February','March', 'April', 'May', 'June', 'July', 'August'], key='1')
