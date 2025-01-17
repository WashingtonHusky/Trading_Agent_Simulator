def decide_trades(current_data, cash, holdings):
    """
    Example trading strategy for an agent.
    Args:
        current_data (pd.DataFrame): Stock data available up to the current date.
        cash (float): Current cash available.
        holdings (dict): Current stock holdings.
    Returns:
        dict: Trading decisions in the format {stock: (action, quantity)}.
    """

    last_row = current_data.iloc[-1]
    prev_row = current_data.iloc[-2] if len(current_data) > 1 else last_row
    prev_prev_row = current_data.iloc[-3] if len(current_data) > 2 else prev_row
    decisions = {}
    
    for stock in holdings:
       
        current_price = last_row[stock]
        previous_price = prev_row[stock]
        double_previous_price = prev_prev_row[stock]
        
        # if double_previous_price > previous_price and current_price > previous_price:  # Positive trend
        if (previous_price-double_previous_price<current_price-previous_price<0 and current_price-previous_price>-0.1) or current_price - previous_price<-1:
            quantity_to_buy = min(1, cash / current_price)
            decisions[stock] = ("buy", quantity_to_buy)
        # elif double_previous_price < previous_price and current_price < previous_price:  # Negative trend
        elif previous_price-double_previous_price>current_price-previous_price>0 and current_price-previous_price<0.1 or current_price - previous_price>1:
            decisions[stock] = ("sell", min(1, holdings[stock]))
    
    return decisions