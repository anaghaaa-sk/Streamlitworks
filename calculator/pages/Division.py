import streamlit as st

num1=st.number_input("Enter Number1",min_value=0)
num2=st.number_input("Enter Number2",min_value=0)

btn=st.button("DIV")
print(btn)


if btn:

    st.write("Result is",num1/num2)