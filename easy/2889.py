"""Reshape Data: Pivot
https://leetcode.com/problems/reshape-data-pivot
"""


import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')


data = {
    'city': ['Jacksonville', 'Jacksonville', 'ElPaso', 'ElPaso'],
    'month': ['January', 'February', 'January', 'February'],
    'temperature': [13, 23, 11, 12],
}

weather = pd.DataFrame(data)
print(pivotTable(weather))
