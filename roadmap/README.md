# Roadmap

Below is our roadmap outlining the vision, direction, priorities and progress of all our products and features over time.

The Roadmap is a schedule of events and milestones that forecasts and communicates planned project solution deliverables over a time horizon and how they will be achieved.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Stage</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>AI Forecast</td>
            <td>Trading Algorithm and ML Library</td>
            <td>This algorithm was added to predicted the "<strong>near-term</strong>" price action by default.
                Users can adjust the settings to expand the forcast length, colour, add a label and the machine learning modelling time.
                The results are displayed in the data window and there is a setting to hide it from the chart.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Highlight Weekend Days</td>
            <td>Trading Algorithm</td>
            <td>During the weekend Bitcoin tends to go sideways. When Bitcoin goes sideways the retail traders get restless and Altcoins make some gains.
                It's worth noting when Bitcoin goes up the Altcoins will have a green day and when Bitcoin goes down the Altcoins tend to have a red day.
                Weekends also tend to not any "expected" fundamental news events.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Weekend Median Area Algorithm</td>
            <td>Trading Algorithm</td>
            <td>During the weekend Bitcoin tends to go sideways and drifts to the median area.
                This feature saves traders time be automatically calculating and drawing the area.
                Traders can turn this feature on/off. Algorithm uses fibonacci sequence and pivot points to generate the median area.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Variable Median Area</td>
            <td>Trading Algorithm</td>
            <td>This algorithm was added to allow users to adjust and fine tune the median area. Users can set different moving average values in the settings menu, the default value will be: 20MA.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Fast and Slow Bands</td>
            <td>Trading Algorithm</td>
            <td><p>The Fast and Slow Bands algorithm is momentum based to determine price trends and sideways consolidation periods.</p><p>This is a trend following algorithm that uses a fast band to capture near-term and short-term price swings and a slow band to capture pullback areas and reversal signals for short-term and medium-term price action.</p><p>The Fast and Slow Bands algorithm is connected to the "Moving Average and Custom Filter" algorithm, where traders can setup many different conditions to tailor better price action signals.</p><p>This algorithm is not intended to replace the Trend Analysis Model 1 and 2 algorithms. But instead to work side by side and extend the visual trend results by filling in the gaps left by Trend Analysis Models to better help traders determine the stages of the trend. For example, highlighting pullback areas, confirming reversals, failed low/high swing points, range support and resistances and many more useful features.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Average Price</td>
            <td>Trading Algorithm</td>
            <td>This algorithm calculates the average price by adding the open and close prices of the current bar and divides them by two. It displays the result in the data window, cleaned to assets corresponding number of decimal places. Allows traders to add an average price trendline option via the settings.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Trend Analysis Model 1</td>
            <td>Trading Algorithm and Library</td>
            <td>Trend analysis combining volatility and pivot points algorithm. This algorithm is an external module which can be used to power other modules and algorithms.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Trend Analysis Model 2</td>
            <td>Trading Algorithm and Library</td>
            <td>Trend analysis combining volatility and average true range (ATR) algorithm. This algorithm is an external module which can be used to power other modules and algorithms.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Lower Timeframe (LTF) Trend Analysis</td>
            <td>Trading Algorithm</td>
            <td>Allows traders to analyse lower timeframes trend analysis on the current timeframe chart. Saving the trader having to switch between different timeframe charts or viewing multiple timeframe screens on the same display. This algorithm also uses Trend Analysis Model 1.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Higher Timeframe (HTF) Trend Analysis</td>
            <td>Trading Algorithm</td>
            <td>Allows traders to analyse higher timeframes trend analysis on the current timeframe chart. Saving the trader having to switch between different timeframe charts or viewing multiple timeframe screens on the same display. This algorithm also uses Trend Analysis Model 2.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>High-Low</td>
            <td>Trading Algorithm</td>
            <td><p>The High-Low algorithm finds pivot (swing) highs and pivot (swing) lows and then calculates the higher highs (HH), lower lows (LL), higher lows (HL) and lower highs (LH) swing points.</p><p>The pivot points are calculated using a default setting of 3. A higher setting results in less swing points and a lower setting results in more swing points. The pivot points are more significant and noteworthy the longer the trend. This means if the trader selects a higher setting, the trend could be longer and therefore prove to be more notable.</p><p>The High-Low algorithm is used to determine and anticipate potential price changes and reversals. It also calculates support and resistance trendlines in real-time by analysing the HH, HL, LL and LH swing points. Generally up trends are made up of higher highs (HH) and higher lows (HL), while down trends are made up of lower lows (LL) and lower highs (LH).</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Short-Term Colouring Theme</td>
            <td>Trading Algorithm</td>
            <td>This algorithm uses the Variable Median Area and the Trend Analysis Model with some extra code to update the chart candlesticks.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>High-Low Colouring Theme</td>
            <td>Trading Algorithm</td>
            <td>This algorithm uses the High-Low Algorithm to work out the pivot highs and pivot lows and then adds some extra code to update the chart candlesticks.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>       
        <tr>
            <td>NET Volume</td>
            <td>Trading Algorithm</td>
            <td>Net volume is calculated by subtracting the asset's uptick volume by its downtick volume over a specified period of time. Unlike standard volume, the algorithm differentiates whether the market sentiment is leaning towards bullish or bearish sentiment. The algorithm works out the short, medium and long-term outlooks for NET Volume. For short-term analysis the algorithm alerts the trader to warning signals and for medium to long-term confirmed buy and sell signals are generated.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Bull/Bear Strength</td>
            <td>Trading Algorithm</td>
            <td>This algorithm measures the speed and magnitude of an assets recent price changes by comparing the buying strength on days when prices go up to its selling strength on days when prices go down. The result of this comparison to price action can give traders an idea of how the asset may perform and how strong or weak the buying/selling action is happening. This can also help to indicate possible trend reversals or a corrective pullback in price action. The algorithm works out the short, medium and long-term outlooks for the Bull/Bear Strength. For short-term analysis the algorithm alerts the trader to warning signals and for medium to long-term confirmed buying and selling signals are generated.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/in-development.png" alt="status"></td>
        </tr>
        <tr>
            <td>Polynomial</td>
            <td>Trading Algorithm</td>
            <td><p>A Vandermonde matrix is a matrix in linear algebra with terms of a geometric progression in each row, typically defined as an matrix with entries being the jth power of the number for all zero-based indices. The determinant of a square Vandermonde matrix is called a Vandermonde determinant or Vandermonde polynomial, which is non-zero only if all entries are distinct, making the matrix invertible. This matrix is crucial in polynomial interpolation, where it helps find a unique solution to the interpolation problem by mapping coefficients to values of polynomials through matrix multiplication. The Vandermonde determinant also plays a significant role in various fields like statistics, representation theory, and error correction codes.</p><p>The Vandermonde polynomial, named after Alexandre-Theophile Vandermonde, is an alternating polynomial defined by the product of the differences between pairs of variables. It is a fundamental polynomial in algebra and serves as the determinant of the Vandermonde matrix. The Vandermonde polynomial is essential in generating alternating polynomials and plays a role in defining discriminants and invariant sets of points. It has applications beyond algebra, including in polynomial least squares fitting and Lagrange interpolating polynomials.</p><p>The algorithm combines the Vandermonde matrix, polynomial, regression and outlier detection methods. It's lower and upper range define a prescribed probability quantile in the normal standard deviation distribution and aims to capture more than 95% of the current price action predicted interval.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Current Timeframe (CTF) Trend Support and Resistance Areas</td>
            <td>Trading Algorithm</td>
            <td>This algorithm combines Trend Analysis Models 1 and 2 together to form support and resistance areas on the current timeframe (CTF). Traders can use these areas to find potential "<strong>bounce</strong>" and "<strong>reversal</strong>" price pivots.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Lower Timeframes</td>
            <td>Core Trading Algorithm</td>
            <td>Currently supports the following timeframes: <code>M1, M3, M5, M15, M30, M45, H1, H2, H3, H4, H6, H8, H12, D1, W1, M1, M3, M6</code> and <code>M12</code>. Automatically sets a lower timeframe from the current timeframe being displayed. Currently not setup to process <strong>seconds</strong> or <strong>ranges</strong>. Also <strong>ticker</strong> timeframes are excluded from this algorithms calculations.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Higher Timeframes</td>
            <td>Core Trading Algorithm</td>
            <td>Currently supports the following timeframes: <code>M1, M3, M5, M15, M30, M45, H1, H2, H3, H4, H6, H8, H12, D1, W1, M1, M3, M6</code> and <code>M12</code>. Automatically sets a higher timeframe from the current timeframe being displayed. Currently not setup to process <strong>seconds</strong> or <strong>ranges</strong>. Also <strong>ticker</strong> timeframes are excluded from this algorithms calculations.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Long-Term Timeframes</td>
            <td>Core Trading Algorithm</td>
            <td>Currently supports the following timeframes: <code>M1, M3, M5, M15, M30, M45, H1, H2, H3, H4, H6, H8, H12, D1, W1, M1, M3, M6</code> and <code>M12</code>. Automatically sets a <code>D1</code> timeframe on timeframes lower than <code>D1</code>. For timeframes <code>D1, W1, M1, M3</code> and <code>M6</code> a higher timeframe is selected, e.g. <code>W1</code> becomes <code>M1</code> etc. For M12 timeframe this is set to <code>M12 / Y1</code>. Currently not setup to process <strong>seconds</strong> or <strong>ranges</strong>. Also <strong>ticker</strong> timeframes are excluded from this algorithms calculations.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Time Periods</td>
            <td>Core Trading Algorithm</td>
            <td>Works out the current timeframe period and places it into one of the following groups: <code>Ticks</code>, <code>Seconds</code>, <code>Minutes</code>, <code>Hours</code>, <code>Days</code>, <code>Weeks</code> or <code>Months</code>. Traders should be aware that it currently ignores: <code>Ranges</code>.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Timeframe Label</td>
            <td>Core Trading Algorithm</td>
            <td>This is added to the core code and allows the timeframe to be displayed in the data window for various other algorithms. The various supported timeframes include: <code>seconds</code>, <code>minutes</code>, <code>hours</code>, <code>days</code>, <code>weeks</code> and <code>months</code>.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Timeframe Symbol</td>
            <td>Core Trading Algorithm</td>
            <td>This is added to the core code and allows the timeframe to be displayed in the data window for various other algorithms. The various supported timeframes include: <code>S (for seconds)</code>, <code>M (for minutes)</code>, <code>H (for hours)</code>, <code>D (for days)</code>, <code>W (for weeks)</code> and <code>W (months divided into 4 weeks)</code>. Some examples: <code>M15</code> is 15 minutes, <code>W4</code> is 1 month.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Time Change</td>
            <td>Core Trading Algorithm</td>
            <td>Compares the current source value to its value length bars ago and returns the difference.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Truncate</td>
            <td>Core Trading Algorithm</td>
            <td>Truncate (cut) excess decimal places.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Format Large Numbers</td>
            <td>Core Trading Algorithm</td>
            <td>Seeing <code>458698828817</code> instead of this <code>458.67 B</code> makes it harder on the eyes to work things out. To keep charts future proof, e.g. Bitcoin going over <code>100000</code> or even <code>1000000</code> prices will be written as <code>100 K</code> and <code>1 M</code> etc.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Milliseconds Timestamp</td>
            <td>Core Trading Algorithm</td>
            <td>Find milliseconds for the current timeframe (CTF).</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Big Move Gauge</td>
            <td>Trading Algorithm</td>
            <td><p>The big move gauge algorithm uses the daily calculations of volatility and time-weighted average prices (TWAP) calculated by taking price measurements at 1 minute intervals from the Bitcoin vs the US Dollar price. The <code>fast</code> setting uses a 24-hour H1 timeframe setting and the <code>slow</code> setting uses a rolling 7-day H1 timeframe setting.</p><p>The <code>fast</code> setting shows all the smaller individual moves and traders can look at each move to tell if the bulls or bears are in-control of the price action at that exact period. Traders can also use the <code>fast</code> setting to confirm U-Shape and V-Shape pattern moves. Traders can also use the <code>fast</code> setting to confirm lower-timeframe breakouts. Both the <code>fast</code>and <code>slow</code> modules uses the Trend Analysis Model 2 algorithm with a setting of <code>10.0</code> which is quicker than Trend Analysis Model 1 default setting. Traders can also use the <code>slow</code> setting to confirm higher-timeframe breakouts.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Dominance</td>
            <td>Trading Algorithm</td>
            <td><p>The dominance algorithm is used to measure the relative market strength of Bitcoin vs the Altcoins in the overall cryptocurrency market. This metric is used by crypto traders to understand market trends, spot possible trading opportunities and gauge the performance of altcoins relative to Bitcoin.</p><p>The dominance algorithm is made up of several parts, the first part works out who controls the dominance in the cryptocurrency market, this will either be "Bitcoin" or the "Altcoins".</p><p>The second part compares the daily changes between Bitcoin and the Crypto Market algorithm, which outputs a percentage score.</p><p>The next part checks to see if Bitcoin is making gains or losses and then checks to see if the Altcoins are making gains or losses. If both are making gains the strength is increasing, if one is making a gain and the other one is making a loss strength is going sideways and if both are making a loss then the strength is decreasing.</p><p>The last part works out the strength and classifies the percentage score into four results, these are: "Weak", "Medium", "Strong" and "Extreme" (listed in strength order).</p><p>A consolidation trading period would likely see a "Weak" strength. While "Bitcoin" having a "Strong" strength would drag the cryptocurrencies, in an up trend this would force the Altcoins to have a green day and in a down trend would result in the Altcoins seeing a red day! Another example would be "Altcoins" and "Weak" the trader would expect to see the Altcoins making small gains! While "Altcoins" and "Extreme" the trader would expect to see the Altcoins making large gains! An "Altcoin Season" the trader would expect to see either "Altcoins" and "Strong" / "Altcoins" and "Extreme".</p><p>Therefore, changes in the dominance algorithm can help traders make decisions about how to position themselves in the cryptocurrency market.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Crypto Market Sentiment</td>
            <td>Trading Algorithm</td>
            <td><p>The Crypto Market Sentiment algorithm reflects the collective mood of investors overall regarding the cryptocurrency sector as a whole.</p><p>The mood of the market is affected by crowd psychology and can impact a coin or tokens outlook by the market's direction.</p><p>It involves analysing the collective mood of market participants, revealed through buying and selling activity, identifying bullish or bearish sentiment and navigating market volatility.</p><p>In general, rising prices imply optimism about the market, while declining prices suggest the opposite.</p><p>The Crypto Market Sentiment algorithm is split into three result sections, these deal with the short-term, medium-term and long-term sentiment of the cryptocurrency market as a whole.</p><p>The short-term looks at the 'Intraday' trading period, which is also referred to as 'Day Trading'.</p><p>The medium-term looks at the 'Swing' trading period, a style of trading that attempts to capture the medium-term gains in a cryptoasset (or any financial instrument) over a period of a few days to several weeks.</p><p>The long-term looks at the 'Position' trading period, a common trading strategy where an individual holds a position in a cryptoasset for a long period of time, typically over a number of months or years. In the context of cryptocurrencies, bull and bear markets relate to both the overall state of the market as well as specific markets. Given the daily changes and ongoing volatility of the market, these phrases are used to characterise longer periods of mostly positive or downward movement.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Liquidations</td>
            <td>Trading Algorithm</td>
            <td><p>Crypto liquidations refer to the process of forcibly closing a trader's positions in the cryptocurrency market when their margin account cannot meet the required maintenance level. This occurs to cover margin calls and prevent further losses. Automated procedures like auto-liquidation algorithms are used by brokers to manage these liquidations in real-time.</p><p>The liquidation process typically involves stages such as pre-liquidation, automatic partial liquidation, liquidity support programs, insurance funds and auto-deleveraging to manage risks associated with margin trading. These processes aim to prevent excessive losses and maintain market stability in the face of high volatility in crypto-assets.</p><p>Many websites have crypto liquidation API's where the data is delayed for 1-4 hours (depending upon the exchange). The Liquidations Algorithm displays the liquidations in "real-time" with zero delay meaning it's a <code>leading</code> and not a <code>lagging</code> gauge. Which helps traders to better understand the dynamics of the overall crypto market and the cryptocurrency token they are trading.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Daily Change Percentage</td>
            <td>Trading Algorithm</td>
            <td>The daily percentage change algorithm uses the closing price and calculates the percentage change in a cryptoassets value over a single day of trading. This calculation does not consider circulating supply or other factors that can be easily computed. It's used to frequently analyse fluctuations in cryptocurrency prices or market indexes over time. It helps track price changes in various financial instruments and is crucial for understanding the market dynamics. The calculations are fundamental in assessing the performance and volatility of a digital currency and other assets.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Scheduled Maintenance</td>
            <td>Core Module</td>
            <td>Scheduled maintenance is any repair and service work performed within a set timeframe. It details when given maintenance tasks are performed and by who. Scheduled maintenance may occur at repeating intervals or in response to a work request.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Z-Score</td>
            <td>Trading Algorithm</td>
            <td>A Z-score is a statistical measurement that describes a value's relationship to the mean of a group of values, measured in terms of standard deviations from the mean. If a Z-score is 0, it indicates that the data point's score is identical to the mean score. Positive Z-scores indicate values above the mean, while negative scores indicate values below the mean.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Alerts</td>
            <td>Core Module</td>
            <td>Adds an alerts module to message the trader when one of the trading signals from any of the trading algorithms trigger a various trading condition! The trader can also select the frequency of the alerts in the options settings.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Trading Signals</td>
            <td>Core Module</td>
            <td><p>The trading module processes the various trading algorithms that are currently used by the trader. The results are then displayed in a section of the data window, where the trader can show/hide in the menu options.</p><p>Different trading signals are displayed ranging from buy and sell signals through to informational signals. Actionable trading signals are displayed at the top of the list and informational signals are displayed below them. Each trading signal tells the trader what trading algorithm got called and a suggested trading action.</p><p>There are also complex trading signals merging several different trading algorithms together that get displayed in the data window.</p><p>All the trading signals are joined to the alerts module to be able to send various alerts to the trader such as email, txt, push notifications etc.</p><p>All the trading signals are also joined to the warning signals module, where the trader can highlight any of the trading signals on the trading chart.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Warning Signals</td>
            <td>Core Module</td>
            <td><p>Traders can display any of the various trading algorithms and their corresponding warning signals (which can range from reversal and/or pullback buy and sell signals through to informational signals).</p><p>The purpose of the warning signals module is to allow traders to highlight these warning signals on the chart. The main difference between the warning signal module vs the trading signal module. The warning signal module highlights these warning signals on the chart whereas the trading signals module displays the information in the data window and not on the chart.</p><p>Traders can select any trading algorithm warning signal to display on the chart and use multiple different warning signals on the chart at the same time, allowing traders to generate more in-depth warning signals.</p><p>The default theme uses the following setup: green for buy warning signals, red for sell warning signals, grey for sideways warning signals and yellow for pullback area warning signals.</p><p>Traders can also select different themes and customize their own colours.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Nadaraya-Watson (Kernel Regression) Bands</td>
            <td>Trading Algorithm</td>
            <td><p>The statistical techniques for regression function estimation that were created by G. S. Watson and E. A. Nadaraya in the 1960s are the foundation of the Nadaraya-Watson Envelope algorithm. The Nadaraya-Watson Envelope method and other trading tools were developed as a result of the kernel regression ideas they established, despite the fact that their work was not expressly focused on developing trading algorithms.</p><p>Watson-Nadaraya Regression is a subset of Kernel Regression, a non-parametric technique for determining a dataset's curve of best fit. In contrast to Polynomial or Linear regression, Kernel regression does not make any assumptions about the data's underlying distribution. It employs a kernel function for estimate, which is a weighting function that gives each data point a weight according to how near it is to the current point. The weighted average of the data points is then determined using the obtained weights.</p><p>Traders and programmers have developed trading algorithms that use historical price data to assess market patterns, spot possible reversals, and offer insights into price movements over time by using statistical techniques like kernel regression. The Nadaraya-Watson Envelope algorithm, which provides a non-repainting envelope based on Kernel Smoothing to outline market extremes and support technical analysis in trading strategies, has grown to be a useful tool for traders looking for precise and trustworthy insights into market trends and price dynamics.</p><p>By employing a kernel regression technique to smooth price data, the Nadaraya-Watson Envelope algorithm is a dynamic volatility algorithm that adjusts to shifting market conditions. To give limits for excessive price swings, it computes upper and lower bounds using the Average True Range (ATR) and certain variables.</p><p>By examining the link between price and envelopes, this technique is intended to assist traders in locating possible reversal zones and verifying the trend's direction.</p><p>Because of its broad applicability over a wide range of datasets, the Gaussian Kernel is one of the most widely used Kernel functions and is utilised extensively in many Machine Learning techniques. Imagine a Gaussian kernel on steroids. That's what the Rational Quadratic Kernel is - a bunch of Gaussian kernels with different length scales added together. This gives the user even more flexibility to adjust the indicator to suit their own requirements.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Semaphore Signal Level (SSL)</td>
            <td>Trading Algorithm</td>
            <td><p>The Semaphore Signal Level (SSL) algorithm combines moving averages to provide you with a clear visual signal of near-term price movement dynamic. It's designed to show you all the price action pivot swing points. The algorithm has been modified to connect to the Moving Average and Custom Filter algorithm, to give traders the most amount of options and customizations.</p><p>This algorithm creates an envelope curve that tracks the market price by applying two moving averages, one to the price high and the other to the price low. Trading on the flip technique-where price goes from above the two moving averages to below them and vice versa-is the rationale behind this strategy.</p><p>The algorithm indicates that the direction of price movement is changing or likely to shift (from long to short or from short to long) when the two moving averages meet.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Themes</td>
            <td>Core Module</td>
            <td><p>The themes module has various sections allowing traders to adjust the themes for: candlesticks, trading chart background, trading warning signals, the data window, trading algorithms and highlight weekend sessions. More themes and sections will be added over time!</p><p>The themes module provides various themes used in trading and charting software, such as:</p><h3>Light Theme</h3><p>A theme with a light background colour, typically white or off-white, and dark text colours. This theme is suitable for use in well-lit environments.</p><h3>Dark Theme</h3><p>A theme with a dark background colour, typically black or dark grey, and light text colours. This theme is suitable for use in low-light environments and can reduce eye strain.</p><h3>Coloured Theme</h3><p>A theme that incorporates various colours, often based on a specific colour scheme or palette. These themes can be customized to match branding or personal preferences.</p><h3>High Contrast Theme</h3><p>A theme designed to provide maximum contrast between the background and foreground elements, making it easier to read and distinguish different components. This theme is often used for accessibility purposes.</p><p>The glossary provides a concise explanation of each theme, helping users understand the different visual styles available in charting and trading applications.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Stablecoin Flows</td>
            <td>Trading Algorithm</td>
            <td><p>The algorithm looks at the movements of Stablecoins and calculates the net money flow.</p><p><code>Inflows</code> are defined when Stablecoins deposited into the exchange wallets are more than Stablecoin withdrawal from the exchange wallets, this is a <strong>bearish</strong> trading signal.</p><p><code>Outflows</code>` are defined when Stablecoins withdrawn from the exchange wallets are more than Stablecoin deposited into the exchange wallets, this is a <strong>bullish</strong> trading signal.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>String-Manipulation</td>
            <td>Core Module</td>
            <td><p>This module provides string manipulation features to the core algorithm code. The following list of features are provided:</p><ul><li>Returns the leftmost characters in the string.</li><li>Returns the rightmost characters in the string.</li><li>Returns the substring of the string from a range position with two specified points inclusively.</li><li>Returns the substring of the string to the left of a specified separating character.</li><li>Returns the substring of the string to the right of a specified separating character.</li><li>Returns the position of the first occurrence of a specified separating character in the string, where the first character position is <code>0</code>. Returns <code>-1</code> if the character is not found.</li><li>Replaces a character at a specified position in the string with a defined character or string.</li><li>Returns a formatted string with a rounded value to the symbol's tick precision.</li><li>Removes a particular substring from the end of another string.</li></ul><p><strong>Note for developers:</strong> Using too many string operations will negatively impact the performance of a trading algorithm. If at all possible, restrict the calculation of string manipulation routines in your code to the first or final candlestick bar of the dataset to reduce their influence. This can be accomplished by enclosing code blocks or by utilising the <code>var</code> keyword when declaring variables that hold the outcome of your text manipulations.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
</table>
