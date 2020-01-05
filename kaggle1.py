#!/usr/bin/env python
# coding: utf-8

# In[65]:


import pandas as pd


# In[66]:


traffic = pd.read_csv("..\cm-00_30_04_15_1c_fd\Downloads\mock-traffic-data\MockTrafficDataForMCNFP.csv")


# In[71]:


traffic.groupby('plate_id').plate_id.min()


# In[78]:


traffic.plate_id.value_counts().head()


# In[81]:


traffic.groupby('plate_id').plate_id.count()


# In[85]:


ar1=traffic.plate_id.unique()


# In[86]:


ar1[:50]


# In[88]:


traffic.groupby('plate_id').apply(lambda traffic:traffic.plate_id[0])


# In[ ]:




