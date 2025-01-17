def decide_trades(current_data, cash, holdings):
    """
    Buy the stocks that has a higher 14-day average price than the last closing price 
    and sell the stocks that has a lower 14-day average price than last closing price.

    Args:
        current_data (pd.DataFrame): Stock data available up to the current date.
        cash (float): Current cash available.
        holdings (dict): Current stock holdings.
    Returns:
        dict: Trading decisions in the format {stock: (action, quantity)}.
    """

    price = current_data.iloc[:, 1:]
    MA1 = price.rolling(window=1, min_periods=1).mean()
    MA14 = price.rolling(window=14, min_periods=1).mean()
    decisions = {}
    
    # Buy the stocks that has a higher 14-day average price than the last closing price 
    for stock in current_data.iloc[:, 1:].columns:
        if MA1[stock].iloc[-1] < MA14[stock].iloc[-1]:
            quantity_to_buy = max(1, cash // price[stock].iloc[-1])
            decisions[stock] = ("buy", quantity_to_buy)
    
    # Sell the stocks that has a lower 14-day average price than last closing price
        if MA1[stock].iloc[-1] > MA14[stock].iloc[-1]:
            decisions[stock] = ("sell", max(0, holdings[stock]))

    return decisions
