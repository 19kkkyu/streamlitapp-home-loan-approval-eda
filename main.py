
import pandas as pd
import numpy as np
import streamlit as st
import wash_data
import get_data

def main():

    x=st.sidebar.slider('The size of data:',0.0,1.0,1.0,0.01)
    df=wash_data.wash_data()
    is_graduate=st.sidebar.selectbox('Graduate', [True,False,None])
    is_married=st.sidebar.selectbox('Married', [True,False,None])
    is_female=st.sidebar.selectbox('Female', [True,False,None])
    is_self_employed=st.sidebar.selectbox('Self_employed', [True,False,None])
    is_urban=st.sidebar.selectbox('Urban', [True,False,None])
    credit_history=st.sidebar.selectbox('Credit_History',[True,False,None])
    df_selected=get_data.sidebar.select_data(x,is_graduate,is_married,is_female,is_self_employed,is_urban,credit_history)
    st.dataframe(df_selected)
    return None
    # radio('Pick one:', ['nose ','ear'])
    # st.selectbox('Select', [ 1, 2,3])
    # st.multiselect('Multiselect', [ 1, 2,3])
    # st.slider('Slide me', min_value=0, max_value=10)
    # st.select_slider('Slide to select', options=[ 1,'2'])
    # st.text_input('Enter some text')
    # st.number_input('Enter a number')
    # st.text_area('Area for textual entry')
    # st.date_input('Date input')
    # st.time_input('Time entry')
    # st.file_uploader('File uploader')
    #
    # st.camera_input("一二三,茄子!")
    # st.color_picker('Pick a color')

main()






