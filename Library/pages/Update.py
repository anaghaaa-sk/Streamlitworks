import streamlit as st
from Library_db import BookListCreateRetrieveUpdateDelete

st.title("Update Record")

i=st.number_input("Enter ID",min_value=0)
title=st.text_input("Title")
author=st.text_input("Author")
price=st.number_input("Price",min_value=0)
language=st.text_input("Language")
pages=st.number_input("Pages",min_value=0)

btn=st.button("Update")

if btn:

    b=BookListCreateRetrieveUpdateDelete()
    records=b.update(i,title, author, price, language, pages)

    print(records)

    if records:

        st.success(" Record is Updated successfully")

    else:
        st.error("No Record Found")








