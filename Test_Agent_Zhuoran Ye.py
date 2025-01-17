def decide_trades(current_data, cash, holdings):
    last_5_days = current_data.iloc[-5:]
    decisions = {}

    for stock in holdings:
        price_trend = last_5_days[stock].diff().dropna()
        if (price_trend < 0).sum() >= 3:  
            quantity_to_buy = min(2, cash / last_5_days.iloc[-1][stock])
            decisions[stock] = ("buy", quantity_to_buy)
        elif (price_trend > 0).sum() >= 3 and holdings[stock] > 0:  
            decisions[stock] = ("sell", min(2, holdings[stock]))

    return decisions