def decide_trades(current_data, cash, holdings):
    """
    Buys stocks with positive trends and sells stocks with negative trends.
    Args:
        current_data (pd.DataFrame): Stock data available up to the current date.
        cash (float): Current cash available.
        holdings (dict): Current stock holdings.
    Returns:
        dict: Trading decisions in the format {stock: (action, quantity)}.
    """
    last_row = current_data.iloc[-1]
    prev_row = current_data.iloc[-2] if len(current_data) > 1 else last_row
    decisions = {}
    
    for stock in holdings:
        current_price = last_row[stock]
        previous_price = prev_row[stock]
        
        if current_price > previous_price:  # Positive trend
            quantity_to_buy = min(1, cash / current_price)
            decisions[stock] = ("buy", quantity_to_buy)
        elif current_price < previous_price:  # Negative trend
            decisions[stock] = ("sell", min(1, holdings[stock]))
    
    return decisions
