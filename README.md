# Trading Agent Simulator

**Designed for Johns Hopkins University Financial Mathematics Master's 2025 Winter Intersection**  
Author: Zheng Cao  
License: [MIT License](LICENSE)

Special thanks to Professor John Miller and many students from the course as contributors.

---

## Overview

The **Trading Agent Simulator** is an educational framework designed to teach and explore algorithmic trading strategies in a simulated environment. Students can develop their own trading agents, simulate trades using historical stock data, and evaluate the performance of their strategies in a controlled, dynamic setting.

---

## Features

- **Stock Simulation**: Generate synthetic stock price data for multiple assets, stored in CSV format.
- **Agent Framework**: Develop custom trading agents to make buy/sell decisions dynamically.
- **Performance Tracking**: Evaluate agent performance over time, combining cash holdings and portfolio value.
- **Collaborative Learning**: Encourages students to experiment with different strategies and compare results.

---

## Structure

- **`stocks/`**: Contains simulated stock price data for different assets.
- **`agents/`**: A folder for student-created trading agents. Each agent is a Python file implementing a `decide_trades` function.
- **`trading_agent_master.ipynb`**: The main notebook for running simulations and visualizing results.
- **`LICENSE`**: Project license under MIT.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Recommended libraries:
  - `pandas`
  - `numpy`
  - `matplotlib` (optional for visualization)

### Steps to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/WashingtonHusky/Trading_Agent_Simulator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Trading_Agent_Simulator
   ```
3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the `trading_agent_master.ipynb` notebook to simulate and evaluate agents.

---

## How to Contribute

1. Fork the repository and create a new branch:
   ```bash
   git checkout -b my-agent-branch
   ```
2. Add your custom agent to the `agents/` folder (e.g., `My_Agent.py`).
3. Test your agent using the `trading_agent_master.ipynb`.
4. Push your changes and submit a pull request!

---

## License

This project is licensed under the [MIT License](LICENSE).  
**Note**: If you use this code in academic work, you must cite the author:

> Cao, Z., "Trading Agent Simulation and Stock Simulator Framework," GitHub repository, https://github.com/WashingtonHusky/Trading_Agent_Simulator.
