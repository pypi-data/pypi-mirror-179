## Generating Diagnostic Table using python

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

To install and import the package
 ```
  pip install Diagnostictable
  ```

 ```
from Diagnostictable import diagnostictable
 ```
To generate table follow these steps

Import these packages
 ```
  -import pandas as pd
  ```
 ```
  -import numpy as np
  ```

 ```
  -import datetime
  ```

 ```
  -from datetime import datetime, timedelta
  ```





Load these data
 ```
  -icd_10
  ```
 ```
  -diagnoses
  ```
 ```
  -new_group
  ```



Example

 ```
  table=diagnostictable(icd_10,diagnoses,new_group)
  table
 ```
