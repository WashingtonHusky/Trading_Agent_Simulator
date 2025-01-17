import pandas as pd
def decide_trades(current_data, cash, holdings, moment_period=20, buy_thre=0.05, sell_thre=0.05):
    """
    Mean Reversion Strategy.
    
    Args:
        current_data (pd.DataFrame): Stock data available up to the current date.
        cash (float): Current cash available.
        holdings (dict): Current stock holdings.
        moment_period (int): Number of days to look back for moving average.
        buy_thre (float): Threshold percentage below moving average to trigger.
        sell_thre (float): Threshold percentage above moving average to trigger sell (default is 5%).
        
    Returns:
        dict: Trading decisions in the format {stock: (action, quantity)}.
    """

    current_data = current_data.apply(pd.to_numeric, errors='coerce')  # Convert all columns to numeric
    moving_avg = current_data.rolling(window=moment_period).mean()  # Calculate the moving average for the last 'moment_period' days for each stock

    decisions = {}

    for stock in current_data.columns:
        current_price =current_data[stock].iloc[-1]  # Get the most recent price
        current_mavg = moving_avg[stock].iloc[-1]  # Get the most recent moving average
        
        price_diff = (current_price - current_mavg) / current_mavg # Calculate the difference between the current price and moving average

        
        if price_diff < -buy_thre: 
            action = "buy"
            quantity = min(1, cash / current_price)  # Buy up to 1 share

        
        elif price_diff> sell_thre and stock in holdings:
            action = "sell"
            quantity = min(holdings[stock], 1)  # Sell up to 1 share

        else:
            action = "hold"
            quantity = 0
        
        decisions[stock] = (action, quantity)

    return decisions

