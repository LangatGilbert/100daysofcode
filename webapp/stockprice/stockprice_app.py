import yfinance as yf
import streamlit as st
import numexpr as ne
import pandas as pd
#HERE: reset number of vml-threads
ne.set_vml_num_threads(4)

#App header
st.write("""
# STOCK PRICES APP

Shown are the stock closing price and volume for Google!
""")

#defining a ticker symbol
tickerSymbol = 'GOOGL'

#getting data from ticker
tickerData = yf.Ticker(tickerSymbol)

#getting historical prices from the ticker
tickerDf= tickerData.history(period ="1d", start = '2010-05-31', end = '2020-05-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
