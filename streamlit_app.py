import streamlit as st

st.title("Layer's of the Earth 🌎")
st.header("Coded by Caden Song")
st.subheader("Intstructions")
st.markdown("To use this app, type a number into the **Enter Depth** box, then choose whether your depth is in Miles(mi) or Kilometers(km). After that, click the Find Info button, and the app will instantly calculate the necessary information.")
st.divider()

unit_list = ("Miles(mi)", "Kilometers(km)")

st.header("Find Info")

find_layer = st.text_input("Enter Depth")
selected_option = st.selectbox("Enter Unit for Depth", unit_list)

find = st.button("Find Info ✅")

if find:
    if find_layer.strip() == "":
        st.warning("Please enter a depth.")
        st.stop()

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


    if layer == "Crust":
        material = "Solid Rock (Granite, Basalt)"
    elif layer == "Mantle":
        material = "Semi-Solid Rock (Iron, Magnesium, and Calcium)"
    elif layer == "Outer Core":
        material = "Liquid Metal (Iron, Nickel)"
    elif layer == "Inner Core":
        material = "Solid Metal (Iron + Nickel)"
    else:
        material = "Unknown"


    if depth_km < 0:
        temp = "Invalid"
    elif depth_km > 6371:
        temp = "Outside Earth"
    elif depth_km <= 70:
        temp = 15 + (depth_km * 14)
    elif depth_km <= 2900:
        temp = 1000 + ((depth_km - 70) * 0.95)
    elif depth_km <= 5100:
        temp = 3700 + ((depth_km - 2900) * 0.60)
    else:
        temp = 5000 + ((depth_km - 5100) * 1.10)

    st.divider()
    st.header("Results")

    st.write("Layer:", layer)
    st.write("Material:", material)

    if temp == "Invalid" or temp == "Outside Earth":
        st.write("Temp:", temp)
    else:
        st.write("Temp:", round(temp, 2), "°C")
