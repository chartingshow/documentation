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
                Users can adjust the settings to expand the forcast length and the machine learning modelling time.
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
            <td>The algorithm finds the pivot highs and pivot lows then calculates the higher highs and lower lows. If price breaks the resistance levels it's an up trend and if price breaks the support level it's a down trend.</td>
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
            <td>Large Numbers</td>
            <td>Core Algorithm</td>
            <td>Seeing <code>458698828817</code> instead of this <code>458.67 B</code> makes it harder on the eyes to work things out. To keep charts future proof, e.g. Bitcoin going over <code>100000</code> or even <code>1000000</code> prices will be written as <code>100 K</code> and <code>1 M</code> etc.</td>
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
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
</table>
