# stock_dashboard.py
import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 Stock Price Dashboard")

ticker = st.text_input("Enter Stock Ticker (e.g. AAPL, TSLA)", "AAPL")

if st.button("Get Data"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="6mo")

    st.subheader(f"Showing last 6 months of {ticker} stock prices")
    st.line_chart(hist["Close"])

    st.subheader("📊 Summary Stats")
    st.write(hist.describe())