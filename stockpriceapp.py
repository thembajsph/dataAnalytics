import yfinance as yf
import streamlit as st
import pandas as pd
import pandas_datareader.data as web
import datetime  

st.write("""
# Buying TSLA Stock?

### You'll find below the stock closing price and volume of TESLA.

""")

tickerSymbol = 'ICHR'

tickerData = yf.Ticker(tickerSymbol)

# tickerDf = tickerData.history(period='1d', start='2011-1-8', end='2021-1-10')

tickerData.info

# tickerData.calendar
# tickerData.dividends

tickerData.major_holders

tickerData.institutional_holders
 
# tickerData.sustainability

# tickerData.recommendations


# start = datetime.datetime(2012, 1, 3)
# end = datetime.datetime(2021, 4, 15)
# df = web.DataReader("TSLA", 'yahoo', start, end)

# dates =[]
# for x in range(len(df)):
#     newdate = str(df.index[x])
#     newdate = newdate[0:10]
#     dates.append(newdate)

# df['date'] = dates

# st.line_chart(df.Close)
# st.line_chart(df.Volume)

# tsla = web.DataReader("TSLA", 'yahoo', start, end)
# # tsla.info['forwardPE']

# st.write("""


# ### The forward P/E ratio. One of the reason why the stock is sky rocketing. (However, I noticed a slight decrease over the past few days...)

# """)
# # tsla.info['forwardPE']


# st.write("""
# ### As we can see below, the P/E ratio was over 1600 currently by the time I wrote the code (01/10/2021).
# This shows that investors are willing to pay a higher share price today because of growth expectations in the future.
# "The high multiple indicates that investors expect higher growth from the company compared to the overall market.
# A high P/E does not necessarily mean a stock is overvalued." - *Investopedia*

# **If the P/E ratio keeps on decreasing, this would mean that the stock future value is becoming more and more uncertain. A potential decline can happen.**

# """)
# import yahoo_fin.stock_info as si
# tsla_data = si.get_quote_table("TSLA")

# tsla_data

#tickers_list = ["tsla", "aapl", "goog"] # example list
#tickers_data= {} # empty dictionary

#for ticker in tickers_list:
#    ticker_object = yf.Ticker(ticker)

    #convert info() output from dictionary to dataframe
#    temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
#    temp.reset_index(inplace=True)
#    temp.columns = ["Attribute", "Recent"]
    
    # add (ticker, dataframe) to main dictionary
#    tickers_data[ticker] = temp

# st.write("""
# ### Some Data about the company. (Expand if needed)

# """)

# temp = pd.DataFrame.from_dict(tsla.info, orient="index")
# temp.reset_index(inplace=True)
# temp.columns = ["Attribute", "Recent"]
# st.dataframe(temp)

# st.write("""
# ### More historical data.

# """)

# tsla_historical = tsla.history(period="max", interval="1wk")
# st.dataframe(tsla_historical)

st.write("""
### Thank you for reading! - Chris Kagabe

**Disclaimer: This content is for educational purposes only. The Information should not be construed as investment/trading advice and is not meant to be a solicitation or recommendation to buy, sell, or hold any securities mentioned. **

""")
