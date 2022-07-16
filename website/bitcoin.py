import requests
from flask import render_template
import redis

redis = redis.Redis(host = "redis", port = 6379)

#the URL ticker to get the .json file of the bitcoin currency
BITCOIN_TICKER_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

#the URL history to get the .json file of the bitcoin currency
BITCOIN_HISTORY_URL = "https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10"

#the required time for caulculting the average bitcoin price (in minutes)
REQIUIRED_TIME = 10


def get_current_bitcoin_price():
    response = requests.get(BITCOIN_TICKER_URL).json()
    redis.set("bitcoin_current_price",response["bpi"]["USD"]["rate"])
    return response["bpi"]["USD"]["rate"]

#the average is for the last 10 minutes
def get_average_bitcoin_price():
    average_price = 0.0
    response = requests.get(BITCOIN_HISTORY_URL).json()

    for minute in range(REQIUIRED_TIME):
        average_price = average_price + (response['Data']["Data"][minute]['close'])

    redis.set("bitcoin_average_price",average_price)
    return average_price/REQIUIRED_TIME

#shows contents on screen
def show_content():
    
        #gets price and updates database
        bitcoin_current_price = get_current_bitcoin_price()
        
        #gets average and updates database
        bitcoin_average_price = get_average_bitcoin_price()

        #updates website renderer
        return render_template("home_page.html" ,price=bitcoin_current_price ,average=bitcoin_average_price)