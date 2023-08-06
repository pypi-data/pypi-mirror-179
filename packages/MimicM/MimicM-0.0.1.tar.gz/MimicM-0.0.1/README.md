## Generating Medication Pivot Table using python

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

To install and import the package
 ```
  pip install MimicM
  ```

 ```
from MimicM import mtable
 ```
To generate table follow these steps

Import these packages
 ```
  import pandas as pd
  ```
 ```
  import numpy as np
  ```

 ```
  import datetime
  ```

 ```
  from datetime import datetime, timedelta
  ```





Load your data
 ```
  prescriptions_data=pd.read_csv()
  ```
 ```
  propensity_data=pd.read_csv()
  ```
 ```
  ndc2_data=pd.read_csv()
  ```



Example

 ```
  table=mtable(prescriptions_data,propensity_data,ndc2_data)
  table
 ```
