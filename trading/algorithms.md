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
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
</table>
