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

#import data
mpesa_df = pd.read_csv("../data/notebook_outputs/aggregated_mpesa_charges.csv")

#setting up the title
st.title("Mpesa Transactions  Data Analysis for Year 2020")

st.markdown("""
This is an hobby project trying to understand my expenses|income during the past year. The Goal is to answer the following"
* Who do I send money often?
* In most cases where do my incomes come from on month-to-month basis?
* Most common merchants I transact with
"""
)

st.sidebar.header("Input A Specific Month of Interest")
selected_year = st.sidebar.selectbox('transactions_cohort', list(reversed(range(2015,2021))))

# Sidebar - Group selection selection
sorted_unique_group = sorted(mpesa_df.transactions_group.unique())
selected_group = st.sidebar.multiselect('transactions_group', sorted_unique_group, sorted_unique_group)

#Filtering data
df_selected_group = mpesa_df[(mpesa_df.transactions_group.isin(selected_group))]# & (mpesa_df.Pos.isin(selected_pos))]

st.header('Display Player Stats of Selected Group(s)')
st.write('Data Dimension: ' + str(df_selected_group.shape[0]) + ' rows and ' + str(df_selected_group.shape[1]) + ' columns.')
st.dataframe(df_selected_group)


#creating select box
st.sidebar.title("Transaction Month")
select = st.sidebar.selectbox('month', ['March', 'April', 'May', 'June', 'July', 'August'], key='1')
