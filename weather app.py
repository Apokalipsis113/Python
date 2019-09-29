#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import os
import requests 


# In[2]:


#api.openweathermap.org/data/2.5/forecast?q={city name},{country code} request string from documentation
def get_weather(city):
    '''return weather for entred sity name'''
    #token
    token = '3b0b395acfbd1073bb48e4d5cd0ef122'
    #api adress for request
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': token, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    print(weather)
    label['text'] = format_response(weather)


# In[3]:


#parse json response to text for label
def format_response(weather):
    #trying to get structure fields
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        #building formated string
        final_str = 'City: %s \nConditions: %s \nTemperature (°С): %s' % (name, desc, temp)
    except:
        #if there was a problem inform the user
        final_str = 'There was a problem retrieving that information'

    return final_str


# In[4]:


#main window with name 'weather'
root = tk.Tk(className='Weather')
HEIGHT = 500
WIDTH = 600
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()


# In[5]:


#set background image
bg_file = tk.PhotoImage(file='bg_image.png')
bg_label = tk.Label(root,image=bg_file)
#placing image for fill background
bg_label.place(relwidth=1,relheight=1)


# In[6]:


#area for entry and button
frame = tk.Frame(root, bg='#80c1ff', bd=5)
#put it on top
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


# In[7]:


#entry box on frame
entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)


# In[8]:


#buttont for make request on frame
button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)


# In[9]:


#lower area for text
lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


# In[10]:


#label with current weather on lower_frame
label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)


# In[11]:


#start main window loop
root.mainloop()


# In[ ]:




