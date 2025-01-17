'''
                        ---  \_/  \__
'''

import numpy as np
from math import erf
def phi(x):
    return (1.0 + erf(x / np.sqrt(2.0))) / 2.0

def decide_trades(current_data, cash, holdings):
    dt = 1/252
    decisions = {}
    if current_data.shape[0]< 25:
        return decisions
    # D H
    for stock in holdings:
        action = "sell"
        quantity = holdings[stock]
        decisions[stock] = (action, quantity)
    current_data = current_data.set_index("Date")
    log_returns = np.log(current_data /current_data.shift(1))
    log_returns = log_returns.dropna()
    sgms = log_returns.std() * np.sqrt(dt)
    weights = (sgms**(1/7))/(np.sum(sgms**(1/7)))
    last_row = current_data.iloc[-1]
    def compute_port(sgm,S_t,cash,K):
        p_cash = phi(-( np.log(S_t/K)-0.5 * (sgm**2) * dt)/(sgm * np.sqrt(dt)) )
        p_stock =  1 - phi(-(np.log(S_t/K) + 0.5 * (sgm**2) * dt)/(sgm * np.sqrt(dt)))
        tv = K * p_cash + S_t*p_stock
        p_cash,p_stock = K * p_cash /tv, S_t*p_stock/tv
        return p_cash, p_stock
    for stock in holdings:
        action = 'buy'
        current_price = last_row[stock]
        cash_for_this = weights[stock] * cash
        p_cash, p_stock = compute_port(sgms[stock],current_price,cash_for_this,current_price*1) 
        quantity = (p_stock * cash_for_this)/current_price
        decisions[stock] = (action, quantity)
    return decisions