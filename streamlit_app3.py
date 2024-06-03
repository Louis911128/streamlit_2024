# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:22:22 2024

@author: bbkao4514
"""

import streamlit as st
import pandas as pd
import yfinance as yf

st.title('台股股票信息查尋')

# 允许用户输入股票代码
stock_symbol = st.text_input('請输入股票代碼（例如：2330）：')

if stock_symbol:
    try:
        # 从 Yahoo Finance 加载股票数据
        stock_data = yf.Ticker(f'{stock_symbol}.TW')
        
        # 获取股票实时信息
        stock_info = stock_data.history(period="1d")
        latest_stock_info = stock_info.iloc[-1]
        
        # 获取股票中文名称
        stock_name = stock_data.info['longName']
        
        st.subheader('股票實時信息')
        st.write({
            "股票名稱": stock_name,
            "日期": latest_stock_info.name.strftime("%Y-%m-%d"),
            "收盤價": latest_stock_info['Close'],
            "開盤價": latest_stock_info['Open'],
            "最高價": latest_stock_info['High'],
            "最低價": latest_stock_info['Low'],
            "成交量": latest_stock_info['Volume']
        })
        
        # 获取股票历史价格数据
        stock_history = stock_data.history(period="max")
        
        st.subheader('歷史價格走势')
        st.line_chart(stock_history['Close'])
        
        # 获取最新交易日的股票收盘价
        latest_price = latest_stock_info['Close']
        
        st.subheader('最新收盤價')
        st.write(f'最新交易日的收盤價：{latest_price:.2f}')
    except Exception as e:
        st.error('出现錯誤：' + str(e))






