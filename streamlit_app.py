import streamlit as st

st.title("Layer's of the Earth 🌎")
st.subheader("Coded by Caden Song")
st.divider()

unit_list = ("Miles(mi)", "Kilometers(km)")

tab_about, tab_find_info, tab_crust, tab_mantle, tab_outer_core, tab_inner_core, = st.tabs(["About", "Find Info", "Crust", "Mantle", "Outer Core", "Inner Core"])

layer = ""
material = ""
temp = 0

with tab_about:

    st.header("Instructions")
    st.write(
    "To use this app, type a number into the Enter Depth box, then choose whether your depth is in Miles (mi) or "
    "Kilometers (km). After that, click the Find Info  button, and the Results tab will show you the Earth layer, "
    "material, temperature at that depth, etc."
)

    st.divider()

    st.header("About 🌍")

    st.write(
        "This app helps you learn about Earth's layers by entering a depth and finding what layer you would be in. "
        "It also shows the material in that layer and an estimated temperature."
    )

    st.write("**Earth Layers Used in This App:**")
    st.write("- Crust: 0 km to 70 km")
    st.write("- Mantle: 70 km to 2900 km")
    st.write("- Outer Core: 2900 km to 5100 km")
    st.write("- Inner Core: 5100 km to 6371 km")

    st.markdown(
        "**IMPORTANT NOTE**: The temperature values are simplified estimates using formulas, so they might not be accurate."
    )

with tab_find_info:
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

    if find:
        if find_layer.strip() == "":
            st.warning("Please enter a depth.")
            st.stop()

        try:
            depth = float(find_layer)
        except:
            st.warning("Please enter a number for depth (example: 120).")
            st.stop()

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
            material = "Semi-Solid Rock (Iron, Magnesium)"
        elif layer == "Outer Core":
            material = "Liquid Metal (Iron + Nickel)"
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

        if layer == "":
            st.warning("You haven't entered anything yet. Go to the Find Info tab, enter a depth, and click Find Info.")
        else:
            st.write("Layer:", layer)
            st.write("Material:", material)

            if temp == "Invalid" or temp == "Outside Earth":
                st.write("Estimated Temperature:", temp)
            else:
                st.write(" Estimated Temperature:", round(temp, 2), "°C")
    
col1, col2 = st.columns([1, 3])

with tab_crust:

    st.header("Crust")

    with col1:
        st.write("To start off, the crust is the most outer layer of our plant, and is the thinist layer. It is 25 miles (40 kilometers) thick, and is made out of two diffrent types of crust, continental, and oceanic. ")
        st.write("Oceanic crust, the crust beneath the ocean floor, is mostly made up basalt. On the otherhand, continental crust is mostly composed of diffrent types granite, and can be much thicker that oceanic crust. ")
        st.write("Information Found: https://education.nationalgeographic.org/resource/crust/")

    with col2:
        st.image('https://www.natgeokids.com/wp-content/uploads/2014/04/structure-of-the-earth-%E2%80%93-earths-crust.jpg', caption = 'Picture from National Geographic Kids: The Crust', width = 350)

with tab_mantle:
    st.header("Mantle")
    st.write("")

with tab_outer_core:
    st.header("Outer Core")
    st.write("")

with tab_inner_core:
    st.header("Inner Core")
    st.write("")
