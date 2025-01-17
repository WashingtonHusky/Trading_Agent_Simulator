import random

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
    decisions = {}
    for stock in holdings:
        current_price = last_row[stock]
        if random.random() > 0.5:  # Randomly decide to buy or sell
            action = "buy"
            quantity = min(1, cash / current_price)  # Buy up to 1 share
        else:
            action = "sell"
            quantity = min(holdings[stock], 1)  # Sell up to 1 share
        decisions[stock] = (action, quantity)
    return decisions
