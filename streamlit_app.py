

import requests
import pandas as pd
import streamlit as st
from datetime import datetime

# 使用 Streamlit 接收用戶輸入的股票代碼
stock_code = st.text_input('請輸入股票代碼', '2330')

# 如果用戶輸入了股票代碼，則進行數據查詢
if stock_code:
    # 構建請求URL
    url = f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={datetime.now().strftime("%Y%m%d")}&stockNo={stock_code}'

    # 發送HTTP請求
    response = requests.get(url)
    
    # 檢查HTTP請求狀態碼
    if response.status_code == 200:
        data = response.json()
        
        # 檢查數據狀態
        if data['stat'] == 'OK':
            # 解析數據
            fields = data['fields']
            rows = data['data']

            # 將數據轉換為DataFrame
            df = pd.DataFrame(rows, columns=fields)

            # 將日期欄位轉換為datetime格式
            df['日期'] = pd.to_datetime(df['日期'])

            # 顯示DataFrame
            st.write(f"股票代碼：{stock_code}")
            st.write(f"股票名稱：{data['title'].split(' ')[1]}")  # 從標題中提取股票名稱
            st.write(f"最新收盤價：{df['收盤價'].iloc[-1]}")
            st.write(df)
        else:
            st.error("無法獲取股票數據: " + data['stat'])
    else:
        st.error("HTTP請求失敗，狀態碼: " + str(response.status_code))




















