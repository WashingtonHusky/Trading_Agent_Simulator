def decide_trades(current_data, cash, holdings):
    """
    Diversified investment strategy with stop-loss mechanism.
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

    # 1. Diversification - Buy stocks at lower prices
    affordable_stocks = [
        stock for stock in last_row.index[1:] if last_row[stock] > 0
    ]
    num_affordable_stocks = len(affordable_stocks)
    if num_affordable_stocks > 0:
        cash_per_stock = cash * 0.8 / num_affordable_stocks  # 留20%的现金
        for stock in affordable_stocks:
            current_price = last_row[stock]
            quantity_to_buy = int(cash_per_stock // current_price)
            if quantity_to_buy > 0:
                decisions[stock] = ("buy", quantity_to_buy)

    # 2. Stop loss mechanism - sell a stock that has fallen in price
    for stock in holdings:
        if holdings[stock] > 0:
            current_price = last_row[stock]
            previous_price = prev_row[stock]
            if current_price < previous_price * 0.9:  # 价格下降10%时止损
                decisions[stock] = ("sell", holdings[stock])

    return decisions