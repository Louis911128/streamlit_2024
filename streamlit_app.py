
import requests
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

st.title('台股股票信息查询')

# 允许用户输入股票代码
stock_symbol = st.text_input('请输入股票代码（例如：2330）：')

if stock_symbol:
    try:
        # 获取今日日期和一個月前的日期
        today = datetime.now().strftime("%Y%m%d")
        last_month = (datetime.now() - timedelta(days=30)).strftime("%Y%m%d")
        
        # 构建URL
        url = f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={last_month}&stockNo={stock_symbol}'
        
        # 发送HTTP请求
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data['stat'] == 'OK':
                # 提取字段和数据
                fields = data['fields']
                rows = data['data']
                
                # 将数据转换为DataFrame
                df = pd.DataFrame(rows, columns=fields)
                
                # 将日期列转换为datetime格式
                df['日期'] = pd.to_datetime(df['日期'], format='%Y/%m/%d')
                
                # 显示实时信息
                stock_info = df.iloc[-1]
                st.subheader('股票实时信息')
                st.write({
                    "股票名称": stock_symbol,
                    "日期": stock_info['日期'].strftime("%Y-%m-%d"),
                    "收盘价": float(stock_info['收盘价'].replace(',', '')),
                    "开盘价": float(stock_info['开盘价'].replace(',', '')),
                    "最高价": float(stock_info['最高价'].replace(',', '')),
                    "最低价": float(stock_info['最低价'].replace(',', '')),
                    "成交量": int(stock_info['成交股数'].replace(',', ''))
                })
                
                # 显示历史价格数据
                st.subheader('历史价格走势')
                df['收盘价'] = df['收盘价'].str.replace(',', '').astype(float)
                st.line_chart(df.set_index('日期')['收盘价'])
                
                # 显示最新收盘价
                latest_price = float(stock_info['收盘价'].replace(',', ''))
                st.subheader('最新收盘价')
                st.write(f'最新交易日的收盘价：{latest_price:.2f}')
            else:
                st.error('無法獲取股票數據: ' + data['stat'])
        else:
            st.error('HTTP請求失敗，狀態碼: ' + str(response.status_code))
    except Exception as e:
        st.error('出现错误：' + str(e))





















