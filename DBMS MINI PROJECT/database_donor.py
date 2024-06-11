import mysql.connector
import streamlit as st
import pandas as pd 
import plotly.express as px
import random as r
import copy
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="swenik2112",
    database="PES1UG20CS078_organ"
)

c = mydb.cursor()

def view_donor_details():
    c.execute('SELECT * FROM DONOR')
    data=c.fetchall()
    return data

def add_donor_data(a,organ_donated, H_ID, reason_of_donation, date_of_Donation):
    organid=r.randint(100000,999999)
    c.execute('INSERT INTO donor (Donor_ID,organ_donated, H_ID, reason_of_donation, date_of_Donation) VALUES(%s,%s,%s,%s,%s)',(a,organ_donated, H_ID, reason_of_donation, date_of_Donation))
    mydb.commit()
    c.execute('INSERT INTO organ_available (Organ_ID,Organ_Name,Donor_ID) VALUES(%s,%s,%s)',(organid,organ_donated,a))
    mydb.commit()
    return a


def new_func(date):
    c.execute('SELECT  det_donor_details("{}")'.format(date))
    data=c.fetchall()
    return data
