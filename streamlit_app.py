import streamlit as st

st.title("Layer's of the Earth 🌎")
st.write("Coded by Caden Song")
st.divider()

unit_list = ("Miles(mi)", "Kilometers(km)")

st.header("Find Info")

find_layer = st.text_input("Enter Depth")
selected_option = st.selectbox("Enter Unit for Depth", unit_list)
import streamlit as st

st.title("Layer's of the Earth 🌎")
st.write("Coded by Caden Song")
st.divider()

unit_list = ("Miles(mi)", "Kilometers(km)")

st.header("Find Info")

find_layer = st.text_input("Enter Depth")
selected_option = st.selectbox("Enter Unit for Depth", unit_list)

find = st.button("Find Info ✅")

if find:
    # ✅ If nothing is entered, show a message instead of crashing
    if find_layer.strip() == "":
        st.warning("Please enter a depth.")
        st.stop()

    depth = float(find_layer)

    # convert to km
    if selected_option == "Miles(mi)":
        depth_km = depth * 1.60934
    else:
        depth_km = depth

    # layer
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

    # temperature (simple)
    if depth_km < 0:
        temp = "Invalid"
    elif depth_km > 6371:
        temp = "Outside Earth"
    else:
        temp = 15 + (25 * depth_km)

    if layer == "Crust":
        material = "Solid Rock (Granite, Basalt)"
    elif layer == "Mantle":
        material = "Semi-Solid Rock (Iron, Magnesium, Silicon)"
    elif layer == "Outer Core":
        material = "Liquid Metal (Iron + Nickel)"
    elif layer == "Inner Core":
        material = "Solid Metal (Iron + Nickel)"
    else:
        material = "Unknown"

    st.write("Layer:", layer)

    if temp == "Invalid" or temp == "Outside Earth":
        st.write("Temp:", temp)
    else:
        st.write("Temp:", round(temp, 2), "°C")

        st.write("Material:", material)

find = st.button("Find Info ✅")

if find:
    # ✅ If nothing is entered, show a message instead of crashing
    if find_layer.strip() == "":
        st.warning("Please enter a depth.")
        st.stop()

    depth = float(find_layer)

    # convert to km
    if selected_option == "Miles(mi)":
        depth_km = depth * 1.60934
    else:
        depth_km = depth

    # layer
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

    # temperature (simple)
    if depth_km < 0:
        temp = "Invalid"
    elif depth_km > 6371:
        temp = "Outside Earth"
    else:
        temp = 15 + (25 * depth_km)

    st.write("Layer:", layer)

    if temp == "Invalid" or temp == "Outside Earth":
        st.write("Temp:", temp)
    else:
        st.write("Temp:", round(temp, 2), "°C")
