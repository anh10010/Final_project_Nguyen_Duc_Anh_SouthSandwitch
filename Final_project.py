#conda activate cs_ftmle
#streamlit run Final_project.py
import streamlit as st
import datetime as dt
import pandas as pd
import numpy as np
import pickle
import sklearn
from sklearn.ensemble import RandomForestRegressor

menu = ['Home','Suicide Problem','Model','Predict Suicide Rate' ,'After credit']
choice = st.sidebar.selectbox('Menu',menu)
if choice=='Home':
    st.title('About me')
    st.write('Final Project  :Predict Suicide Rate')
    st.write('Name  :Nguyen Duc Anh')
    st.write('E-mail    :anh10010@gmail.com')       
    
    st.image('PIC\suicide-and-suicidal-behavior_thumb.jpg')
if choice=='Suicide Problem':
    st.image('PIC\Suicide-thumbnail.jpg')
    st.write('Suicide:The death caused by someones who injuring oneself with the intent to die')
    st.header('Reason:')
    st.write('1/Impulsivity')
    st.write('2/Substance use')
    st.write('3/Psychosis or Psychopath')
    st.header('Solution:')
    st.write('We need a model what can  Predict the Suicide rate in the near future')
    st.write('That will help ')
if choice=='Model':
    st.image('PIC\RMSE.jpg')
    st.header('Choose model')
    st.image('PIC\Choose model.png')
    st.header('Check model after Tuning')
    st.image('PIC\Model Tuning.png')
    st.header('After Train model I choose to use:')
    st.write('Random Forest Regression model')
    st.image('PIC\Random-Forest-Regression.png')
if choice=='Predict Suicide Rate':
    st.image('PIC\death-clock1-1625569443.jpg')    
    
    col1,col2=st.columns(2)
    with col1:
        country=st.text_input('Name of Country:', value="Where should I Go?")
        gdp=st.number_input('GDP(Billions $):',min_value=1.)
    with col2:
        year = st.number_input('Year:',max_value=2016,min_value=2015,step=1)
        no_pop=st.number_input('Population(Million):',min_value=0.01)
    # load the model from disk
    filename='Model\RandomForestRegressor.sav'
    loaded_model = pickle.load(open(filename, 'rb'))    
    if st.button('Calculate'):
        x={0:{'Country':country,'Year':year,'GDP ($)':gdp*1000000000,'Population':no_pop*1000000}}
        #Model Predict 
        x_df = pd.DataFrame.from_dict(x, orient='index')
        y_test_pred = loaded_model.predict(x_df)
        no_suicide=y_test_pred
        #Print Table and Predict
        a={0:{'Country':country,'Year':year,'GDP(Billions $)':int(gdp),'Population(Million)':int(no_pop),'No.Suicides':int(no_suicide[0])}}
        dk = pd.DataFrame.from_dict(a, orient='index')
        st.table(dk) 
        suicide_rate =  no_suicide[0]/(no_pop*10)
        st.write('Suicide rate per in ',country,' per 100000 pop :', round(suicide_rate,2))
        st.image(r'PIC\tomp.jpg')
if choice=='Credit':
    st.header('SOURCE')

    st.image('PIC\site-logo.png')
    st.write('https://www.kaggle.com/kralmachine/data-visualization-of-suicide-rates')
    st.write('https://www.kaggle.com/twinkle0705/mental-health-and-suicide-rates?select=Age-standardized+suicide+rates.csv')
