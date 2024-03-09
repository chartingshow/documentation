# Trading Algorithms

Below shows all the current trading algorithms development stages and let's users know about any proposals, updates, development or deprecations.

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
            <td>EMA Ribbon</td>
            <td>Algorithm</td>
            <td>This algorithm was dropped due to it's large amount of false positives from price action spiking above
                the highest moving average. Price crossing the moving average ribbons is an unreliable indicator of a
                price reversal!</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>AI Forecast</td>
            <td>Algorithm and ML Library</td>
            <td>This algorithm was added to predicted the "<strong>near-term</strong>" price action by default.
                Users can adjust the settings to expand the forcast length, colour, add a label and the machine learning modelling time.
                The results are displayed in the data window and there is a setting to hide it from the chart.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Highlight Weekend Days</td>
            <td>Algorithm</td>
            <td>During the weekend Bitcoin tends to go sideways. When Bitcoin goes sideways the retail traders get restless and Altcoins make some gains.
                It's worth noting when Bitcoin goes up the Altcoins will have a green day and when Bitcoin goes down the Altcoins tend to have a red day.
                Weekends also tend to not any "expected" fundamental news events.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Weekend Median Area Algorithm</td>
            <td>Algorithm</td>
            <td>During the weekend Bitcoin tends to go sideways and drifts to the median area.
                This feature saves traders time be automatically calculating and drawing the area.
                Traders can turn this feature on/off. Algorithm uses fibonacci sequence and pivot points to generate the median area.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>20MA Fixed Median Area</td>
            <td>Algorithm</td>
            <td>This algorithm was dropped due to removing the 20MA and 30MA "fixed" median areas algorithms and going to be replaced by a variable median area algorithm with a default set at 20MA.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>30MA Fixed Median Area</td>
            <td>Algorithm</td>
            <td>This algorithm was dropped due to removing the 20MA and 30MA "fixed" median areas algorithms and going to be replaced by a variable median area algorithm with a default set at 20MA.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>Variable Median Area</td>
            <td>Algorithm</td>
            <td>This algorithm was added to allow users to adjust and fine tune the median area. Users can set different moving average values in the settings menu, the default value will be: 20MA.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Average Price</td>
            <td>Algorithm</td>
            <td>This algorithm calculates the average price by adding the open and close prices of the current bar and divides them by two. It displays the result in the data window, cleaned to assets corresponding number of decimal places. Allows traders to add an average price trendline option via the settings.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Trend Analysis Model 1</td>
            <td>Algorithm and Library</td>
            <td>Trend analysis combining volatility and pivot points algorithm. This algorithm is an external module which can be used to power other modules and algorithms.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Trend Analysis Model 2</td>
            <td>Algorithm and Library</td>
            <td>Trend analysis combining volatility and average true range (ATR) algorithm. This algorithm is an external module which can be used to power other modules and algorithms.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Lower Timeframe (LTF) Trend Analysis</td>
            <td>Algorithm</td>
            <td>Allows traders to analyse lower timeframes trend analysis on the current timeframe chart. Saving the trader having to switch between different timeframe charts or viewing multiple timeframe screens on the same display. This algorithm also uses Trend Analysis Model 1.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Higher Timeframe (HTF) Trend Analysis</td>
            <td>Algorithm</td>
            <td>Allows traders to analyse higher timeframes trend analysis on the current timeframe chart. Saving the trader having to switch between different timeframe charts or viewing multiple timeframe screens on the same display. This algorithm also uses Trend Analysis Model 2.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>High-Low</td>
            <td>Algorithm</td>
            <td><p>The High-Low algorithm finds pivot (swing) highs and pivot (swing) lows and then calculates the higher highs (HH), lower lows (LL), higher lows (HL) and lower highs (LH) swing points.</p><p>The pivot points are calculated using a default setting of 3. A higher setting results in less swing points and a lower setting results in more swing points. The pivot points are more significant and noteworthy the longer the trend. This means if the trader selects a higher setting, the trend could be longer and therefore prove to be more notable.</p><p>The High-Low algorithm is used to determine and anticipate potential price changes and reversals. It also calculates support and resistance trendlines in real-time by analysing the HH, HL, LL and LH swing points. Generally up trends are made up of higher highs (HH) and higher lows (HL), while down trends are made up of lower lows (LL) and lower highs (LH).</p></td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Short-Term Colouring Theme</td>
            <td>Algorithm</td>
            <td>This algorithm uses the Variable Median Area and the Trend Analysis Model with some extra code to update the chart candlesticks.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>High-Low Colouring Theme</td>
            <td>Algorithm</td>
            <td>This algorithm uses the High-Low Algorithm to work out the pivot highs and pivot lows and then adds some extra code to update the chart candlesticks.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>NET Volume</td>
            <td>Algorithm</td>
            <td>Net volume is calculated by subtracting the asset's uptick volume by its downtick volume over a specified period of time. Unlike standard volume, the algorithm differentiates whether the market sentiment is leaning towards bullish or bearish sentiment. The algorithm works out the short, medium and long-term outlooks for NET Volume. For short-term analysis the algorithm alerts the trader to warning signals and for medium to long-term confirmed buy and sell signals are generated.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Ichimoku Cloud Median Area</td>
            <td>Algorithm</td>
            <td>This algorithm was dropped due to giving poor results and traders are advised to use the Trend Analysis Models 1 and 2 instead giving superior results.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>Current Timeframe (CTF) Trend Support and Resistance Areas</td>
            <td>Algorithm</td>
            <td>This algorithm combines Trend Analysis Models 1 and 2 together to form support and resistance areas on the current timeframe (CTF). Traders can use these areas to find potential "<strong>bounce</strong>" and "<strong>reversal</strong>" price pivots.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Lower Timeframes</td>
            <td>Core Algorithm</td>
            <td>Currently supports the following timeframes: <code>M1, M3, M5, M15, M30, M45, H1, H2, H3, H4, H6, H8, H12, D1, W1, M1, M3, M6</code> and <code>M12</code>. Automatically sets a lower timeframe from the current timeframe being displayed. Currently not setup to process <strong>seconds</strong> or <strong>ranges</strong>. Also <strong>ticker</strong> timeframes are excluded from this algorithms calculations.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Higher Timeframes</td>
            <td>Core Algorithm</td>
            <td>Currently supports the following timeframes: <code>M1, M3, M5, M15, M30, M45, H1, H2, H3, H4, H6, H8, H12, D1, W1, M1, M3, M6</code> and <code>M12</code>. Automatically sets a higher timeframe from the current timeframe being displayed. Currently not setup to process <strong>seconds</strong> or <strong>ranges</strong>. Also <strong>ticker</strong> timeframes are excluded from this algorithms calculations.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Long-Term Timeframes</td>
            <td>Core Algorithm</td>
            <td>Currently supports the following timeframes: <code>M1, M3, M5, M15, M30, M45, H1, H2, H3, H4, H6, H8, H12, D1, W1, M1, M3, M6</code> and <code>M12</code>. Automatically sets a <code>D1</code> timeframe on timeframes lower than <code>D1</code>. For timeframes <code>D1, W1, M1, M3</code> and <code>M6</code> a higher timeframe is selected, e.g. <code>W1</code> becomes <code>M1</code> etc. For M12 timeframe this is set to <code>M12 / Y1</code>. Currently not setup to process <strong>seconds</strong> or <strong>ranges</strong>. Also <strong>ticker</strong> timeframes are excluded from this algorithms calculations.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Time Periods</td>
            <td>Core Algorithm</td>
            <td>Works out the current timeframe period and places it into one of the following groups: <code>Ticks</code>, <code>Seconds</code>, <code>Minutes</code>, <code>Hours</code>, <code>Days</code>, <code>Weeks</code> or <code>Months</code>. Traders should be aware that it currently ignores: <code>Ranges</code>.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Tick Formatter</td>
            <td>Core Algorithm</td>
            <td>Produce a string format usable to restrict precision to ticks.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Truncate</td>
            <td>Core Algorithm</td>
            <td>Truncate (cut) excess decimal places.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Format Large Numbers</td>
            <td>Core Algorithm</td>
            <td>Seeing <code>458698828817</code> instead of this <code>458.67 B</code> makes it harder on the eyes to work things out. To keep charts future proof, e.g. Bitcoin going over <code>100000</code> or even <code>1000000</code> prices will be written as <code>100 K</code> and <code>1 M</code> etc.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Milliseconds Timestamp</td>
            <td>Core Algorithm</td>
            <td>Find milliseconds for the current timeframe (CTF).</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Big Move Gauge</td>
            <td>Algorithm</td>
            <td><p>The big move gauge algorithm uses the daily calculations of volatility and time-weighted average prices (TWAP) calculated by taking price measurements at 1 minute intervals from the Bitcoin vs the US Dollar price. The <code>fast</code> setting uses a 24-hour H1 timeframe setting and the <code>slow</code> setting uses a rolling 7-day H1 timeframe setting.</p><p>The <code>fast</code> setting shows all the smaller individual moves and traders can look at each move to tell if the bulls or bears are in-control of the price action at that exact period. Traders can also use the <code>fast</code> setting to confirm U-Shape and V-Shape pattern moves. Traders can also use the <code>fast</code> setting to confirm lower-timeframe breakouts. Both the <code>fast</code>and <code>slow</code> modules uses the Trend Analysis Model 2 algorithm with a setting of <code>10.0</code> which is quicker than Trend Analysis Model 1 default setting. Traders can also use the <code>slow</code> setting to confirm higher-timeframe breakouts.</p></td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Dominance</td>
            <td>Algorithm</td>
            <td><p>The dominance algorithm is used to measure the relative market strength of Bitcoin vs the Altcoins in the overall cryptocurrency market. This metric is used by crypto traders to understand market trends, spot possible trading opportunities and gauge the performance of altcoins relative to Bitcoin.</p><p>The dominance algorithm is made up of several parts, the first part works out who controls the dominance in the cryptocurrency market, this will either be "Bitcoin" or the "Altcoins".</p><p>The second part compares the daily changes between Bitcoin and the Crypto Market algorithm, which outputs a percentage score.</p><p>The next part checks to see if Bitcoin is making gains or losses and then checks to see if the Altcoins are making gains or losses. If both are making gains the strength is increasing, if one is making a gain and the other one is making a loss strength is going sideways and if both are making a loss then the strength is decreasing.</p><p>The last part works out the strength and classifies the percentage score into four results, these are: "Weak", "Medium", "Strong" and "Extreme" (listed in strength order).</p><p>A consolidation trading period would likely see a "Weak" strength. While "Bitcoin" having a "Strong" strength would drag the cryptocurrencies, in an up trend this would force the Altcoins to have a green day and in a down trend would result in the Altcoins seeing a red day! Another example would be "Altcoins" and "Weak" the trader would expect to see the Altcoins making small gains! While "Altcoins" and "Extreme" the trader would expect to see the Altcoins making large gains! An "Altcoin Season" the trader would expect to see either "Altcoins" and "Strong" / "Altcoins" and "Extreme".</p><p>Therefore, changes in the dominance algorithm can help traders make decisions about how to position themselves in the cryptocurrency market.</p></td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Crypto Market Sentiment</td>
            <td>Algorithm</td>
            <td><p>The Crypto Market Sentiment algorithm reflects the collective mood of investors overall regarding the cryptocurrency sector as a whole.</p><p>The mood of the market is affected by crowd psychology and can impact a coin or tokens outlook by the market's direction.</p><p>It involves analysing the collective mood of market participants, revealed through buying and selling activity, identifying bullish or bearish sentiment and navigating market volatility.</p><p>In general, rising prices imply optimism about the market, while declining prices suggest the opposite.</p><p>The Crypto Market Sentiment algorithm is split into three result sections, these deal with the short-term, medium-term and long-term sentiment of the cryptocurrency market as a whole.</p><p>The short-term looks at the 'Intraday' trading period, which is also referred to as 'Day Trading'.</p><p>The medium-term looks at the 'Swing' trading period, a style of trading that attempts to capture the medium-term gains in a cryptoasset (or any financial instrument) over a period of a few days to several weeks.</p><p>The long-term looks at the 'Position' trading period, a common trading strategy where an individual holds a position in a cryptoasset for a long period of time, typically over a number of months or years. In the context of cryptocurrencies, bull and bear markets relate to both the overall state of the market as well as specific markets. Given the daily changes and ongoing volatility of the market, these phrases are used to characterise longer periods of mostly positive or downward movement.</p></td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Liquidations</td>
            <td>Algorithm</td>
            <td><p>Crypto liquidations refer to the process of forcibly closing a trader's positions in the cryptocurrency market when their margin account cannot meet the required maintenance level. This occurs to cover margin calls and prevent further losses. Automated procedures like auto-liquidation algorithms are used by brokers to manage these liquidations in real-time.</p><p>The liquidation process typically involves stages such as pre-liquidation, automatic partial liquidation, liquidity support programs, insurance funds and auto-deleveraging to manage risks associated with margin trading. These processes aim to prevent excessive losses and maintain market stability in the face of high volatility in crypto-assets.</p><p>Many websites have crypto liquidation API's where the data is delayed for 1-4 hours (depending upon the exchange). The Liquidations Algorithm displays the liquidations in "real-time" with zero delay meaning it's a <code>leading</code> and not a <code>lagging</code> gauge. Which helps traders to better understand the dynamics of the overall crypto market and the cryptocurrency token they are trading.</p></td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Daily Change Percentage</td>
            <td>Algorithm</td>
            <td>The daily percentage change algorithm uses the closing price and calculates the percentage change in a cryptoassets value over a single day of trading. This calculation does not consider circulating supply or other factors that can be easily computed. It's used to frequently analyse fluctuations in cryptocurrency prices or market indexes over time. It helps track price changes in various financial instruments and is crucial for understanding the market dynamics. The calculations are fundamental in assessing the performance and volatility of a digital currency and other assets.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Divergence From Mean</td>
            <td>Algorithm</td>
            <td><p>This algorithm was dropped due to producing conflicting results for traders. For example, during a healthy up trend, price action will often be quite far away from the medium-term mean. The algorithm signalled a "high risk" trade when far away from the medium-term mean and suggested to traders to wait for a "low risk" trade instead.</p><p>However, even during a "pullback" period in an up trend the algorithm still signalled this as a "high risk" trade due to the large distance between price action and the medium-term mean.</p><p><strong>This resulted in many trading opportunities being missed by traders; due to these conflicting results and so this algorithm has been removed. Traders are advised to use the <code>Z-Score</code> algorithm instead.</strong></p></td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>TVL Buy Zone</td>
            <td>Algorithm</td>
            <td><p>The Total Value Locked (TVL) is usually manipulated on individual assets. By looking at the TVL for the whole cryptocurrency market, this reduces the noise and manipulation. The TVL Buy Zone shows 4 different labels, these are: 'Prepare To Buy', 'Buy Zone', 'Too Late To Buy' and 'Dumb Money'.</p><p>Prepare To Buy = is when extreme bearish market conditions makes the TVL drop down due to fear and signals that a trader should get ready for the buy zone label coming next.</p><p>Buy Zone = is when extreme bearish market conditions makes the TVL drop and signals to a trader to lookout for a possible buy trade, a trader could place a buy trigger combining the Trend Analysis Model 1 algorithm data. It's designed to help the trader buy the fear and not the greed.</p><p>Too Late To Buy = signals to the trader that the best time to buy is now over and price should've already triggered a buy trade and not to FOMO into the market.</p><p>Dumb Money = signals to the trader not to FOMO into the market and the need to wait for a better time to get into the market.</p><p>Note: The api data is displayed at the 'End of the Day' meaning it's not in real-time and shows the previous days data, this means there is a large delay!</p><p><strong>Due to this algorithm being a lagging indicator and giving a large delay (between 1-2 days). It has been deprecated and replaced by a new and improved algorithm system giving a zero delay and acting as a leading indicator. Traders are advised to use the <code>Medium-Term Sentiment</code> and <code>Medium-Term Polynomial</code> algorithms instead.</strong></p></td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>Z-Score</td>
            <td>Algorithm</td>
            <td>A Z-score is a statistical measurement that describes a value's relationship to the mean of a group of values, measured in terms of standard deviations from the mean. If a Z-score is 0, it indicates that the data point's score is identical to the mean score. Positive Z-scores indicate values above the mean, while negative scores indicate values below the mean.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/in-development.jpg" alt="in development"></td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
</table>
