import streamlit as st


from Library_db import BookListCreateRetrieveUpdateDelete
st.title("Welcome to Library App")

b = BookListCreateRetrieveUpdateDelete()

tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','READ','RETRIEVE','UPDATE','DELETE'])

with tab1:
    st.write("ADD")
    st.title("Add New Record")

    title = st.text_input("Title")
    author = st.text_input("Author")
    price = st.number_input("Price", min_value=0)
    language = st.text_input("Language")
    pages = st.number_input("Pages", min_value=0)

    btn = st.button("Add")

    if btn:

        b.create(title, author, price, language, pages)
        st.success("Create record successfully")

with tab2:
    st.write("READ")

with tab3:
    st.write("RETRIEVE")
    st.title("Book Details")

    i = st.number_input("Enter ID", min_value=0)
    btn = st.button("Retrieve")

    if btn:


        records = b.retrieve(i)
        print(records)

        if records:
            st.write("Title", records[1])
            st.write("Author", records[2])
            st.write("Price", records[3])
            st.write("Language", records[4])
            st.write("Pages", records[5])

        else:
            print("No Records Found")

with tab4:
    st.write("UPDATE")

with tab5:
    st.write("DELETE")
    st.title("Delete Book Details")

    i = st.number_input("Enter ID", min_value=0)
    btn = st.button("Delete")

    if btn:


        records = b.delete(i)
        print(records)

        if records:

            st.success(" Record is Deleted successfully")

        else:
            st.error("No Record Found")