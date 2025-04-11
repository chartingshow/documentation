# Trading Algorithms and Modules

Below shows all the current trading algorithms and modules development stages and let's users know about any proposals, updates, development or deprecations.

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
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>AI Forecast</td>
            <td>Algorithm and ML Library</td>
            <td>This algorithm was added to predicted the "<strong>near-term</strong>" price action by default.
                Users can adjust the settings to expand the forcast length, colour, add a label and the machine learning modelling time.
                The results are displayed in the data window and there is a setting to hide it from the chart.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Highlight Weekend Days</td>
            <td>Algorithm</td>
            <td>During the weekend Bitcoin tends to go sideways. When Bitcoin goes sideways the retail traders get restless and Altcoins make some gains.
                It's worth noting when Bitcoin goes up the Altcoins will have a green day and when Bitcoin goes down the Altcoins tend to have a red day.
                Weekends also tend to not any "expected" fundamental news events.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Weekend Median Area Algorithm</td>
            <td>Algorithm</td>
            <td>During the weekend Bitcoin tends to go sideways and drifts to the median area.
                This feature saves traders time be automatically calculating and drawing the area.
                Traders can turn this feature on/off. Algorithm uses fibonacci sequence and pivot points to generate the median area.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>20MA Fixed Median Area</td>
            <td>Algorithm</td>
            <td><p>This algorithm was dropped due to removing the 20MA and 30MA "fixed" median areas algorithms and going to be replaced by a variable median area algorithm with a default set at 20MA.</p><p><strong>This algorithm was replaced with the "Variable Median Area" algorithm, the reason was to move away from a "fixed" setting and move to an "adjustable" setting allowing traders more scope and options.</strong></p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>30MA Fixed Median Area</td>
            <td>Algorithm</td>
            <td><p>This algorithm was dropped due to removing the 20MA and 30MA "fixed" median areas algorithms and going to be replaced by a variable median area algorithm with a default set at 20MA.</p><p><strong>This algorithm was replaced with the "Variable Median Area" algorithm, the reason was to move away from a "fixed" setting and move to an "adjustable" setting allowing traders more scope and options.</strong></p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>Variable Median Area</td>
            <td>Algorithm</td>
            <td><p>This algorithm was added to allow users to adjust and fine tune the median area. Users can set different moving average values in the settings menu, the default value will be: 20MA.</p><p><strong>This algorithm was replaced with the "Median and Pullback Areas" algorithm. The "Variable Median Area" algorithm closely matching the Fast Band settings. This new algorithm connects to many new moving average and filters modules, giving traders more scope and options.</strong></p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>Median and Pullback Areas</td>
            <td>Algorithm</td>
            <td><p>The Median and Pullback Areas algorithms are momentum based to determine price trends and sideways consolidation periods.</p><p>They are trend following algorithms that uses a median area to capture near-term and short-term price swings and a pullback area to capture pullbacks and reversal signals for short-term and medium-term price action.</p><p>The Median and Pullback Areas algorithms are connected to the "Moving Average and Custom Filter" trading module, where traders can setup many different conditions to tailor better price action signals.</p><p>These algorithms are not intended to replace the Trend Analysis Model 1 and 2 algorithms. But instead intended to work side by side and extend the visual trend results by filling in the gaps left by Trend Analysis Models to better help traders determine the stages of the trend. For example, highlighting pullback areas, confirming reversals, failed low/high swing points, range support and resistances and many more useful features.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Average Price</td>
            <td>Algorithm</td>
            <td>This algorithm calculates the average price by adding the open and close prices of the current bar and divides them by two. It displays the result in the data window, cleaned to assets corresponding number of decimal places. Allows traders to add an average price trendline option via the settings.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Trend Analysis Model 1</td>
            <td>Algorithm and Library</td>
            <td>Trend analysis combining volatility and pivot points algorithm. This algorithm is an external module which can be used to power other modules and algorithms.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Trend Analysis Model 2</td>
            <td>Algorithm and Library</td>
            <td>Trend analysis combining volatility and average true range (ATR) algorithm. This algorithm is an external module which can be used to power other modules and algorithms.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Lower Timeframe (LTF) Trend Analysis</td>
            <td>Algorithm</td>
            <td>Allows traders to analyse lower timeframes trend analysis on the current timeframe chart. Saving the trader having to switch between different timeframe charts or viewing multiple timeframe screens on the same display. This algorithm also uses Trend Analysis Model 1.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Higher Timeframe (HTF) Trend Analysis</td>
            <td>Algorithm</td>
            <td>Allows traders to analyse higher timeframes trend analysis on the current timeframe chart. Saving the trader having to switch between different timeframe charts or viewing multiple timeframe screens on the same display. This algorithm also uses Trend Analysis Model 2.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>LTF + HTF Trend Analysis <code>auto</code> and <code>manual</code> timeframe settings</td>
            <td>Algorithm</td>
            <td>Allows the trader an option to override the auto timeframe setting for lower and higher timeframes on the chart's current timeframe. For example, if the chart's current timeframe is <code>H2</code>, the auto feature will select <code>H1</code> as the lower timeframe. However, the trader can now override this and set the lower timeframe setting to <code>M30</code> if desired.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>High-Low</td>
            <td>Algorithm</td>
            <td><p>The High-Low algorithm finds pivot (swing) highs and pivot (swing) lows and then calculates the higher highs (HH), lower lows (LL), higher lows (HL) and lower highs (LH) swing points.</p><p>The pivot points are calculated using a default setting of 3. A higher setting results in less swing points and a lower setting results in more swing points. The pivot points are more significant and noteworthy the longer the trend. This means if the trader selects a higher setting, the trend could be longer and therefore prove to be more notable.</p><p>The High-Low algorithm is used to determine and anticipate potential price changes and reversals. It also calculates support and resistance trendlines in real-time by analysing the HH, HL, LL and LH swing points. Generally up trends are made up of higher highs (HH) and higher lows (HL), while down trends are made up of lower lows (LL) and lower highs (LH).</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Short-Term Colouring Theme</td>
            <td>Algorithm</td>
            <td>This algorithm uses the Variable Median Area and the Trend Analysis Model with some extra code to update the chart candlesticks.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>High-Low Colouring Theme</td>
            <td>Algorithm</td>
            <td>This algorithm uses the High-Low Algorithm to work out the pivot highs and pivot lows and then adds some extra code to update the chart candlesticks.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>NET Volume</td>
            <td>Algorithm</td>
            <td>Net volume is calculated by subtracting the asset's uptick volume by its downtick volume over a specified period of time. Unlike standard volume, the algorithm differentiates whether the market sentiment is leaning towards bullish or bearish sentiment. The algorithm works out the short, medium and long-term outlooks for NET Volume. For short-term analysis the algorithm alerts the trader to warning signals and for medium to long-term confirmed buy and sell signals are generated.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Bull/Bear Strength</td>
            <td>Algorithm</td>
            <td>This algorithm measures the speed and magnitude of an assets recent price changes by comparing the buying strength on days when prices go up to its selling strength on days when prices go down. The result of this comparison to price action can give traders an idea of how the asset may perform and how strong or weak the buying/selling action is happening. This can also help to indicate possible trend reversals or a corrective pullback in price action. The algorithm works out the short, medium and long-term outlooks for the Bull/Bear Strength. For short-term analysis the algorithm alerts the trader to warning signals and for medium to long-term confirmed buying and selling signals are generated.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/in-development.jpg" alt="in development"></td>
        </tr>
        <tr>
            <td>Polynomial</td>
            <td>Algorithm</td>
            <td><p>A Vandermonde matrix is a matrix in linear algebra with terms of a geometric progression in each row, typically defined as an matrix with entries being the jth power of the number for all zero-based indices. The determinant of a square Vandermonde matrix is called a Vandermonde determinant or Vandermonde polynomial, which is non-zero only if all entries are distinct, making the matrix invertible. This matrix is crucial in polynomial interpolation, where it helps find a unique solution to the interpolation problem by mapping coefficients to values of polynomials through matrix multiplication. The Vandermonde determinant also plays a significant role in various fields like statistics, representation theory, and error correction codes.</p><p>The Vandermonde polynomial, named after Alexandre-Theophile Vandermonde, is an alternating polynomial defined by the product of the differences between pairs of variables. It is a fundamental polynomial in algebra and serves as the determinant of the Vandermonde matrix. The Vandermonde polynomial is essential in generating alternating polynomials and plays a role in defining discriminants and invariant sets of points. It has applications beyond algebra, including in polynomial least squares fitting and Lagrange interpolating polynomials.</p><p>The algorithm combines the Vandermonde matrix, polynomial, regression and outlier detection methods. It's lower and upper range define a prescribed probability quantile in the normal standard deviation distribution and aims to capture more than 95% of the current price action predicted interval.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Ichimoku Cloud Median Area</td>
            <td>Algorithm</td>
            <td>This algorithm was dropped due to giving poor results and traders are advised to use the Trend Analysis Models 1 and 2 instead giving superior results.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>Current Timeframe (CTF) Trend Support and Resistance Areas</td>
            <td>Algorithm</td>
            <td>This algorithm combines Trend Analysis Models 1 and 2 together to form support and resistance areas on the current timeframe (CTF). Traders can use these areas to find potential "<strong>bounce</strong>" and "<strong>reversal</strong>" price pivots.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Lower Timeframes</td>
            <td>Core Algorithm</td>
            <td>Currently supports the following timeframes: <code>M1, M3, M5, M15, M30, M45, H1, H2, H3, H4, H6, H8, H12, D1, W1, M1, M3, M6</code> and <code>M12</code>. Automatically sets a lower timeframe from the current timeframe being displayed. Currently not setup to process <strong>seconds</strong> or <strong>ranges</strong>. Also <strong>ticker</strong> timeframes are excluded from this algorithms calculations.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Higher Timeframes</td>
            <td>Core Algorithm</td>
            <td>Currently supports the following timeframes: <code>M1, M3, M5, M15, M30, M45, H1, H2, H3, H4, H6, H8, H12, D1, W1, M1, M3, M6</code> and <code>M12</code>. Automatically sets a higher timeframe from the current timeframe being displayed. Currently not setup to process <strong>seconds</strong> or <strong>ranges</strong>. Also <strong>ticker</strong> timeframes are excluded from this algorithms calculations.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Long-Term Timeframes</td>
            <td>Core Algorithm</td>
            <td>Currently supports the following timeframes: <code>M1, M3, M5, M15, M30, M45, H1, H2, H3, H4, H6, H8, H12, D1, W1, M1, M3, M6</code> and <code>M12</code>. Automatically sets a <code>D1</code> timeframe on timeframes lower than <code>D1</code>. For timeframes <code>D1, W1, M1, M3</code> and <code>M6</code> a higher timeframe is selected, e.g. <code>W1</code> becomes <code>M1</code> etc. For M12 timeframe this is set to <code>M12 / Y1</code>. Currently not setup to process <strong>seconds</strong> or <strong>ranges</strong>. Also <strong>ticker</strong> timeframes are excluded from this algorithms calculations.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Manual Timeframes</td>
            <td>Core Algorithm</td>
            <td><p>The purpose is to convert and map human-readable string representations of a timeframe (e.g., "<code>1 minute</code>", "<code>1 day</code>") into its corresponding code-compatible format.</p><p>This allows other trading modules to create a dropdown menu or inputs for the user to select a timeframe manually in a readable format.</p><h3>Key Points</h3><ul><li><strong>Flexibility:</strong> Supports many timeframes, from minutes to years.</li><li><strong>Error Handling:</strong> If an invalid string is passed (e.g., "<code>-10 minutes</code>"), the code returns <code>na</code>.</li><li><strong>Use Case:</strong> It simplifies working with user-defined or dynamically selected timeframes when writing extra code.</li></ul></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Time Periods</td>
            <td>Core Algorithm</td>
            <td>Works out the current timeframe period and places it into one of the following groups: <code>Ticks</code>, <code>Seconds</code>, <code>Minutes</code>, <code>Hours</code>, <code>Days</code>, <code>Weeks</code> or <code>Months</code>. Traders should be aware that it currently ignores: <code>Ranges</code>.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Timeframe Label</td>
            <td>Core Algorithm</td>
            <td>This is added to the core code and allows the timeframe to be displayed in the data window for various other algorithms. The various supported timeframes include: <code>seconds</code>, <code>minutes</code>, <code>hours</code>, <code>days</code>, <code>weeks</code> and <code>months</code>.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Timeframe Symbol</td>
            <td>Core Algorithm</td>
            <td>This is added to the core code and allows the timeframe to be displayed in the data window for various other algorithms. The various supported timeframes include: <code>S (for seconds)</code>, <code>M (for minutes)</code>, <code>H (for hours)</code>, <code>D (for days)</code>, <code>W (for weeks)</code> and <code>W (months divided into 4 weeks)</code>. Some examples: <code>M15</code> is 15 minutes, <code>W4</code> is 1 month.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Time Change</td>
            <td>Core Algorithm</td>
            <td>Compares the current source value to its value length bars ago and returns the difference.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Truncate</td>
            <td>Core Algorithm</td>
            <td>Truncate (cut) excess decimal places.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Format Large Numbers</td>
            <td>Core Algorithm</td>
            <td>Seeing <code>458698828817</code> instead of this <code>458.67 B</code> makes it harder on the eyes to work things out. To keep charts future proof, e.g. Bitcoin going over <code>100000</code> or even <code>1000000</code> prices will be written as <code>100 K</code> and <code>1 M</code> etc.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Milliseconds Timestamp</td>
            <td>Core Algorithm</td>
            <td>Find milliseconds for the current timeframe (CTF).</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Big Move Gauge</td>
            <td>Algorithm</td>
            <td><p>The big move gauge algorithm uses the daily calculations of volatility and time-weighted average prices (TWAP) calculated by taking price measurements at 1 minute intervals from the Bitcoin vs the US Dollar price. The <code>fast</code> setting uses a 24-hour H1 timeframe setting and the <code>slow</code> setting uses a rolling 7-day H1 timeframe setting.</p><p>The <code>fast</code> setting shows all the smaller individual moves and traders can look at each move to tell if the bulls or bears are in-control of the price action at that exact period. Traders can also use the <code>fast</code> setting to confirm U-Shape and V-Shape pattern moves. Traders can also use the <code>fast</code> setting to confirm lower-timeframe breakouts. Both the <code>fast</code>and <code>slow</code> modules uses the Trend Analysis Model 2 algorithm with a setting of <code>10.0</code> which is quicker than Trend Analysis Model 1 default setting. Traders can also use the <code>slow</code> setting to confirm higher-timeframe breakouts.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Dominance Algorithm</td>
            <td>Algorithm</td>
            <td><p>The "Dominance Algorithm" is a comprehensive tool designed for analysing cryptocurrency market dynamics. It tracks the dominance of Bitcoin, major altcoins, minor altcoins, and Stablecoins to provide insights into potential trading opportunities. It uses a unique algorithm to generate real-time trading signals based on market dominance shifts, trend analysis, and stablecoin flows.</p><h3>Key Features</h3><ul><li><strong>Market Dominance Tracking</strong>: Tracks the dominance of Bitcoin, major altcoins and minor altcoins.</li><li><strong>Stablecoin Analysis</strong>: Option to include stablecoin metrics with a choice between Tether USDT, Circle USDC and other Stablecoins.</li><li><strong>Trend Analysis</strong>: Uses Exponential Moving Average (EMA) to smooth dominance data and identify trends.</li><li><strong>Real-time Trading Signals</strong>: Generates potential buy/sell signals based on market conditions.</li><li><strong>Altcoin Season Detection</strong>: Identifies potential altcoin season beginnings and endings.</li><li><strong>Customizable Appearance</strong>: Offers options for dark and light themes, adjustable themes and background colouring based on market sentiment.</li><li><strong>Alert System</strong>: Provides alerts for dominance shifts, significant dominance differences, altcoin season events and stablecoin flows.</li><li><strong>Data Window</strong>: Displays real-time analysis in a customizable table format.</li></ul></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Crypto Market Sentiment</td>
            <td>Algorithm</td>
            <td><p>The Crypto Market Sentiment algorithm reflects the collective mood of investors overall regarding the cryptocurrency sector as a whole.</p><p>The mood of the market is affected by crowd psychology and can impact a coin or tokens outlook by the market's direction.</p><p>It involves analysing the collective mood of market participants, revealed through buying and selling activity, identifying bullish or bearish sentiment and navigating market volatility.</p><p>In general, rising prices imply optimism about the market, while declining prices suggest the opposite.</p><p>The Crypto Market Sentiment algorithm is split into three result sections, these deal with the short-term, medium-term and long-term sentiment of the cryptocurrency market as a whole.</p><p>The short-term looks at the 'Intraday' trading period, which is also referred to as 'Day Trading'.</p><p>The medium-term looks at the 'Swing' trading period, a style of trading that attempts to capture the medium-term gains in a cryptoasset (or any financial instrument) over a period of a few days to several weeks.</p><p>The long-term looks at the 'Position' trading period, a common trading strategy where an individual holds a position in a cryptoasset for a long period of time, typically over a number of months or years. In the context of cryptocurrencies, bull and bear markets relate to both the overall state of the market as well as specific markets. Given the daily changes and ongoing volatility of the market, these phrases are used to characterise longer periods of mostly positive or downward movement.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Liquidations</td>
            <td>Algorithm</td>
            <td><p>Crypto liquidations refer to the process of forcibly closing a trader's positions in the cryptocurrency market when their margin account cannot meet the required maintenance level. This occurs to cover margin calls and prevent further losses. Automated procedures like auto-liquidation algorithms are used by brokers to manage these liquidations in real-time.</p><p>The liquidation process typically involves stages such as pre-liquidation, automatic partial liquidation, liquidity support programs, insurance funds and auto-deleveraging to manage risks associated with margin trading. These processes aim to prevent excessive losses and maintain market stability in the face of high volatility in crypto-assets.</p><p>Many websites have crypto liquidation API's where the data is delayed for 1-4 hours (depending upon the exchange). The Liquidations Algorithm displays the liquidations in "real-time" with zero delay meaning it's a <code>leading</code> and not a <code>lagging</code> gauge. Which helps traders to better understand the dynamics of the overall crypto market and the cryptocurrency token they are trading.<p><strong>This algorithm added little benefit to traders and so the decision was to remove it from the main data window and add it to a separate trading algorithm to increase performance to the main trading algorithms.</strong></p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>Daily Change Percentage</td>
            <td>Algorithm</td>
            <td>The daily percentage change algorithm uses the closing price and calculates the percentage change in a cryptoassets value over a single day of trading. This calculation does not consider circulating supply or other factors that can be easily computed. It's used to frequently analyse fluctuations in cryptocurrency prices or market indexes over time. It helps track price changes in various financial instruments and is crucial for understanding the market dynamics. The calculations are fundamental in assessing the performance and volatility of a digital currency and other assets.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Divergence From Mean</td>
            <td>Algorithm</td>
            <td><p>This algorithm was dropped due to producing conflicting results for traders. For example, during a healthy up trend, price action will often be quite far away from the medium-term mean. The algorithm signalled a "high risk" trade when far away from the medium-term mean and suggested to traders to wait for a "low risk" trade instead.</p><p>However, even during a "pullback" period in an up trend the algorithm still signalled this as a "high risk" trade due to the large distance between price action and the medium-term mean.</p><p><strong>This resulted in many trading opportunities being missed by traders; due to these conflicting results and so this algorithm has been removed. Traders are advised to use the <code>Z-Score</code> algorithm instead.</strong></p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>TVL Buy Zone</td>
            <td>Algorithm</td>
            <td><p>The Total Value Locked (TVL) is usually manipulated on individual assets. By looking at the TVL for the whole cryptocurrency market, this reduces the noise and manipulation. The TVL Buy Zone shows 4 different labels, these are: 'Prepare To Buy', 'Buy Zone', 'Too Late To Buy' and 'Dumb Money'.</p><p>Prepare To Buy = is when extreme bearish market conditions makes the TVL drop down due to fear and signals that a trader should get ready for the buy zone label coming next.</p><p>Buy Zone = is when extreme bearish market conditions makes the TVL drop and signals to a trader to lookout for a possible buy trade, a trader could place a buy trigger combining the Trend Analysis Model 1 algorithm data. It's designed to help the trader buy the fear and not the greed.</p><p>Too Late To Buy = signals to the trader that the best time to buy is now over and price should've already triggered a buy trade and not to FOMO into the market.</p><p>Dumb Money = signals to the trader not to FOMO into the market and the need to wait for a better time to get into the market.</p><p>Note: The api data is displayed at the 'End of the Day' meaning it's not in real-time and shows the previous days data, this means there is a large delay!</p><p><strong>Due to this algorithm being a lagging indicator and giving a large delay (between 1-2 days). It has been deprecated and replaced by a new and improved algorithm system giving a zero delay and acting as a leading indicator. Traders are advised to use the <code>Medium-Term Sentiment</code>, <code>Medium-Term Polynomial</code> and <code>Medium-Term Z-Score</code> algorithms instead.</strong></p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>Z-Score</td>
            <td>Algorithm</td>
            <td>A Z-score is a statistical measurement that describes a value's relationship to the mean of a group of values, measured in terms of standard deviations from the mean. If a Z-score is 0, it indicates that the data point's score is identical to the mean score. Positive Z-scores indicate values above the mean, while negative scores indicate values below the mean.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Daily Sentiment Index</td>
            <td>Algorithm</td>
            <td><p>First it calculates the daily and intraday sentiment if it's bullish or bearish using blockchain api data. This results is four possible outcomes: Up Trend, Up Trend (pullback), Down Trend and Down Trend (pullback).</p><p>Note: The api data is displayed at the 'End of the Day' meaning it's not in real-time and shows the previous days data, this means there is a large delay!</p><p><strong>Due to this algorithm being a lagging indicator and giving a large delay (between 1-2 days). It has been deprecated and replaced by a new and improved algorithm system giving a zero delay and acting as a leading indicator. Traders are advised to use the <code>Medium-Term Sentiment</code>, <code>Medium-Term Polynomial</code> and <code>Medium-Term Z-Score</code> algorithms instead.</strong></p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>Market Cycle</td>
            <td>Algorithm</td>
            <td><p>Market cycles, refer to trends or patterns that emerge during different markets or business environments. These cycles include four phases: <code>accumulation</code>, <code>mark-up</code>, <code>distribution</code> and <code>downturn</code>. The <code>accumulation</code> phase occurs after the market has bottomed, the <code>mark-up</code> phase is when the market stabilizes and moves higher in price, the <code>distribution</code> phase sees sellers dominating as the stock reaches its peak and the <code>downturn</code> phase is when the stock price tumbles down. The algorithm worked this out using blockchain api data instead of price action data analyzing whale and retail trader blockchain wallet data.</p><p>Note: The api data is displayed at the 'End of the Day' meaning it's not in real-time and shows the previous days data, this means there is a large delay!</p><p><strong>Due to this algorithm being a lagging indicator and giving a large delay (between 1-2 days). It has been deprecated and replaced by a new and improved algorithm system giving a zero delay and acting as a leading indicator. Traders are advised to use the <code>Long-Term Sentiment</code> and <code>Long-Term Z-Score</code> algorithms instead.</strong></p></td></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>Alerts</td>
            <td>Core Algorithm</td>
            <td>Adds an alerts module to message the trader when one of the trading signals from any of the trading algorithms trigger a various trading condition! The trader can also select the frequency of the alerts in the options settings.</td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Trading Signals</td>
            <td>Core Algorithm</td>
            <td><p>The trading module processes the various trading algorithms that are currently used by the trader. The results are then displayed in a section of the data window, where the trader can show/hide in the menu options.</p><p>Different trading signals are displayed ranging from buy and sell signals through to informational signals. Actionable trading signals are displayed at the top of the list and informational signals are displayed below them. Each trading signal tells the trader what trading algorithm got called and a suggested trading action.</p><p>There are also complex trading signals merging several different trading algorithms together that get displayed in the data window.</p><p>All the trading signals are joined to the alerts module to be able to send various alerts to the trader such as email, txt, push notifications etc.</p><p>All the trading signals are also joined to the warning signals module, where the trader can highlight any of the trading signals on the trading chart.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Warning Signals</td>
            <td>Core Algorithm</td>
            <td><p>Traders can display any of the various trading algorithms and their corresponding warning signals (which can range from reversal and/or pullback buy and sell signals through to informational signals).</p><p>The purpose of the warning signals module is to allow traders to highlight these warning signals on the chart. The main difference between the warning signal module vs the trading signal module. The warning signal module highlights these warning signals on the chart whereas the trading signals module displays the information in the data window and not on the chart.</p><p>Traders can select any trading algorithm warning signal to display on the chart and use multiple different warning signals on the chart at the same time, allowing traders to generate more in-depth warning signals.</p><p>The default theme uses the following setup: green for buy warning signals, red for sell warning signals, grey for sideways warning signals and yellow for pullback area warning signals.</p><p>Traders can also select different themes and customize their own colours.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Nadaraya-Watson (Kernel Regression) Bands</td>
            <td>Algorithm</td>
            <td><p>The statistical techniques for regression function estimation that were created by G. S. Watson and E. A. Nadaraya in the 1960s are the foundation of the Nadaraya-Watson Envelope algorithm. The Nadaraya-Watson Envelope method and other trading tools were developed as a result of the kernel regression ideas they established, despite the fact that their work was not expressly focused on developing trading algorithms.</p><p>Watson-Nadaraya Regression is a subset of Kernel Regression, a non-parametric technique for determining a dataset's curve of best fit. In contrast to Polynomial or Linear regression, Kernel regression does not make any assumptions about the data's underlying distribution. It employs a kernel function for estimate, which is a weighting function that gives each data point a weight according to how near it is to the current point. The weighted average of the data points is then determined using the obtained weights.</p><p>Traders and programmers have developed trading algorithms that use historical price data to assess market patterns, spot possible reversals, and offer insights into price movements over time by using statistical techniques like kernel regression. The Nadaraya-Watson Envelope algorithm, which provides a non-repainting envelope based on Kernel Smoothing to outline market extremes and support technical analysis in trading strategies, has grown to be a useful tool for traders looking for precise and trustworthy insights into market trends and price dynamics.</p><p>By employing a kernel regression technique to smooth price data, the Nadaraya-Watson Envelope algorithm is a dynamic volatility algorithm that adjusts to shifting market conditions. To give limits for excessive price swings, it computes upper and lower bounds using the Average True Range (ATR) and certain variables.</p><p>By examining the link between price and envelopes, this technique is intended to assist traders in locating possible reversal zones and verifying the trend's direction.</p><p>Because of its broad applicability over a wide range of datasets, the Gaussian Kernel is one of the most widely used Kernel functions and is utilised extensively in many Machine Learning techniques. Imagine a Gaussian kernel on steroids. That's what the Rational Quadratic Kernel is - a bunch of Gaussian kernels with different length scales added together. This gives the user even more flexibility to adjust the indicator to suit their own requirements.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Semaphore Signal Level (SSL)</td>
            <td>Algorithm</td>
            <td><p>The Semaphore Signal Level (SSL) algorithm combines moving averages to provide you with a clear visual signal of near-term price movement dynamic. It's designed to show you all the price action pivot swing points. The algorithm has been modified to connect to the Moving Average and Custom Filter algorithm, to give traders the most amount of options and customizations.</p><p>This algorithm creates an envelope curve that tracks the market price by applying two moving averages, one to the price high and the other to the price low. Trading on the flip technique-where price goes from above the two moving averages to below them and vice versa-is the rationale behind this strategy.</p><p>The algorithm indicates that the direction of price movement is changing or likely to shift (from long to short or from short to long) when the two moving averages meet.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Themes</td>
            <td>Core Algorithm</td>
            <td><p>The themes module has various sections allowing traders to adjust the themes for: candlesticks, trading chart background, trading warning signals, the data window, trading algorithms and highlight weekend sessions. More themes and sections will be added over time!</p><p>The themes module provides various themes used in trading and charting software, such as:</p><h3>Light Theme</h3><p>A theme with a light background colour, typically white or off-white, and dark text colours. This theme is suitable for use in well-lit environments.</p><h3>Dark Theme</h3><p>A theme with a dark background colour, typically black or dark grey, and light text colours. This theme is suitable for use in low-light environments and can reduce eye strain.</p><h3>Coloured Theme</h3><p>A theme that incorporates various colours, often based on a specific colour scheme or palette. These themes can be customized to match branding or personal preferences.</p><h3>High Contrast Theme</h3><p>A theme designed to provide maximum contrast between the background and foreground elements, making it easier to read and distinguish different components. This theme is often used for accessibility purposes.</p><p>The glossary provides a concise explanation of each theme, helping users understand the different visual styles available in charting and trading applications.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Stablecoin Flows</td>
            <td>Algorithm</td>
            <td><p>The algorithm looks at the movements of Stablecoins and calculates the net money flow.</p><p><code>Inflows</code> are defined when Stablecoins deposited into the exchange wallets are more than Stablecoin withdrawal from the exchange wallets, this is a <strong>bearish</strong> trading signal.</p><p><code>Outflows</code>` are defined when Stablecoins withdrawn from the exchange wallets are more than Stablecoin deposited into the exchange wallets, this is a <strong>bullish</strong> trading signal.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>String-Manipulation</td>
            <td>Core Algorithm</td>
            <td><p>This module provides string manipulation features to the core algorithm code. The following list of features are provided:</p><ul><li>Returns the leftmost characters in the string.</li><li>Returns the rightmost characters in the string.</li><li>Returns the substring of the string from a range position with two specified points inclusively.</li><li>Returns the substring of the string to the left of a specified separating character.</li><li>Returns the substring of the string to the right of a specified separating character.</li><li>Returns the position of the first occurrence of a specified separating character in the string, where the first character position is <code>0</code>. Returns <code>-1</code> if the character is not found.</li><li>Replaces a character at a specified position in the string with a defined character or string.</li><li>Returns a formatted string with a rounded value to the symbol's tick precision.</li><li>Removes a particular substring from the end of another string.</li></ul><p><strong>Note for developers:</strong> Using too many string operations will negatively impact the performance of a trading algorithm. If at all possible, restrict the calculation of string manipulation routines in your code to the first or final candlestick bar of the dataset to reduce their influence. This can be accomplished by enclosing code blocks or by utilising the <code>var</code> keyword when declaring variables that hold the outcome of your text manipulations.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Moving Average and Custom Filter</td>
            <td>Trading Module</td>
            <td><p>A moving average filter is a simple low-pass filter that smooths out a signal by replacing each data point with the average of the neighbouring data points, defined within a fixed window size. It is commonly used to reduce random noise while preserving the sharp step response of a signal.</p><h3>Key Properties of Moving Average Filters</h3><ul><li>Easy to implement by convolving the input signal with a rectangular pulse of unit area.</li><li>Reduces random noise by a factor equal to the square root of the window size.</li><li>Preserves fast step response, making it suitable for time-domain encoded signals.</li><li>Introduces lag/delay in the output signal, as it is a causal filter.</li><li>Performs poorly for filtering frequency-domain encoded signals due to sub-optimal attenuation.</li></ul><p>A custom filter refers to a user-defined digital filter implemented on a hardware platform like an FPGA or microcontroller. Custom filters can be designed and optimized for specific applications, offering more flexibility and performance compared to standard off-the-shelf filters.</p><h3>Advantages of Custom Filters</h3><ul><li>Can be tailored to meet specific requirements, e.g. filter characteristics, resource utilization and real-time performance.</li><li>Allows combining multiple filtering techniques, such as linear (moving average) and nonlinear (median) filters, for effective noise and transient rejection.</li><li>Can be optimized for the target hardware platform, leveraging parallelism and pipelining for high-performance implementations.</li><li>Enables integration with other custom signal processing functions or control systems on the same hardware.</li></ul><p>In summary, moving average filters are simple and effective for smoothing time-domain signals, while custom filters offer flexibility and optimization for specific applications, often implemented on hardware platforms like FPGAs or microcontrollers.</p><p>This core module can be merged into any trading algorithm code to offer complex Moving Average and Custom Filters calculations.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Rational Quadratic Kernel (Support And Resistance Areas)</td>
            <td>Algorithm</td>
            <td><p>The Rational Quadratic kernel trading algorithm is a type of kernel function used in Gaussian Process Regression (GPR) models. It is derived from the Radial Basis Function (RBF) kernel and can be considered as an infinite sum of RBF kernels with different length-scales.</p><h3>Rational Quadratic Kernel Properties</h3><p>The Rational Quadratic kernel is defined as:</p><p><code>k(x, x') = (1 + (x - x')^2 / (2αl^2))^(-α)</code></p><p>Where:</p><ul><li><code>α</code> is a scale mixture parameter.</li><li><code>l</code> is the length-scale parameter.</li></ul><p>Some key properties of the Rational Quadratic kernel include:</p><ul><li><strong>Smoothness</strong>: It is an infinitely differentiable function, providing smooth predictions.</li><li><strong>Long-range Correlations</strong>: It exhibits long-range correlations, meaning data points far apart can still influence each othe's predictions.</li><li><strong>Flexibility</strong>: By varying the <code>α</code> parameter, it can approximate the behavior of other kernels like the RBF (<code>α → ∞</code>) or the Matérn class of kernels (<code>α = p/2</code>, where <code>p</code> is a positive integer).</li></ul><h3>Support and Resistance Areas</h3><p>While the Rational Quadratic kernel trading algorithm itself does not directly provide support and resistance areas, the Gaussian Process Regression model using this kernel can be employed to identify such areas based on the predicted mean and uncertainty estimates.</p><p>Potential support and resistance areas can be inferred from the predicted mean function, where:</p><ul><li>Local maxima may indicate potential resistance areas.</li><li>Local minima may indicate potential support areas.</li></ul><p>Additionally, the uncertainty estimates (e.g., variance) from the GPR model can help quantify the confidence in these potential support/resistance areas. Areas with lower uncertainty are more likely to be significant support/resistance levels.</p><p>In summary, the Rational Quadratic kernel trading algorithm offers a flexible and smooth kernel for GPR models, which can then be leveraged to identify potential support and resistance areas in financial data or other time series analysis tasks.</p><p><strong>This algorithm added little benefit to traders and so the decision was to remove it!</strong></p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/deprecated.jpg" alt="Deprecated"></td>
        </tr>
        <tr>
            <td>Bull-Bear Power (BBP)</td>
            <td>Algorithm</td>
            <td><p>The Bull-Bear Power (BBP) algorithm, otherwise known as the Elder-Ray Index, estimates the relationship between the strength of bulls (buyers) and bears (sellers) on an instrument. When the algorithm's value is nonzero, it supposedly suggests that either bulls or bears have more power in the market. The greater the distance is from zero, the greater the apparent dominance of bulls or bears. Positive values indicate higher bull power and negative values indicate higher bear power.</p><p>The logic is simple: the market situation is constantly changing as bears turn into bulls and vice versa. The indicators help to track this conversion and trade on it.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Daily Open</td>
            <td>Algorithm</td>
            <td><p>The daily open in a trading chart refers to the price at which a security begins trading when the market opens for a new trading day. It is a crucial data point in daily charts, representing the starting price for that day's trading session.</p><p>The daily open is significant for several reasons:</p><ol><li>It provides a reference point for intraday price movements.</li><li>It can indicate market sentiment at the start of trading.</li><li>It is often used in various trading strategies and technical analysis techniques.</li></ol><p>For Crypto traders, it's important to note that the concept of a daily open can vary depending on time zones, as the Crypto market operates 24 hours a day. In the Crypto market, the daily open is often considered to be at UTC time, which marks the beginning of a new trading day for many traders.</p><p>Understanding the daily open is essential for traders who use daily charts to analyze market trends, identify potential trading opportunities, and make informed decisions about their trades.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>Volatility</td>
            <td>Trading Module</td>
            <td><p>It's a comprehensive volatility algorithm, combining various algorithms and custom volatility strength calculations. It allows users to configure parameters and historical comparison periods. The volatility algorithm can output volatility strength as a color-coded step line and includes alerts for extreme volatility, trend direction changes and abnormal volatility levels. The data can be sent to the data window module to display the real-time current volatility strength.</p><h3>Key Features</h3><ul><li><strong>Volatility Strength Meter:</strong> Determines volatility strength is currently "Low," "Medium," "High," or "Extreme." Think of it like a weather report for price swings.</li><li><strong>Volatility Percentile:</strong> It compares current price movement to the lowest price movements, this helps identify unusually low price movements.</li><li><strong>Volatility Squeeze Detection:</strong> Check to see if price movements are very tight or consolidated, usually happens before a breakout or major price change.</li><li><strong>Customizable Look-back Period:</strong> You can adjust the settings to tell the tool how far back to look when figuring out what "normal" price movement is.</li><li><strong>Volatility Ratio:</strong> Calculates the ratio between the current Volatility and historical average Volatility.</li><li><strong>Historical Comparison:</strong> Compares current Volatility to historical average Volatility over a user-defined period.</li><li><strong>Customizable Parameters:</strong> Users can adjust parameters and historical comparison periods.</li><li><strong>Visualizations:</strong> Color-coded step line for volatility strength.</li><li><strong>Alerts:</strong> Notifications for significant market changes.</li><li><strong>Data Window:</strong> Displays volatility strength with customizable appearance from the themes module.</li></ul><h3>Applications</h3><ul><li><strong>Identify Accumulation Zones:</strong> Detects periods of <code>low volatility</code>, which often coincide with accumulation phases and can be used in conjunction with other algorithms and market analysis techniques to confirm these zones.</li><li><strong>Volatility Breakouts:</strong> Identify periods of <code>extreme</code> or <code>abnormal volatility</code> for breakout trades.</li><li><strong>Risk Management:</strong> Adjusts position sizing based on volatility levels.</li></ul><p>The Volatility Algorithm provides traders with a versatile tool to analyse market volatility, enhancing decision-making efficiency.</p></td>
            <td><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/trading-algorithms/enabled-by-default.jpg" alt="Enabled by default"></td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
</table>
