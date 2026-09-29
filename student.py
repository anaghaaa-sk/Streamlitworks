import streamlit as st
from datetime import date

st.title("Student Registration Form")

name=st.text_input("Name")

age=st.number_input("Age",min_value=0)

dob=st.date_input("DOB",min_value=date(1990,1,1),
                        max_value=date.today(),
                        value=date(2006,1,1))

email=st.text_input("email")


g=st.radio("Gender",['male','female'])


s=st.selectbox("Courses",['python','dotnet','testing'])


btn=st.button("Submit")
print(btn)

if btn:
    st.write("Name",name)
    st.write("Age",age)
    st.write("DOB",dob)
    st.write("email",email)
    st.write(g)
    st.write(s)