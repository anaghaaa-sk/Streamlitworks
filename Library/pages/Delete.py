import streamlit as st
from Library_db import BookListCreateRetrieveUpdateDelete
st.title("Delete Book Details")


i=st.number_input("Enter ID",min_value=0)
btn=st.button("Delete")

if btn:

    b=BookListCreateRetrieveUpdateDelete()
    records=b.delete(i)
    print(records)

    if records:

        st.success(" Record is Deleted successfully")

    else:
        st.error("No Record Found")