import streamlit as st
st.title("SPGA Estimator")
c=st.number_input("Enter your present CGPA",min_value=0,step=1.0,format="%f")
n=st.number_input("Enter number of Semesters held",min_value=1)
e=st.number_input("Enter your target CGPA after this semester",min_value=0,step=1.0,format="%f")
s=0
x=round(((n*c)+s)/(n+1))
while x<=e:
	s+=0.01
	x = round(((n * c) + s) / (n + 1),2)
if s>10:
	st.write("You cannot reach your espected CGPA!!")
else:
	st.write("You need to score minimum of ",s," SGPA in your next semester")
