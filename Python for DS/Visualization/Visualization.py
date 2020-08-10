#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import os
from os.path import abspath,dirname,join


# In[2]:


data_dir = join(dirname(abspath('.')), 'data')
dir1 = os.path.abspath(os.path.dirname('.'))


# In[3]:


df = pd.read_csv('file.csv', delimiter=',')
df


# In[ ]:
