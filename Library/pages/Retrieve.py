import streamlit as st

from Library_db import BookListCreateRetrieveUpdateDelete

st.title("Book Details")

i=st.number_input("Enter ID",min_value=0)
btn=st.button("Retrieve")

if btn:

    b=BookListCreateRetrieveUpdateDelete()
    records=b.retrieve(i)
    print(records)

    if records:
        st.write("Title", records[1])
        st.write("Author", records[2])
        st.write("Price", records[3])
        st.write("Language", records[4])
        st.write("Pages", records[5])

    else:
        print("No Records Found")












