#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import os
import ast

import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('oil_data.csv', index_col=0)


# In[3]:


df.info()


# In[4]:


df['keywords']


# In[5]:


df.head()


# In[6]:


cryptoData = df.to_dict(orient='records')
cryptoData = sorted(cryptoData, key = lambda k: k['sentiment_score'])

text = ""
for article in cryptoData:
    run = ast.literal_eval(article['keywords'])
    for value in run:
        text += value + " "


# In[7]:


def transform_format(val):
    if val == 0:
        return 255
    else:
        return val


# In[8]:


rbc_mask = np.array(Image.open("img/rbc_mask.png"))
rbc_mask


# In[9]:


transformed_rbc_mask = np.ndarray((rbc_mask.shape[0], rbc_mask.shape[1]), np.int32)

for i in range(len(rbc_mask)):
    transformed_rbc_mask[i] = list(map(transform_format, rbc_mask[i]))


# In[10]:


transformed_rbc_mask


# In[11]:


#Create and generate a word cloud image:
wordcloud = WordCloud(width=960, height=480, max_font_size=100, max_words=100, background_color='white').generate(text)


# In[12]:


plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[13]:


wordcloud.to_file("img/wordcloud.png")


# In[ ]:




