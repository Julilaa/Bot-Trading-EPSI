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
        if 'AAPL' in candle_dict:
            self.buy_aapl_if_pertinent(candle_dict)

            self.sell_aapl_if_pertinent(candle_dict)

            self.previous_price = candle_dict['AAPL']['c']

    def sell_aapl_if_pertinent(self, candle_dict):
        if candle_dict['AAPL']['c'] > self.previous_price:
            if self.client.money > candle_dict['AAPL']['c']:
                self.client.sell('AAPL', 1)

    def buy_aapl_if_pertinent(self, candle_dict):
        if candle_dict['AAPL']['c'] < self.previous_price:
            if self.client.money > candle_dict['AAPL']['c']:
                self.client.buy('AAPL', 1)

        
            
    

