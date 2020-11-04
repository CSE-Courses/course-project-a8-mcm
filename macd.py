# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:24:45 2020

@author: Ralph
"""

from webscrape import *

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

url = get_url("csco")
write_to_csv(url)
df = pd.read_csv('output.csv', index_col=0, parse_dates=True)
df = df.reindex(index=df.index[::-1])
df.plot(y="Close", ylabel="Price", figsize=(10,8), title=get_company_name(url), rot=90)
plt.show()
