#modules/packages required
import os

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


#for pdf extraction as pdf
import tabula

# Supress unnecessary warnings so that presentation looks clean
import warnings
warnings.filterwarnings('ignore')

#import data
mpesa_df = pd.read_csv("../data/notebook_outputs/aggregated_mpesa_charges.csv")

#setting up the title
st.title("Mpesa Transactions analysis for March 2020 to Aug 2020:")
st.sidebar.title("Mpesa Transactions analysis for March 2020 to Aug 2020:")
st.markdown("This application is a Mpesa Transactions dashboard for March-August 2020:")
st.sidebar.markdown("This application is a Mpesa Transactions dashboard for March-August 2020:")

#creating select box
st.sidebar.title("Transaction Month")
select = st.sidebar.selectbox('month', ['March', 'April', 'May', 'June', 'July', 'August'], key='1')
