import streamlit as st

from blood_db import Donor

st.title("Retrieve all Donors")

c=Donor()
records=c.list()
st.write("")


if records:
   st.table(records)
else:
    st.info("No records Found")