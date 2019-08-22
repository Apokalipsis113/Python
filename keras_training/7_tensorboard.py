#!/usr/bin/env python
# coding: utf-8

# In[1]:


import keras
from keras import layers
from keras.datasets import imdb
from keras.preprocessing import sequence



# In[2]:


max_len = 200
max_features = 1000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
x_train = sequence.pad_sequences(x_train, maxlen=max_len)
x_test = sequence.pad_sequences(x_test, maxlen=max_len)


# In[3]:


model = keras.models.Sequential()
model.add(layers.Embedding(max_features, 32, input_length=max_len, name='embed'))
model.add(layers.Conv1D(16, 5, activation='relu'))
#model.add(layers.MaxPooling1D(5))
#model.add(layers.Conv1D(16, 5, activation='relu'))
model.add(layers.GlobalMaxPooling1D())
model.add(layers.Dense(1))
model.summary()
model.compile(optimizer='rmsprop',
             loss='binary_crossentropy',
              metrics=['acc'])


# In[4]:


#!mkdir board_log_dir


# In[5]:


callbacks = [keras.callbacks.TensorBoard(log_dir='board_log_dir',
                                        histogram_freq=1,
                                       # embeddings_freq=2,                                       
                                        embeddings_data=x_train)]
#  keras.callbacks.EarlyStopping(monitor='val_acc', patience=5)


# In[ ]:


history = model.fit(x_train, y_train,
                   epochs= 10,
                   batch_size=64,
                   callbacks=callbacks,
                   validation_split=0.2)


# In[ ]:


#!tensorboard --logdor=board_log_dir

