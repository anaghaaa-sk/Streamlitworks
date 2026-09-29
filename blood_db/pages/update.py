import streamlit as st
from blood_db import Donor

st.title("Update Donor Details")

i=st.number_input("Enter ID",min_value=0)
name=st.text_input("Name")
blood_group=st.text_input("Blood Group")
phone=st.number_input("Phone",min_value=0)
city=st.text_input("City")
last_donation=st.date_input("Last Donation")

btn=st.button("Update")

if btn:

    c=Donor()
    records=c.update(i,name,blood_group,phone,city,last_donation)

    print(records)

    if records:

        st.success(" Data is Updated successfully")

    else:
        st.error("No Data Found")








