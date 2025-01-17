def decide_trades(current_data, cash, holdings):
    """
    Strategy:
    1. Datasets is small, Average Reversion, Price > Average, Sell; Price < Average, Buy
    2. Datasets is large, Moving Average, Price > Moving Average, Sell; Price < Moving Average, Buy

    Args:
        current_data (pd.DataFrame): Stock data available up to the current date.
        cash (float): Current cash available.
        holdings (dict): Current stock holdings.
    Returns:
        dict: Trading decisions in the format {stock: (action, quantity)}.
    """
 
    last_row = current_data.iloc[-1]
    decisions = {}
    window = 16

    for stock in holdings:
        previous_prices = current_data[stock] # Get all previous prices for the stock
        current_price = last_row[stock]

        if len(previous_prices) < window:
            current_average = previous_prices.mean() 
            # Buy Signals: current_price < current_average
            if current_price < current_average:
                action = "buy"
                quantity_to_buy = int(cash // current_price)
                decisions[stock] = (action, quantity_to_buy)
            
            # Sell Signals: current_price > current_average
            if holdings[stock] > 0 and current_price > current_average:
                action = "sell"
                quantity_to_sell = holdings[stock]
                decisions[stock] = (action, quantity_to_sell)
            return decisions
        
        else:
            moving_average = previous_prices.rolling(window=window).mean()
            current_ma = moving_average.iloc[-1] # Get the current moving average price

            # Buy Signals: current_price < current_ma
            if current_price < current_ma:
                action = "buy"
                quantity_to_buy = int(cash // current_price)
                decisions[stock] = (action, quantity_to_buy)
            
            # Sell Signals: current_price > current_ma
            if holdings[stock] > 0 and current_price > current_ma:
                action = "sell"
                quantity_to_sell = holdings[stock]
                decisions[stock] = (action, quantity_to_sell)
            return decisions



