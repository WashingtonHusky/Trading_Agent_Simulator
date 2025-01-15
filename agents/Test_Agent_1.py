def decide_trades(current_data, cash, holdings):
    """
    Buys the stock with the lowest price and sells the most expensive stock held.
    Args:
        current_data (pd.DataFrame): Stock data available up to the current date.
        cash (float): Current cash available.
        holdings (dict): Current stock holdings.
    Returns:
        dict: Trading decisions in the format {stock: (action, quantity)}.
    """
    last_row = current_data.iloc[-1]
    min_price_stock = last_row.iloc[1:].idxmin()
    max_price_stock = max(holdings, key=lambda s: last_row[s] if holdings[s] > 0 else -float('inf'))
    decisions = {}
    
    # Buy the cheapest stock
    if min_price_stock:
        min_price = last_row[min_price_stock]
        quantity_to_buy = min(1, cash / min_price)
        decisions[min_price_stock] = ("buy", quantity_to_buy)
    
    # Sell the most expensive stock
    if holdings[max_price_stock] > 0:
        decisions[max_price_stock] = ("sell", min(1, holdings[max_price_stock]))
    
    return decisions
