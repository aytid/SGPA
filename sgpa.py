import streamlit as st

st.title("SPGA Estimator")

c = st.number_input("Enter your present CGPA", min_value=0, step=1, format="%f")
n = st.number_input("Enter number of Semesters held", min_value=1)
e = st.number_input("Enter your expecting CGPA", min_value=0, step=1, format="%f")

s = 0
x = round(((n * c) + s) / (n + 1),2)

while x <= e:
    s += 0.1

st.write("You need to score ", s, " in your next semester")
