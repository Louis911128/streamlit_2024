pip install  twstock

import streamlit as st
import twstock
import pandas as pd
from datetime import datetime

st.title('台股股票信息查尋')

# 允许用户输入股票代码
stock_symbol = st.text_input('請输入股票代碼（例如：2330）：')

if stock_symbol:
    try:
        # 从 twstock 加载股票数据
        stock_data = twstock.Stock(stock_symbol)
        
        # 获取股票实时信息
        stock_info = stock_data.data[-1]  # 这里需要使用整数索引
        stock_date = stock_info[0]
        
        # 获取股票中文名称
        stock_name = twstock.codes[stock_symbol].name
        
        st.subheader('股票實時信息')
        st.write({
            "股票名稱": stock_name,
            "日期": stock_date.strftime("%Y-%m-%d"),
            "收盤價": stock_info[6],
            "開盤價": stock_info[3],
            "最高價": stock_info[4],
            "最低價": stock_info[5],
            "成交量": stock_info[1]
        })
        
        # 获取股票历史价格数据
        stock_history = stock_data.fetch_from(2022, 1)
        
        # 将历史价格数据转换为 DataFrame 格式
        df = {
            '日期': [data.date for data in stock_history],
            '收盤價': [data.close for data in stock_history]
        }
        df = pd.DataFrame(df)
        
        st.subheader('歷史價格走势')
        st.line_chart(df.set_index('日期')['收盤價'])
        
        # 获取最新交易日的股票收盘价
        latest_price = stock_info[6]
        
        st.subheader('最新收盤價')
        st.write(f'最新交易日的收盤價：{latest_price:.2f}')
    except Exception as e:
        st.error('出现錯誤：' + str(e))


















