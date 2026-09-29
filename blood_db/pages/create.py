import streamlit as st

from blood_db import Donor

st.title("Add a New Donor")

name=st.text_input("Name")
blood_group=st.text_input("Blood Group")
phone=st.number_input("Phone",min_value=0)
city=st.text_input("City")
last_donation=st.date_input("Last Donation")

btn=st.button("Add")

if btn:
    c=Donor()
    c.create(name,blood_group,phone,city,last_donation)
    st.success("Create record successfully")