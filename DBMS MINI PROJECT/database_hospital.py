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

def create_hospital_table():
      c.execute('CREATE TABLE IF NOT EXISTS hospital ( H_ID int not null,H_Name varchar(70) not null,H_Address varchar(150) not null,Ph_Number varchar(11),PRIMARY KEY(H_ID));')

def add_hospital_data( H_ID ,H_Name,H_Address ,Ph_Number):
      c.execute('INSERT INTO  hospital ( H_ID ,H_Name,H_Address ,Ph_Number) VALUES(%s,%s,%s,%s)',( H_ID ,H_Name,H_Address ,Ph_Number))
      mydb.commit()

def view_hospital_details():
      c.execute('SELECT * FROM HOSPITAL')
      data=c.fetchall()
      return data

def delete_hospital_row(H_ID):
    c.execute('DELETE From Hospital where  H_ID="{}"'.format(H_ID))
    mydb.commit()

def update_hospital_row(H_ID, new_H_Name, new_H_Address, new_Ph_Number):
      c.execute("UPDATE hospital SET H_Name=%s, H_Address=%s, Ph_Number=%s WHERE H_ID=%s;",(new_H_Name, new_H_Address, new_Ph_Number,H_ID))
      mydb.commit()
      data = c.fetchall()
      return data

def queryy(x):
    c.execute(x)
    data = c.fetchall()
    return data


