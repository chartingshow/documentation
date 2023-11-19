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
            <td>Algorithm</td>
            <td>This algorithm was added to predicted the near-term price action by default.
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
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
</table>
