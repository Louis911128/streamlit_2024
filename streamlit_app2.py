import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# 定義 Alpha Vantage API 的基本 URL 和你的 API 金鑰
ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"
API_KEY = "ROVUPSI1FD3SV3DQ"

st.title('股票資訊查詢')

ticker = st.text_input('請輸入股票代碼 (例如: AAPL)：')

if ticker:
    # 發送請求到 Alpha Vantage API
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "apikey": API_KEY
    }
    response = requests.get(ALPHA_VANTAGE_URL, params=params)
    data = response.json()

    # 檢查 API 回應是否成功
    if "Time Series (Daily)" in data:
        # 將 API 回應轉換為 DataFrame
        stock_data = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
        stock_data.index = pd.to_datetime(stock_data.index)

        # 繪製股價走勢圖
        st.subheader('股價走勢')
        st.line_chart(stock_data['4. close'])

        # 顯示最新股價資訊
        st.subheader('最新股價資訊')
        latest_data = stock_data.iloc[0]
        st.write(latest_data)
    else:
        st.error('無法取得股票資訊，請確認輸入的股票代碼是否正確。')
