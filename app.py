import yfinance as yf
import streamlit as st

st.title("🧪 yfinance Test")

ticker = st.text_input("Enter Ticker", value="AAPL")
data = yf.Ticker(ticker).history(period="5d")

st.dataframe(data.tail())
