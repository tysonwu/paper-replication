import os 
import csv
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

data_path = os.getcwd() + '/data/'
currencies = ['bch', 'btc', 'xrp', 'xlm', 'eos', 'eth', 'ltc']

df = {}
for file in currencies:
    df[file] = pd.read_csv(data_path + file + '.csv')
wallet = pd.read_csv(data_path + 'wallet.csv')

columns = {}
for currency in currencies:
    df[currency] = df[currency].fillna(0)
    df[currency] = df[currency][['date','PriceUSD','CapMrktCurUSD']]
    print(df[currency])