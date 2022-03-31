import globals
import json


class Nemo():

    def __init__(self, client):
        """
        client is used to issue orders
        """
        self.client = client
        self.previous_price = 0

    def process_candle(self, candle_msg:str):
        """This function is called when a new candle_msg is received.
            Candle message is a string of the form:
            'symbol_key' : {'c': [174.3], 'h': [174.3], 'l': [174.19], 'o': [174.19], 's': 'ok', 't': [1643670000], 'v': [1888]}

            Note that there are list, so you can have multiple candles in one message.
        """

        candle_dict = json.loads(candle_msg)
        if globals.affichage:
            globals.data[globals.symboles.index(candle_dict.keys()[0])][0].append(candle_dict['o'])
            globals.data[globals.symboles.index(candle_dict.keys()[0])][1].append(candle_dict['c'])
            globals.data[globals.symboles.index(candle_dict.keys()[0])][2].append(candle_dict['h'])
            globals.data[globals.symboles.index(candle_dict.keys()[0])][3].append(candle_dict['l'])
            globals.data[globals.symboles.index(candle_dict.keys()[0])][4].append(candle_dict['t'])
            globals.argent.append(100000+self.client.gains())
        if 'AAPL' in candle_dict:
            self.buy_aapl_if_pertinent(candle_dict)

            self.sell_aapl_if_pertinent(candle_dict)

            self.previous_price = candle_dict['AAPL']['c']

        
        if 'BINANCE:BTCUSDT' in candle_dict:
            self.buy_binance_if_pertinent(candle_dict)

            self.sell_binance_if_pertinent(candle_dict)
            
            self.previous_price = candle_dict['BINANCE:BTCUSDT']['c']

        
        if 'ATVI' in candle_dict:
            if candle_dict['ATVI']['c'] < self.previous_price:
                if self.client.money > candle_dict['ATVI']['c']:
                    self.client.buy('ATVI', 1)

            if candle_dict['ATVI']['c'] > self.previous_price:
                if self.client.money > candle_dict['ATVI']['c']:
                    if self.client.actions['ATVI'] > 1:
                        self.client.sell('ATVI', 1)
            
            self.previous_price = candle_dict['ATVI']['c']

       
        if 'AMZN' in candle_dict:
            if candle_dict['AMZN']['c'] < self.previous_price:
                if self.client.money > candle_dict['AMZN']['c']:
                    self.client.buy('AMZN', 1)

            if candle_dict['AMZN']['c'] > self.previous_price:
                if self.client.money > candle_dict['AMZN']['c']:
                    if self.client.actions['AMZN'] > 1:
                        self.client.sell('AMZN', 1)
            
            self.previous_price = candle_dict['AMZN']['c']

      
        if 'TSLA' in candle_dict:
            if candle_dict['TSLA']['c'] < self.previous_price:
                if self.client.money > candle_dict['TSLA']['c']:
                    self.client.buy('TSLA', 1)

            if candle_dict['TSLA']['c'] > self.previous_price:
                if self.client.money > candle_dict['TSLA']['c']:
                    if self.client.actions['TSLA'] > 1:
                        self.client.sell('TSLA', 1)
            
            self.previous_price = candle_dict['TSLA']['c']

      
        if 'DIS' in candle_dict:
            if candle_dict['DIS']['c'] < self.previous_price:
                if self.client.money > candle_dict['DIS']['c']:
                    self.client.buy('DIS', 1)

            if candle_dict['DIS']['c'] > self.previous_price:
                if self.client.money > candle_dict['DIS']['c']:
                    if self.client.actions['DIS'] > 1:
                        self.client.sell('DIS', 1)
            
            self.previous_price = candle_dict['DIS']['c']

    def sell_binance_if_pertinent(self, candle_dict):
        if candle_dict['BINANCE:BTCUSDT']['c'] < self.previous_price:
            if self.client.money > candle_dict['BINANCE:BTCUSDT']['c']:
                self.client.buy('BINANCE:BTCUSDT', 1)

    def buy_binance_if_pertinent(self, candle_dict):
        if candle_dict['BINANCE:BTCUSDT']['c'] > self.previous_price:
            if self.client.money > candle_dict['BINANCE:BTCUSDT']['c']:
                if self.client.actions['BINANCE:BTCUSDT'] > 1:
                    self.client.sell('BINANCE:BTCUSDT', 1)

    def sell_aapl_if_pertinent(self, candle_dict):
        if candle_dict['AAPL']['c'] > self.previous_price:
            if self.client.money > candle_dict['AAPL']['c']:
                if self.client.actions['AAPL'] > 1:
                    self.client.sell('AAPL', 1)

    def buy_aapl_if_pertinent(self, candle_dict):
        if candle_dict['AAPL']['c'] < self.previous_price:
            if self.client.money > candle_dict['AAPL']['c']:
                self.client.buy('AAPL', 1)

  

        
            
    

