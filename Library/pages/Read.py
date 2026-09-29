import streamlit as st

from Library_db import BookListCreateRetrieveUpdateDelete

st.title("Book List")

b=BookListCreateRetrieveUpdateDelete()
records=b.list()
st.write("")


if records:
   st.table(records)
else:
    st.info("No records Found")





























