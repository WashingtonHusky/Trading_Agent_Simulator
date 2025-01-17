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
    # Get the most recent stock data
    last_row = current_data.iloc[-1]

    # Identify the stock with the lowest price
    min_price_stock = last_row.iloc[1:].idxmin()

    # Identify the stock with the highest price among the stocks held
    max_price_stock = (
        max(
            holdings,
            key=lambda s: last_row[s] if holdings.get(s, 0) > 0 else -float('inf')
        )
        if holdings else None
    )

    # Initialize the decisions dictionary
    decisions = {}

    # Buy the cheapest stock if it exists and cash is sufficient
    if min_price_stock and cash > 0:
        min_price = last_row[min_price_stock]
        quantity_to_buy = min(1, cash // min_price)  # Use integer division for clear intent
        if quantity_to_buy > 0:
            decisions[min_price_stock] = ("buy", quantity_to_buy)

    # Sell the most expensive stock if it exists and is held
    if max_price_stock and holdings.get(max_price_stock, 0) > 0:
        sell_quantity = min(1, holdings[max_price_stock])
        if sell_quantity > 0:
            decisions[max_price_stock] = ("sell", sell_quantity)

    return decisions
