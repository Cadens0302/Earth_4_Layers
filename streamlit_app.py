import streamlit as st

st.title("Layer's of the Earth 🌎")
st.write(
    "Coded by Caden Song"
)
st.divider()

unit_list = ("Miles(mi)", "Kilometers(km)")

st.header("Find Info")
st.write("")

st.text_input("Enter Depth")

selected_option = st.selectbox(
    "Enter Unit for Depth", 
    unit_list 
)
st.write("")
st.write("")

find = st.button("Find Info")
