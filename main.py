
import pandas as pd
import numpy as np
import streamlit as st
import wash_data
import get_data

def main():

    x=st.sidebar.slider('The size of data:',0.0,1.0,1.0,0.01)
    df=wash_data.wash_data()
    is_graduate=st.sidebar.selectbox('Graduate', [None,True,False])
    is_married=st.sidebar.selectbox('Married', [None,True,False])
    is_female=st.sidebar.selectbox('Female', [None,True,False])
    is_self_employed=st.sidebar.selectbox('Self_employed', [None,True,False])
    is_urban=st.sidebar.selectbox('Urban', [None,True,False])
    credit_history=st.sidebar.selectbox('Credit_History',[None,True,False])
    df_selected=get_data.select_data(x,is_graduate,is_married,is_female,is_self_employed,is_urban,credit_history)
    st.dataframe(df_selected)
    fig,ax=plt.subplot()
    ax.plot(df_selected)
    st.pyplot(fig)
    return None

main()






