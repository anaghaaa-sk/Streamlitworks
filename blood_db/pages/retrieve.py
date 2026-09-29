import streamlit as st

from blood_db import Donor

st.title("Retrieve Donor Details")

i=st.number_input("Enter ID",min_value=0)
btn=st.button("Retrieve")

if btn:

    c=Donor()
    records=c.retrieve(i)
    print(records)

    if records:
        st.write("Name:", records[1])
        st.write("Blood Group:", records[2])
        st.write("Phone:", records[3])
        st.write("City:", records[4])
        st.write("Last Donation:", records[5])

    else:
        print("No Records Found")












