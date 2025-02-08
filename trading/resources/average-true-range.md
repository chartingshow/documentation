## Introduction to Average True Range (ATR)

The Average True Range (ATR) is a technical indicator used in financial markets to measure the volatility of a security’s price. It was developed by J. Welles Wilder Jr. and introduced in his 1978 book “New Concepts in Technical Trading Systems.” The ATR is calculated based on the true range of a security’s price over a specified period, typically 14 days.

### Understanding True Range (TR)

The true range is the greatest of the following three values:

1. The difference between the current high and the current low.
2. The absolute value of the difference between the current high and the previous close.
3. The absolute value of the difference between the current low and the previous close. This calculation provides a measure of the range of price movement for a given trading day, taking into account both the daily high-low range and the overnight price gaps.

### Calculating Average True Range (ATR)

The ATR is calculated by taking an average of the true range values over a specified number of periods. The most common method is to use a simple moving average, but an exponential moving average can also be used. The formula for the first ATR calculation (when there is no previous ATR) is: `ATR = (TR1 + TR2 + … + TRn) / n` Where `n` represents the number of periods (e.g., 14 days).

For subsequent calculations, when an ATR value from the previous period is available, the formula becomes: `ATRnew = ((ATRprevious * (n - 1)) + TRcurrent) / n` This formula incorporates the previous ATR value and the current true range to calculate the new ATR, smoothing out fluctuations over time.

### Interpretation of ATR

The ATR provides several key pieces of information to traders and investors:

- **Volatility Measurement:** A higher ATR value indicates higher volatility, suggesting that the price is moving more rapidly. A lower ATR value indicates lower volatility, suggesting that the price is moving more slowly.
- **Stop-Loss Placement:** The ATR can be used to determine where to place stop-loss orders, as it gives an indication of the average price movement.
- **Position Sizing:** Traders can use the ATR to adjust their position sizes based on the volatility of the market.

## Conclusion

The Average True Range (ATR) is a valuable tool for assessing market volatility and can be used in various trading strategies. By understanding how the ATR is calculated and how it reflects price movements, traders can make more informed decisions about their investments.

The Average True Range (ATR) is a technical indicator that measures the volatility of a security’s price by calculating the average of the true range values over a specified period.
