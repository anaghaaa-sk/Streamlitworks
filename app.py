import streamlit as st

#number_input()
#text_input()
#date_input


#NUMBER
num1=st.number_input("Enter Number1",min_value=0)
num2=st.number_input("Enter Number2",min_value=0)
#
# st.write(num1)
# st.write(num2)



#TEXT
name=st.text_input("Enter your Name")
# st.write(name)


#DATE
date=st.date_input("Enter date")
# st.write(date)


#BUTTON
# button()

btn=st.button("Click")
print(btn)


if btn:
    st.write(num1)
    st.write(num2)
    st.write(name)
    st.write(date)












