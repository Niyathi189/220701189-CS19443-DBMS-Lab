import mysql.connector
import streamlit as st
import pandas as pd 
import plotly.express as px
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="swenik2112",
    database="PES1UG20CS078_organ"
)
c = mydb.cursor()

def create_doctor_table():
      c.execute('CREATE TABLE IF NOT EXISTS doctor(H_ID int,D_Name varchar(50),DOB DATE,D_ID int,PRIMARY KEY(D_ID));')

def view_doctor_details():
      c.execute('SELECT * FROM DOCTOR')
      data=c.fetchall()
      return data

def add_doctor_data( H_ID ,D_Name,DOB ,D_ID):
      c.execute('INSERT INTO  doctor ( H_ID ,D_Name,DOB ,D_ID) VALUES(%s,%s,%s,%s)',( H_ID ,D_Name,DOB ,D_ID))
      mydb.commit()

def view_doctor_count():
    c.execute('SELECT count(h_id) as count , h_id from doctor group by h_id')
    data = c.fetchall()
    return data