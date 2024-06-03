

import streamlit as st
import twstock
import pandas as pd
from datetime import datetime

st.title('台股股票信息查询')

# 允许用户输入股票代码
stock_symbol = st.text_input('请输入股票代码（例如：2330）：')

if stock_symbol:
    try:
        # 从 twstock 加载股票数据
        stock_data = twstock.Stock(stock_symbol)
        
        # 获取股票实时信息
        stock_info = stock_data.data[-1]  # 这里需要使用整数索引
        stock_date = stock_info[0]
        stock_name = stock_data.sid  # 获取股票名称
        
        st.subheader('股票实时信息')
        st.write({
            "股票名称": stock_name,
            "日期": stock_date.strftime("%Y-%m-%d"),
            "收盘价": stock_info[6],
            "开盘价": stock_info[3],
            "最高价": stock_info[4],
            "最低价": stock_info[5],
            "成交量": stock_info[1]
        })
        
        # 获取股票历史价格数据
        stock_history = stock_data.fetch_from(2022, 1)
        
        # 将历史价格数据转换为 DataFrame 格式
        df = {
            '日期': [data.date for data in stock_history],
            '收盘价': [data.close for data in stock_history]
        }
        df = pd.DataFrame(df)
        
        st.subheader('历史价格走势')
        st.line_chart(df.set_index('日期')['收盘价'])
        
        # 获取最新交易日的股票收盘价
        latest_price = stock_info[6]
        
        st.subheader('最新收盘价')
        st.write(f'最新交易日的收盘价：{latest_price:.2f}')
    except Exception as e:
        st.error('出现错误：' + str(e))




















