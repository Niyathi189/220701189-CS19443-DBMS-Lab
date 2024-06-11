import pandas as pd
import streamlit as st
import plotly.express as px
from database_hospital import *
from database_doctor import *
from database_organ import *
from database_donor import *
from database_patient import *


def read_hospital():
    result = view_hospital_details()
    # st.write(result)
    df = pd.DataFrame(result, columns=['H_ID' ,'H_Name','H_Address' ,'Ph_Number'])
    with st.expander("View all Hospitals"):
        st.dataframe(df)

def read_doctor():
    result = view_doctor_details()
    # st.write(result)
    df = pd.DataFrame(result, columns=['H_ID' ,'D_Name','DOB' ,'D_ID'])
    with st.expander("View all Doctors"):
        st.dataframe(df)


def read_donor():
    result = view_donor_details()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Donor_ID' ,'organ_donated','H_ID' ,'reason_of_donation','date_of_donation'])
    with st.expander("View all Donors"):
        st.dataframe(df)

def read_organ():
    result = view_organ_details()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Organ_ID' ,'Organ_name','Donor_ID' ])
    with st.expander("View all organs"):
        st.dataframe(df)

def read_patient():
    result = view_patient_details()
    # st.write(result)
    df = pd.DataFrame(result, columns=['patient_ID' ,'name','date_of_Birth','organ_ID','reason_of_request','date_of_procurement','d_id' ])
    with st.expander("View patient details "):
        st.dataframe(df)


def count_doctor():
    result = view_doctor_count()
    # st.write(result)
    df = pd.DataFrame(result, columns=['count','H_ID'])
    with st.expander("View number of doctors in each hospital "):
        st.dataframe(df)

def view_date():
    date_ID  = st.date_input("enter a date ")
    data=new_func(date_ID)
    df = pd.DataFrame(data, columns=['Donor ID   Organ Name'])
    with st.expander("View number of doctors in each hospital "):
        st.dataframe(df)

