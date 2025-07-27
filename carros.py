import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt

import os
print(os.listdir("../input/"))

df=pd.read_csv('../input/brazil-car-sales-records-from-1990-to-2022/dados.csv')
df.head()