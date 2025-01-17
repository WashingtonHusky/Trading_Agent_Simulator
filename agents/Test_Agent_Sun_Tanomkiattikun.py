import random
import math

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
    last_row = current_data.iloc[-1, 1:]
    ewma = current_data.iloc[:,1:].ewm(alpha=0.95, adjust=False).mean().iloc[-1]
    decisions = {}
    reversion = last_row.div(ewma) - 1
    reversion_ranked = reversion.rank(ascending=False)
    reversion_ranked[reversion > 0] = 0
    reversion_scaled = reversion_ranked / reversion_ranked.sum()
    target_holdings = reversion_scaled * cash / last_row * 0.97
    for stock in holdings:
        quantity = target_holdings.loc[stock] - holdings[stock]
        if quantity > 1:
            decisions[stock] = ("buy", math.floor(quantity))
        elif quantity < -1:
            decisions[stock] = ("sell", math.floor(-quantity))

    return decisions

