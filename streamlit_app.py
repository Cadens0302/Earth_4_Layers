import streamlit as st

st.title("Layer's of the Earth 🌎")
st.write(
    "Coded by Caden Song"
)
st.divider()

unit_list = ("Miles(mi)", "Kilometers(km)")

st.header("Find Info")
st.write("")

find_layer = st.text_input("Enter Depth")

selected_option = st.selectbox(
    "Enter Unit for Depth",
    unit_list
)
st.write("")
st.write("")

find = st.button("Find Info")

layer = ""
temp = ""

if find:
    depth = float(find_layer)

    if selected_option == "Miles(mi)":
        depth_km = depth * 1.60934
    else:
        depth_km = depth

    if depth_km < 0:
        layer = "Invalid Layer"
    elif depth_km <= 70:
        layer = "Crust"
    elif depth_km <= 2900:
        layer = "Mantle"
    elif depth_km <= 5100:
        layer = "Outer Core"
    elif depth_km <= 6371:
        layer = "Inner Core"
    else:
        layer = "Outside Earth"

    if depth_km < 0:
        temp = "Invalid"
    elif depth_km <= 70:
        temp = 15 + (25 * depth_km)
    elif depth_km <= 2900:
        temp = 1800 + (0.5 * (depth_km - 70))
    elif depth_km <= 5100:
        temp = 3000 + (0.3 * (depth_km - 2900))
    elif depth_km <= 6371:
        temp = 4000 + (0.4 * (depth_km - 5100))
    else:
        temp = "Outside Earth"


    st.divider()

    st.header("Results")

    st.write("Layer:", layer)

    if temp == "Invalid" or temp == "Outside Earth":
        st.write("Temp:", temp)
    else:
        st.write("Temp:", round(temp, 2), "°C")

    
