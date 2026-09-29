import streamlit as st

#title()
st.title("Welcome to my app")

# header
st.header("Main header")

# subheader()
st.subheader("Subheading")

# write()
st.write("My Name is Anagha")
st.write(100)
st.write([10,20,30])
st.write({'a':10,'b':20})


#Radio button
st.radio("Gender")
g=st.radio("Gender",['male','female'])
st.write(g)


#checkbox
l=st.checkbox("python")
st.write(l)

#select
s=st.selectbox("places",['ekm','trsr','tvm'])
st.write(s)



