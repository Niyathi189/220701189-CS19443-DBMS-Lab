import streamlit as st
import random as r
from database_hospital import *
from database_doctor import *
from database_donor import *
from database_patient import *

def create_hospital():
    col1, col2 = st.columns(2)
    with col1:
        H_ID  = st.number_input("Hospital Id:")
        H_Name = st.text_input("Name:")
        
    with col2:
        H_Address=st.text_input("Address")
        Ph_Number=st.text_input("Number:")

    if st.button("Add Hospital"):
        add_hospital_data(H_ID, H_Name, H_Address, Ph_Number)
        st.success("Successfully added : {}".format(H_Name))
        



def create_doctor():
    col1, col2 = st.columns(2)
    with col1:
        H_ID  = st.number_input("Hospital Id:")
        D_Name = st.text_input("Enter Doctor Name:")
        
    with col2:
        DOB=st.date_input("Enter date of birth")
        D_ID=st.text_input("Enter Doctor Id")

    if st.button("Add Doctor"):
        add_doctor_data(H_ID, D_Name, DOB, D_ID)
        st.success("Successfully added : {}".format(D_Name))
        


def create_donor():
    col1, col2 = st.columns(2)
    with col1:
        H_ID  = st.number_input("Hospital Id:")
        organ_donated = st.text_input("Enter the type of Organ Donated:")
        
    with col2:
        
        date_of_Donation=st.date_input("Enter date of donation")
        reason_of_donation=st.text_input("Enter the reason for donation")

    if st.button("Add Donor"):
        a=a=r.randint(1000000,9999999)
        x=add_donor_data(a,organ_donated, H_ID, reason_of_donation, date_of_Donation)
        st.title(x)
        st.success("Successfully added : {}".format(reason_of_donation))
        


def create_patient():
    col1, col2 = st.columns(2)
    with col1:
        patient_ID  = st.number_input("Patient Id:")
        name = st.text_input("Enter the patient name ")
        organ_ID=st.text_input("Enter the organ id ")
        date_of_procurement=st.date_input("Enter date of Procurement")
    with col2:
        date_of_Birth=st.date_input("Enter date of Birth")
        reason_of_request=st.text_input("Enter the reason for request")
        d_id=st.number_input("Enter the doctor id ")

    if st.button("Add Donor"):
        a=a=r.randint(1000000,9999999)
        x=add_patient_data(patient_ID,name,date_of_Birth,organ_ID,reason_of_request,date_of_procurement,d_id)
  
        st.success("Successfully added : {}".format(patient_ID))
       