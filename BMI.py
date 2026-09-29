import streamlit as st

weight = st.number_input("Enter the weight in kg",min_value=0)
height = st.number_input("Enter the height in meters",min_value=0)

btn = st.button("Calculate BMI")

print(btn)

if btn:
    BMI=weight/height**2

    if BMI <= 18.5:
        st.info("Underweight")

    elif 18.5<=BMI<=25:
        st.success("Normal")

    elif 25<=BMI<=30:
        st.warning( "Overweight")

    else:
        st.error("Obesity")

    st.write("BMI is",BMI)