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
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Highlight Weekend Days</td>
            <td>Trading Algorithm</td>
            <td>During the weekend Bitcoin tends to go sideways. When Bitcoin goes sideways the retail traders get restless and Altcoins make some gains.
                It's worth noting when Bitcoin goes up the Altcoins will have a green day and when Bitcoin goes down the Altcoins tend to have a red day.
                Weekends also tend to not any "expected" fundamental news events.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Weekend Median Area Algorithm</td>
            <td>Trading Algorithm</td>
            <td>During the weekend Bitcoin tends to go sideways and drifts to the median area.
                This feature saves traders time be automatically calculating and drawing the area.
                Traders can turn this feature on/off. Algorithm uses fibonacci sequence and pivot points to generate the median area.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Variable Median Area</td>
            <td>Trading Algorithm</td>
            <td>This algorithm was added to allow users to adjust and fine tune the median area. Users can set different moving average values in the settings menu, the default value will be: 20MA.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Average Price</td>
            <td>Trading Algorithm</td>
            <td>This algorithm calculates the average price by adding the open and close prices of the current bar and divides them by two. It displays the result in the data window, cleaned to assets corresponding number of decimal places. Allows traders to add an average price trendline option via the settings.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Trend Analysis Model 1</td>
            <td>Trading Algorithm and Library</td>
            <td>Trend analysis combining volatility and pivot points algorithm. This algorithm is an external module which can be used to power other modules and algorithms.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Trend Analysis Model 2</td>
            <td>Trading Algorithm and Library</td>
            <td>Trend analysis combining volatility and average true range (ATR) algorithm. This algorithm is an external module which can be used to power other modules and algorithms.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Lower Timeframe (LTF) Trend Analysis</td>
            <td>Trading Algorithm</td>
            <td>Allows traders to analyse lower timeframes trend analysis on the current timeframe chart. Saving the trader having to switch between different timeframe charts or viewing multiple timeframe screens on the same display. This algorithm also uses Trend Analysis Model 1.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Higher Timeframe (HTF) Trend Analysis</td>
            <td>Trading Algorithm</td>
            <td>Allows traders to analyse higher timeframes trend analysis on the current timeframe chart. Saving the trader having to switch between different timeframe charts or viewing multiple timeframe screens on the same display. This algorithm also uses Trend Analysis Model 2.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>High-Low</td>
            <td>Trading Algorithm</td>
            <td>The algorithm finds the pivot highs and pivot lows then calculates the higher highs and lower lows. If price breaks the resistance levels it's an up trend and if price breaks the support level it's a down trend.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Short-Term Colouring Theme</td>
            <td>Trading Algorithm</td>
            <td>This algorithm uses the Variable Median Area and the Trend Analysis Model with some extra code to update the chart candlesticks.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>High-Low Colouring Theme</td>
            <td>Trading Algorithm</td>
            <td>This algorithm uses the High-Low Algorithm to work out the pivot highs and pivot lows and then adds some extra code to update the chart candlesticks.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>       
        <tr>
            <td>NET Volume</td>
            <td>Trading Algorithm</td>
            <td>Net volume is calculated by subtracting the asset's uptick volume by its downtick volume over a specified period of time. Unlike standard volume, the algorithm differentiates whether the market sentiment is leaning towards bullish or bearish sentiment. The algorithm works out the short, medium and long-term outlooks for NET Volume. For short-term analysis the algorithm alerts the trader to warning signals and for medium to long-term confirmed buy and sell signals are generated.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Bull/Bear Strength</td>
            <td>Trading Algorithm</td>
            <td>This algorithm measures the speed and magnitude of an assets recent price changes by comparing the buying strength on days when prices go up to its selling strength on days when prices go down. The result of this comparison to price action can give traders an idea of how the asset may perform and how strong or weak the buying/selling action is happening. This can also help to indicate possible trend reversals or a corrective pullback in price action. The algorithm works out the short, medium and long-term outlooks for the Bull/Bear Strength. For short-term analysis the algorithm alerts the trader to warning signals and for medium to long-term confirmed buying and selling signals are generated.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/in-development.png" alt="status"></td>
        </tr>
        <tr>
            <td>Polynomial Mean Spread</td>
            <td>Trading Algorithm</td>
            <td>Combines regression and outlier detection methods. It's lower and upper range define a prescribed probability quantile in the normal standard deviation distribution and aims to capture more than 95% of the current price action predicted interval.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/roadmap/in-development.png" alt="status"></td>
        </tr>
        <tr>
            <td>Current Timeframe (CTF) Trend Support and Resistance Areas</td>
            <td>Trading Algorithm</td>
            <td>This algorithm combines Trend Analysis Models 1 and 2 together to form support and resistance areas on the current timeframe (CTF). Traders can use these areas to find potential "<strong>bounce</strong>" and "<strong>reversal</strong>" price pivots.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Lower Timeframes</td>
            <td>Core Trading Algorithm</td>
            <td>Currently supports the following timeframes: <code>M1, M3, M5, M15, M30, M45, H1, H2, H3, H4, H6, H8, H12, D1, W1, M1, M3, M6</code> and <code>M12</code>. Automatically sets a lower timeframe from the current timeframe being displayed. Currently not setup to process <strong>seconds</strong> or <strong>ranges</strong>. Also <strong>ticker</strong> timeframes are excluded from this algorithms calculations.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Higher Timeframes</td>
            <td>Core Trading Algorithm</td>
            <td>Currently supports the following timeframes: <code>M1, M3, M5, M15, M30, M45, H1, H2, H3, H4, H6, H8, H12, D1, W1, M1, M3, M6</code> and <code>M12</code>. Automatically sets a higher timeframe from the current timeframe being displayed. Currently not setup to process <strong>seconds</strong> or <strong>ranges</strong>. Also <strong>ticker</strong> timeframes are excluded from this algorithms calculations.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Long-Term Timeframes</td>
            <td>Core Trading Algorithm</td>
            <td>Currently supports the following timeframes: <code>M1, M3, M5, M15, M30, M45, H1, H2, H3, H4, H6, H8, H12, D1, W1, M1, M3, M6</code> and <code>M12</code>. Automatically sets a <code>D1</code> timeframe on timeframes lower than <code>D1</code>. For timeframes <code>D1, W1, M1, M3</code> and <code>M6</code> a higher timeframe is selected, e.g. <code>W1</code> becomes <code>M1</code> etc. For M12 timeframe this is set to <code>M12 / Y1</code>. Currently not setup to process <strong>seconds</strong> or <strong>ranges</strong>. Also <strong>ticker</strong> timeframes are excluded from this algorithms calculations.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Tick Formatter</td>
            <td>Core Trading Algorithm</td>
            <td>Produce a string format usable to restrict precision to ticks.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Truncate</td>
            <td>Core Trading Algorithm</td>
            <td>Truncate (cut) excess decimal places.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Format Large Numbers</td>
            <td>Core Trading Algorithm</td>
            <td>Seeing <code>458698828817</code> instead of this <code>458.67 B</code> makes it harder on the eyes to work things out. To keep charts future proof, e.g. Bitcoin going over <code>100000</code> or even <code>1000000</code> prices will be written as <code>100 K</code> and <code>1 M</code> etc.</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Milliseconds Timestamp</td>
            <td>Core Trading Algorithm</td>
            <td>Find milliseconds for the current timeframe (CTF).</td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Big Move Gauge</td>
            <td>Trading Algorithm</td>
            <td><p>The big move gauge algorithm uses the daily calculations of volatility and time-weighted average prices (TWAP) calculated by taking price measurements at 1 minute intervals from the Bitcoin vs the US Dollar price. The <code>fast</code> setting uses a 24-hour H1 timeframe setting and the <code>slow</code> setting uses a rolling 7-day H4 timeframe setting.</p><p>The <code>fast</code> setting shows all the smaller individual moves and traders can look at each move to tell if the bulls or bears are in-control of the price action at that exact period. Traders can also use the <code>fast</code> setting to confirm U-Shape and V-Shape pattern moves. Traders can also use the <code>fast</code> setting to confirm lower-timeframe breakouts. The <code>fast</code> module uses the Trend Analysis Model 2 algorithm with a setting of <code>10.0</code> which is quicker than Trend Analysis Model 1 default setting.</p><p>The <code>slow</code> setting shows all the longer trend moves and traders can use this to confirm breakouts and when the momentum for the trend is over. Traders can also use the <code>slow</code> setting to confirm higher-timeframe breakouts. The <code>slow</code> module uses the Trend Analysis Model 1 algorithm with the default settings.</p></td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Dominance</td>
            <td>Trading Algorithm</td>
            <td><p>The dominance algorithm is used to measure the relative market strength of Bitcoin vs the Altcoins in the overall cryptocurrency market. This metric is used by crypto traders to understand market trends, spot possible trading opportunities and gauge the performance of altcoins relative to Bitcoin.</p><p>The dominance algorithm is made up of several parts, the first part works out who controls the dominance in the cryptocurrency market, this will either be "Bitcoin" or the "Altcoins".</p><p>The second part compares the daily changes between Bitcoin and the Crypto Market algorithm, which outputs a percentage score.</p><p>The next part checks to see if Bitcoin is making gains or losses and then checks to see if the Altcoins are making gains or losses. If both are making gains the strength is increasing, if one is making a gain and the other one is making a loss strength is going sideways and if both are making a loss then the strength is decreasing.</p><p>The last part works out the strength and classifies the percentage score into four results, these are: "Weak", "Medium", "Strong" and "Extreme" (listed in strength order).</p><p>A consolidation trading period would likely see a "Weak" strength. While "Bitcoin" having a "Strong" strength would drag the cryptocurrencies, in an up trend this would force the Altcoins to have a green day and in a down trend would result in the Altcoins seeing a red day! Another example would be "Altcoins" and "Weak" the trader would expect to see the Altcoins making small gains! While "Altcoins" and "Extreme" the trader would expect to see the Altcoins making large gains! An "Altcoin Season" the trader would expect to see either "Altcoins" and "Strong" / "Altcoins" and "Extreme".</p><p>Therefore, changes in the dominance algorithm can help traders make decisions about how to position themselves in the cryptocurrency market.</p></td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>Crypto Market Sentiment</td>
            <td>Trading Algorithm</td>
            <td><p>The Crypto Market Sentiment algorithm reflects the collective mood of investors overall regarding the cryptocurrency sector as a whole.</p><p>The mood of the market is affected by crowd psychology and can impact a coin or tokens outlook by the market's direction.</p><p>It involves analysing the collective mood of market participants, revealed through buying and selling activity, identifying bullish or bearish sentiment and navigating market volatility.</p><p>In general, rising prices imply optimism about the market, while declining prices suggest the opposite.</p><p>The Crypto Market Sentiment algorithm is split into three result sections, these deal with the short-term, medium-term and long-term sentiment of the cryptocurrency market as a whole.</p><p>The short-term looks at the 'Intraday' trading period, which is also referred to as 'Day Trading'.</p><p>The medium-term looks at the 'Swing' trading period, a style of trading that attempts to capture the medium-term gains in a cryptoasset (or any financial instrument) over a period of a few days to several weeks.</p><p>The long-term looks at the 'Position' trading period, a common trading strategy where an individual holds a position in a cryptoasset for a long period of time, typically over a number of months or years. In the context of cryptocurrencies, bull and bear markets relate to both the overall state of the market as well as specific markets. Given the daily changes and ongoing volatility of the market, these phrases are used to characterise longer periods of mostly positive or downward movement.</p></td>
            <td><img src="https://github.com/chartingshow/Documentation/blob/master/assets/images/roadmap/launched.png" alt="status"></td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
</table>
