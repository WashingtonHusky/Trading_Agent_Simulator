def decide_trades(current_data, cash, holdings):
    """
    Allocates cash evenly across all available stocks.
    Args:
        current_data (pd.DataFrame): Stock data available up to the current date.
        cash (float): Current cash available.
        holdings (dict): Current stock holdings.
    Returns:
        dict: Trading decisions in the format {stock: (action, quantity)}.
    """
    last_row = current_data.iloc[-1]
    decisions = {}
    num_stocks = len(holdings)
    
    if num_stocks > 0:
        cash_per_stock = cash / num_stocks
        
        for stock in holdings:
            current_price = last_row[stock]
            quantity_to_buy = min(1, cash_per_stock / current_price)
            decisions[stock] = ("buy", quantity_to_buy)
    
    return decisions
