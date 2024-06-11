import pandas as pd
import streamlit as st
from database_hospital import *
from database_patient import *


def delete_hospital():
    H_ID  = st.number_input("Hospital Id:")
    H_Name = st.text_input("Name:")
    if st.button("Delete Hopsital"):
      delete_hospital_row(H_ID)
      st.success("Successfully delete : {}".format(H_Name)) 



def delete_patient():
    patient_ID  = st.number_input("Patient Id:")
    if st.button("Delete Hopsital"):
      delete_patient_row(patient_ID)
      st.success("Successfully delete : {}".format(patient_ID))  

