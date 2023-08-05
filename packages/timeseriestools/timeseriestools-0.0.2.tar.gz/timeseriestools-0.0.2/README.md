timeseriestools

```
from timeseriestools import TimeseriesTools
import pandas as pd

tst = TimeseriesTools()
tst.login("info@timeseries.tools", "some-password")


s = pd.Series(index=["2020-01-01", "2020-01-02", "2020-01-03"], data=[1, 2, 3])
s.index = pd.to_datetime(s.index)

tst.create_tearsheet(s)



```
