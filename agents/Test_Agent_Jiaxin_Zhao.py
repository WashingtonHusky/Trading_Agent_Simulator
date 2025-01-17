import pandas as pd
import numpy as np

def decide_trades(current_data, cash, holdings):
    """
    Mean reversion with dynamic allocation and volatility filtering.
    Args:
        current_data (pd.DataFrame): Stock data available up to the current date.
        cash (float): Current cash available.
        holdings (dict): Current stock holdings.
    Returns:
        dict: Trading decisions in the format {stock: (action, quantity)}.
    """
    window = 20  # Lookback period for calculating moving average and volatility
    z_threshold = 1.5  # Threshold for z-score to act
    last_row = current_data.iloc[-1]
    decisions = {}

    for stock in holdings:
        # Ensure there's enough data for analysis
        if len(current_data[stock]) >= window:
            # Calculate moving average and standard deviation
            past_data = current_data[stock][-window:]
            moving_avg = past_data.mean()
            volatility = past_data.std()
            current_price = last_row[stock]
            
            # Calculate z-score for current price
            z_score = (current_price - moving_avg) / volatility if volatility > 0 else 0

            if z_score < -z_threshold and cash > current_price:
                # Strong buy signal: price far below mean
                action = "buy"
                quantity = min(2, cash // current_price)  # Limit to 2 shares
            elif z_score > z_threshold and holdings[stock] > 0:
                # Strong sell signal: price far above mean
                action = "sell"
                quantity = min(2, holdings[stock])  # Limit to 2 shares
            else:
                # Hold if the signal is weak
                continue

            # Record the decision
            decisions[stock] = (action, quantity)

    return decisions