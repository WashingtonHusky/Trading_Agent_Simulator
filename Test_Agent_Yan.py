import pandas as pd
def preprocess_data(df):
    """
    Preprocesses the DataFrame to ensure all stock price columns are numeric.
    Args:
        df (pd.DataFrame): The input DataFrame with stock price data.
    Returns:
        pd.DataFrame: The cleaned DataFrame with only numeric data in stock columns.
    """
    numeric_columns = df.columns.difference(['Date'])  # Exclude 'Date' column
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')  # Convert to numeric
    df.fillna(method='ffill', inplace=True)  # Forward fill missing values
    df.fillna(method='bfill', inplace=True)  # Backward fill if necessary
    return df

def decide_trades(current_data, cash, holdings, lookback=10):
    """
    Implements a mean reversion strategy.
    Buys stocks that are below their moving average and sells stocks that are above.
    """
    # Preprocess data to ensure numeric values
    current_data = preprocess_data(current_data)
    
    last_row = current_data.iloc[-1]
    decisions = {}

    for stock in current_data.columns.difference(['Date']):
        if stock not in holdings:
            holdings[stock] = 0
        
        try:
            if len(current_data) >= lookback:
                stock_data = current_data[stock]
                moving_average = stock_data.iloc[-lookback:].mean()
                current_price = last_row[stock]
                
                if current_price < moving_average:  # Below the moving average: buy
                    quantity_to_buy = min(1, cash // current_price)
                    decisions[stock] = ("buy", quantity_to_buy)
                elif current_price > moving_average:  # Above the moving average: sell
                    quantity_to_sell = min(1, holdings[stock])
                    decisions[stock] = ("sell", quantity_to_sell)
        except Exception as e:
            print(f"Error processing stock {stock}: {e}")
    
    return decisions
