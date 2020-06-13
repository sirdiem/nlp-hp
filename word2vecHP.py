#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import modules & set up logging
import gensim, logging
import os


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
 
sentences = MySentences('Documents/USC/HarryPotter') # directory location of all 7 Harry Potter books


model = gensim.models.Word2Vec(sentences)


model = gensim.models.Word2Vec(sentences, min_count=10)  # default value is 5; pruning the internal dictionary
                        

model = gensim.models.Word2Vec(sentences, size=200)  # default value is 100; number of dimensions of the N-dimensional space

model = gensim.models.Word2Vec(sentences, workers=4) # default = 1 worker = no parallelization


# In[ ]:


model.similarity('Harry','Ron')


# In[ ]:


model.similarity('Harry','Voldemort')


# In[ ]:


model.similarity('Malfoy','Voldemort')


# In[ ]:




