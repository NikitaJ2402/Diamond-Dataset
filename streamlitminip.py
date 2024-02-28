# MINI PROJECT
#streamlit run streamlitminip.py 


import streamlit as st 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns



st.title('WEB APP USING STREAMLIT')

st.title('Case Study on Diamond Dataset')

data=sns.load_dataset('diamonds')

st.write('Shape of Dataset :',data.shape)
menu=st.sidebar.radio('Menu',['home','Prediction Price'])

if menu=='home':
    st.header('Tabular Data of a Diamond')
    if st.checkbox('Tabular Data'):
        st.table(data.head(150))

    st.header('Statistical Summary of a DataFrame')
    if st.checkbox('Statistics'):
        st.table(data.describe())

    # if st.header('Correlation Graph'):
    #     fig,ax=plt.subplots(figsize=(10,5))
    #     sns.heatmap(data.corr(),annot=True,cmap='coolwarm')
    #     st.pyplot(fig)

    st.title('Graphs')
    graph=st.selectbox('Different Types of Graph',['Scatter Plot','Bar Plot','Histogram'])
    if graph=='Scatter Plot':
         value=st.slider('Filter Data Using Carat',0,6)
         data=data.loc[data['carat']>=value]
         fig,ax=plt.subplots(figsize=(10,5))
         sns.scatterplot(data=data,x='carat',y='price',hue='cut')    
         st.pyplot(fig)

    if graph=='Bar Plot':
        fig,ax=plt.subplots(figsize=(5,3))
        sns.barplot(x='cut',y=data.cut.index,data=data)
        st.pyplot(fig)st.title('Graphs')
    graph=st.selectbox('Different Types of Graph',['Scatter Plot','Bar Plot','Histogram'])
    if graph=='Scatter Plot':
         value=st.slider('Filter Data Using Carat',0,6)
         data=data.loc[data['carat']>=value]
         fig,ax=plt.subplots(figsize=(10,5))
         sns.scatterplot(data=data,x='carat',y='price',hue='cut')    
         st.pyplot(fig)

    if graph=='Bar Plot':
        fig,ax=plt.subplots(figsize=(5,3))
        sns.barplot(x='cut',y=data.cut.index,data=data)
        st.pyplot(fig)

    if graph=='Histogram':
        fig,ax=plt.subplots(figsize=(5,3))
        sns.distplot(data.price,kde=True)
        st.pyplot(fig)

    if graph=='Histogram':
        fig,ax=plt.subplots(figsize=(5,3))
        sns.distplot(data.price,kde=True)
        st.pyplot(fig)

if menu=='Prediction Price':
    st.title('Prediction Price of Diamond')
    
    from sklearn.linear_model import LinearRegression
    lr=LinearRegression()
    x=np.array(data['carat']).reshape(-1,1)
    y=np.array(data['price']).reshape(-1,1)
    lr.fit(x,y)

    value=st.number_input('carat',0.20,5.01,step=0.15)
    value=np.array(value).reshape(1,-1)
    prediction=lr.predict(value)[0]

    if st.button('Price Prediction($)'):
        st.write(f'{prediction}')