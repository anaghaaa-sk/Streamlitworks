import streamlit as st
from blood_db import Donor
st.title("Delete Donor Details")


i=st.number_input("Enter ID",min_value=0)
btn=st.button("Delete")

if btn:

    c=Donor()
    records=c.delete(i)
    print(records)

    if records:

        st.success(" Record is Deleted successfully")

    else:
        st.error("No Record Found")