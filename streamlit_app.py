

import streamlit as st
import twstock
import pandas as pd

# Streamlit 應用標題
st.title('台灣股票資訊查詢')

# 允許用戶輸入股票代碼
stock_symbol = st.text_input('請輸入股票代碼（例如：2330）：')

if stock_symbol:
    try:
        # 獲取股票資料
        stock = twstock.Stock(stock_symbol)
        
        # 獲取股票中文名稱
        stock_name = twstock.codes[stock_symbol].name
        
        # 顯示股票中文名稱
        st.subheader(f'股票名稱：{stock_name}')
        
        # 獲取股票歷史數據
        stock_data = stock.fetch_from(2022, 1)  # 從2022年開始的數據

        # 轉換為 DataFrame
        df = pd.DataFrame(stock_data, columns=[
            'Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change', 'Transaction'
        ])

        # 顯示股票歷史價格走勢
        st.subheader('歷史價格走勢')
        st.line_chart(df.set_index('Date')['Close'])

        # 獲取最近一個交易日的收盤價
        latest_price = stock.price[-1]

        st.subheader('最近收盤價')
        st.write(f'最近一個交易日的收盤價：${latest_price:.2f}')
    except Exception as e:
        st.error(f'發生錯誤：{e}')


















