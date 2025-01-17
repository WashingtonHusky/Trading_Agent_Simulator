def decide_trades(current_data, cash, holdings):
 
    short_window = 5  
    long_window = 15
    decisions = {}

    for stock in holdings:
        if len(current_data) < long_window:
           
            continue
        
       
        short_sma = current_data[stock].iloc[-short_window:].mean()
        long_sma = current_data[stock].iloc[-long_window:].mean()
        current_price = current_data[stock].iloc[-1]
        
        
        if current_price < short_sma:  
            action = "buy"
            quantity = min(1, cash / current_price)  
        elif current_price > long_sma:  
            action = "sell"
            quantity = min(holdings[stock], 1) 
        else:
            action = None
            quantity = 0
        
        if action:
            decisions[stock] = (action, quantity)
    
    return decisions
