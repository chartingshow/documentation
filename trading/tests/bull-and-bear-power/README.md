# Bull and Bear Power (BBP)

The Bull Bear Power (BBP) algorithm, otherwise known as the Elder-Ray Index, estimates the relationship between the strength of bulls (buyers) and bears (sellers) on an instrument. When the algorithm's value is nonzero, it supposedly suggests that either bulls or bears have more power in the market. The greater the distance is from zero, the greater the apparent dominance of bulls or bears. Positive values indicate higher bull power and negative values indicate higher bear power.

## Libraries required

- sklearn
- talib
- pandas
- numpy

> Python 3.6 or later

## How to Use

```python
# import the package
from Bull_and_Bear_Power import makeBBP # this function returns a pandas series with the indicator values and the raw dataset

df =  pd.read_csv("dataframe.csv")
bbp,sl = makeBBP(df,10) # (df,period)
print(bbp)
```

## Sample Figure

<p align="center"><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/tests/bull-and-bear-power.png" alt="Bull and Bear Power"></p>
