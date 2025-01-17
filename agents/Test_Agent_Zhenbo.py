import pandas as pd

def decide_trades(current_data, cash, holdings):
    """
    Combines trend-based and relative price-based strategies.
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

    # Convert last_row to numeric, ignore non-numeric data
    last_row = pd.to_numeric(last_row, errors='coerce')

    # Drop stocks with NaN prices
    valid_stocks = last_row.dropna()
    low_price_threshold = valid_stocks.quantile(0.25)  # 25th percentile
    high_price_threshold = valid_stocks.quantile(0.75)  # 75th percentile

    for stock in holdings:
        if stock not in valid_stocks:
            continue  # Skip stocks with invalid prices

        current_price = last_row[stock]
        previous_price = prev_row[stock]

        # Determine if stock has a positive or negative trend
        if current_price > previous_price:  # Positive trend
            if current_price <= low_price_threshold:  # Relative low price
                quantity_to_buy = min(1, cash / current_price)
                decisions[stock] = ("buy", quantity_to_buy)
        elif current_price < previous_price:  # Negative trend
            if current_price >= high_price_threshold and holdings[stock] > 0:  # Relative high price
                decisions[stock] = ("sell", min(1, holdings[stock]))

    return decisions
