import streamlit as st

num1=st.number_input("Enter Number1",min_value=0)
num2=st.number_input("Enter Number2",min_value=0)

btn=st.button("Add")
print(btn)


if btn:

    st.write("sum is",num1+num2)