## Generating Lab Event Pivot Table using python

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

To install and import the package
 ```
  pip install MimicL
  ```

 ```
from MimicL import ltable
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
  labevents_data=pd.read_csv()
  ```
 ```
  propensity_data=pd.read_csv()
  ```
 ```
  labitems_data=pd.read_csv()
  ```



Example

 ```
  table=ltable(labevents_data,propensity_data,labitems_data)
  table
 ```
