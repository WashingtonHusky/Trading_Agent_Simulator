def decide_trades(current_data, cash, holdings):
    """
    Simple strategy: Buy when price is below the moving average, sell when price is above it.
    
    Args:
        current_data (pd.DataFrame): Stock data up to the current date.
        cash (float): Available cash.
        holdings (dict): Current stock holdings.
    
    Returns:
        dict: Trading decisions in the format {stock: (action, quantity)}.
    """
    last_row = current_data.iloc[-1]  # Get the latest row of data
    decisions = {}
    
    for stock in current_data.columns[1:]:  # Skip the date column
        stock_data = current_data[stock]
        
        # Check if there is enough data for calculation
        if len(stock_data) < 15:  # At least 15 days of data are required
            continue
        
        # Calculate the 15-day moving average
        moving_average = stock_data.rolling(window=15).mean()
        ma_last = moving_average.iloc[-1]  # The most recent moving average value
        price_last = last_row[stock]  # The most recent price
        
        # Buy signal: Price is below the 15-day moving average
        if price_last < ma_last:
            quantity_to_buy = int(cash // price_last)  # Calculate how many shares can be bought with the available cash
            if quantity_to_buy > 0:
                decisions[stock] = ("buy", quantity_to_buy)
        
        # Sell signal: Price is above the 15-day moving average
        if stock in holdings and holdings[stock] > 0:
            if price_last > ma_last:
                decisions[stock] = ("sell", holdings[stock])  # Sell all holdings of the stock
    
    return decisions
