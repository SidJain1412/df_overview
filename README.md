# df_overview
## A pip package to give the user a quick overview of their dataset. (in a jupyter/iPython notebook)

---
### Currently, this package shows you:
* Number of rows
* Number of columns 
* Count of null values in each column
* Correlation plot
* First 5 rows
---
### Usage
Clone the repository. In the folder, open cmd and `pip install .`
The package is now installed.
Example usage:
```python
import df_overview
import pandas as pd
df=pd.read_csv("data.csv")
df_overview.overview(df)
```
Please be patient as the correlation plot may take time for a large number of columns.

---
This project will be updated soon.
