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

def view_organ_details():
      c.execute('SELECT * FROM organ_available')
      data=c.fetchall()
      return data