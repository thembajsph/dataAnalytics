# Import libraries
import streamlit as st
import math
import pandas_datareader as web
import cufflinks as cf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import datetime
plt.style.use('fivethirtyeight')

st.write("description: this program uses an artificial neural network called lon short Term Memory (LSTM)to prsedict the closing stock price of corporation(Apple Inc.) using the past 60 day stock price.")

# pip install tensorflow






# App title
st.markdown('''
# Stock Price App
Shown are the stock price data for query companies!
**Credits**
- App built by [Chanin Nantasenamat](https://medium.com/@chanin.nantasenamat) (aka [Data Professor](http://youtube.com/dataprofessor))
- Built in `Python` using `streamlit`,`yfinance`, `cufflinks`, `pandas` and `datetime`
''')
st.write('---')

# Sidebar
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 1, 31))

# Retrieving tickers data
ticker_list = pd.read_csv(
    'https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
tickerSymbol = st.sidebar.selectbox(
    'Stock ticker', ticker_list)  # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol)  # Get ticker data
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)

# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)

# Bollinger bands
st.header('**Bollinger Bands**')
qf = cf.QuantFig(tickerDf, title='First Quant Figure', legend='top', name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

####
# st.write('---')
# st.write(tickerData.info)


# my code

# # Get the stock quote
# df = web.DataReader('S32.JO', data_source='yahoo',
#                     start='2012-01-01', end='2021-04-21')
# # Show the data
# df

# df.tail(7)

# # Get the number of row and columns in data set
# df.shape

# # visualize the closing price history
# plt.figure(figsize=(16, 8))
# plt.title('Close Price History')
# plt.plot(df['Close'])
# plt.xlabel('Date', fontsize=18)
# plt.ylabel('Close Price USD ($)', fontsize=18)
# plt.show()

# # Creating a new dataframe with only the 'Close column'
# data = df.filter(['Close'])
# # Convert the dataframe to a numpy array
# dataset = data.values
# # Get the number of rows to train the model on
# training_data_len = math.ceil(len(dataset) * .8)

# training_data_len

# # Scale the data before entered in neural network
# scaler = MinMaxScaler(feature_range=(0, 1))
# scaled_data = scaler.fit_transform(dataset)

# scaled_data

# # Create the training data set
# # Create the scaled the training data set
# train_data = scaled_data[0:training_data_len, :]
# # Split the data into x_train and y_train data sets
# x_train = []
# y_train = []

# for i in range(60, len(train_data)):
#     x_train.append(train_data[i-60:i, 0])
#     y_train.append(train_data[i, 0])
#     if i <= 61:
#         print(x_train)
#         print(y_train)
#         print()

#         # Convert the x_train and y_train to numpy arrays to train the LSTM model
# x_train, y_train = np.array(x_train), np.array(y_train)

# # Build the LSTM model
# model = Sequential()
# model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
# model.add(LSTM(50, return_sequences=False))
# model.add(Dense(25))
# model.add(Dense(1))

# # Compile the model
# model.compile(optimizer='adam', loss='mean_squared_error')

# # Train the model

# model.fit(x_train, y_train, batch_size=1, epochs=1)

# # Create the testing data set
# # Create a new array containing scaled values from index 1802 to 2003
# test_data = scaled_data[training_data_len - 60:, :]
# # Create the data sets x_tests and y_tests
# x_test = []
# y_test = dataset[training_data_len:, :]
# for i in range(60, len(test_data)):
#     x_test.append(test_data[i-60:i, 0])

# # Convert the data into a numpy array
# x_test = np.array(x_test)

# # Reshape the data
# x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# # Get the models predicted price values
# predictions = model.predict(x_test)
# predictions = scaler.inverse_transform(predictions)

# # Get the root mean squared error(RMSE)
# rmse = np.sqrt(np.mean(predictions - y_test)**2)
# rmse

# # Plot the data
# train = data[:training_data_len]
# valid = data[training_data_len:]
# valid['Predictions'] = predictions
# # Visualise the model/data
# plt.figure(figsize=(16, 8))
# plt.title('Model')
# plt.xlabel('Date', fontsize=18)
# plt.ylabel('Close Price USD ($)', fontsize=18)
# plt.plot(train['Close'])
# plt.plot(valid[['Close', 'Predictions']])
# plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
# plt.show()

# # Show the valid and the predicted prices
# valid

# # Get the quote (predict via date)
# apple_quote = web.DataReader(
#     'S32.JO', data_source='yahoo', start='2012-01-01', end='2021-04-19')
# # Create a dataframe
# new_df = apple_quote.filter(['Close'])
# # Get the last 60 days closing price values and convert the dataframe to an array
# last_60_days = new_df[-60:].values
# # Scale the data to be values between 0 and 1
# last_60_days_scaled = scaler.transform(last_60_days)
# # Create an empty list
# x_test = []
# # Append the past 60 days
# x_test.append(last_60_days_scaled)
# # Convert the x_test data set to a numpy array
# x_test = np.array(x_test)
# # Reshape the data
# x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
# # Get the predicted scaled price
# pred_price = model.predict(x_test)
# # undo the scaling
# pred_price = scaler.inverse_transform(pred_price)
# print(pred_price)

# # Get the quote (actual compare)
# apple_quote2 = web.DataReader(
#     'S32.JO', data_source='yahoo', start='2012-04-08', end='2021-04-19')
# print(apple_quote2['Close'])
