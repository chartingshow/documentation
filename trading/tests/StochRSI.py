//@version=6
indicator(title = 'Stochastic RSI (StochRSI)', shorttitle = 'StochRSI')

// Define input parameters
smoothK = input.int(3, 'K', minval = 1)
smoothD = input.int(3, 'D', minval = 1)
lengthRSI = input.int(14, 'RSI Length', minval = 1)
lengthStoch = input.int(14, 'Stochastic Length', minval = 1)
src = input(close, title = 'Source')

// Calculate Stochastic RSI and its components
rsi1 = ta.rsi(src, lengthRSI)
k = ta.sma(ta.stoch(rsi1, rsi1, rsi1, lengthStoch), smoothK)
d = ta.sma(k, smoothD)

// Define overbought and oversold levels
overbought = hline(80, title = 'Overbought', linestyle = hline.style_dashed)
oversold = hline(20, title = 'Oversold', linestyle = hline.style_dashed)
fill(overbought, oversold, #b2b5be1a, title = 'Background')

// Add a green line when smoothK crosses above smoothD in overbought area
crossoverUp = ta.crossover(k, d) and k < 20
plot(crossoverUp ? k : na, style = plot.style_linebr, color = color.green, linewidth = 10)

// Add a red line when smoothD crosses above smoothK in oversold area
crossunderDown = ta.crossunder(k, d) and d > 80
plot(crossunderDown ? d : na, style = plot.style_linebr, color = color.red, linewidth = 10)

// Plot the Stochastic RSI components
plot(k, title = '%K', color = color.new(#98f321, 2))
plot(d, title = '%D', color = color.new(#f16542, 0))

// Alerts
alertcondition(crossoverUp , 'Overbought', 'StochRSI Overbought Crossover')
alertcondition(crossunderDown , 'OverSold', 'StochRSI OverSold Crossover')
