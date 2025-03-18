# Theme Module

### Description

The content below provides information about the theme module used to style trading charts. It includes a list of predefined color themes, each with its corresponding color name and hexadecimal (hex) color code. These themes are designed to enhance the visual appearance and usability of the trading charts by applying consistent and aesthetically pleasing color schemes. 

### Theme Details

| Theme  | Color Name | Hex     |
| ------ | ---------- | ------- |
| Yellow | Early Dawn | #FFF9E5 |
| Pink   | Serenade       | #FFF1E5    |
| Blue    | Selago        | #F1F7FD     |
| Grey    | Alto       | #DBDBDB    |
| White    | White       | #FFFFFF     |
| Black | Cod Gray | #0F0F0F |

This table serves as a reference for developers and designers to implement the specified color themes effectively within the trading chart interface.

We are committed to providing the best possible user experience and are actively developing new themes to enhance your trading chart interface. More exciting themes will be added soon, offering you even greater flexibility and customization options to suit your preferences.

### How can I customize the theme module for different trading charts?

To customize the theme module for different trading charts, you have several options depending on the platform you're using:

1. Access the Chart Settings menu and select Color Scheme.
2. Create a new color scheme by copying an existing one or starting from scratch.
3. Modify colors for specific chart elements to your preference.
4. Save multiple color schemes and apply them to individual charts.
5. Use the Custom themes API to override default colors of light and dark themes.
6. Utilize the `changeTheme` method to switch themes dynamically.

## Highcharts

1. Create a custom theme by defining an options object with your desired styles.
2. Apply the theme using the `Highcharts.setOptions` method.
3. For styled mode:
   - Create a CSS file and import default Highcharts styles.
   - Re-declare CSS variables to customize colors and styles.
   - Use the Palette Helper tool to generate color variations.

## General Tips

- Adjust background colors, candlestick colors, and indicator colors for better visibility.
- Create and save templates to quickly apply your preferred settings across multiple charts.
- Consider using dark themes for reduced eye strain during extended trading sessions.
- Experiment with different color combinations to find what works best for your trading style and preferences.

By following these guidelines, you can create personalized themes that enhance your trading experience and improve chart readability across various platforms.
