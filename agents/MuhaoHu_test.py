def decide_trades(current_data, cash, holdings):
    """
    Buys stocks with the maximum affordable quantity and sells stocks with the maximum held quantity based on enhanced strategy.
    Args:
        current_data (pd.DataFrame): Stock data available up to the current date.
        cash (float): Current cash available.
        holdings (dict): Current stock holdings.
    Returns:
        dict: Trading decisions in the format {stock: (action, quantity)}.
    """
    last_row = current_data.iloc[-1]
    price_columns = current_data.select_dtypes(include='number').columns  # Ensure only numeric columns
    moving_avg = current_data[price_columns].iloc[-20:].mean()  # Calculate 20-day moving average
    decisions = {}

    # Buy stocks that are below their 20-day moving average
    for stock in price_columns:
        if last_row[stock] < moving_avg[stock]:  # Check if stock is undervalued
            min_price = last_row[stock]
            quantity_to_buy = int(cash // min_price)  # Maximum affordable quantity
            if quantity_to_buy > 0:
                decisions[stock] = ("buy", quantity_to_buy)
                cash -= quantity_to_buy * min_price  # Deduct cash for each purchase

    # Sell stocks that are above their 20-day moving average
    for stock, quantity in holdings.items():
        if quantity > 0 and last_row[stock] > moving_avg[stock]:  # Check if stock is overvalued
            decisions[stock] = ("sell", quantity)  # Sell the maximum held quantity

    return decisions
