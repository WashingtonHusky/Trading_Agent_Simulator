def decide_trades(current_data, cash, holdings):
    """
    Improved strategy: Use Exponential Moving Average (EMA) Crossover with reversed logic for buying and selling decisions.

    Args:
        current_data (pd.DataFrame): Stock data up to the current date.
        cash (float): Available cash.
        holdings (dict): Current stock holdings.

    Returns:
        dict: Trading decisions in the format {stock: (action, quantity)}.
    """
    last_row = current_data.iloc[-1]  
    decisions = {}

    for stock in current_data.columns[1:]:  
        stock_data = current_data[stock]

        if len(stock_data) < 26:  
            continue

        # Calculate the short-term (12-day) and long-term (26-day) EMAs
        ema_short = stock_data.ewm(span=12, adjust=False).mean()
        ema_long = stock_data.ewm(span=26, adjust=False).mean()

        ema_short_last = ema_short.iloc[-1]  
        ema_long_last = ema_long.iloc[-1]  

        price_last = last_row[stock]  

        # Buy signal: Short-term EMA crosses below long-term EMA 
        if ema_short_last < ema_long_last and (ema_short.iloc[-2] >= ema_long.iloc[-2]):
            quantity_to_buy = int(cash // price_last)   # Buy as many as possible
            if quantity_to_buy > 0:
                decisions[stock] = ("buy", quantity_to_buy)

        # Sell signal: Short-term EMA crosses above long-term EMA
        if stock in holdings and holdings[stock] > 0:
            if ema_short_last > ema_long_last and (ema_short.iloc[-2] <= ema_long.iloc[-2]):
                decisions[stock] = ("sell", holdings[stock])  # Sell all holdings of the stock

    return decisions
