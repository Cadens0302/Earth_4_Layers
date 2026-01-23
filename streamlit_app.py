import streamlit as st

st.title("Layer's of the Earth 🌎")
st.subheader("Coded by Caden Song")
st.divider()

unit_list = ("Miles(mi)", "Kilometers(km)")

tab_about, tab_find_info, tab_crust, tab_mantle, tab_outer_core, tab_inner_core, tab_how, = st.tabs(["About", "Find Info", "Crust", "Mantle", "Outer Core", "Inner Core", "How I Coded My Website?",])

layer = ""
material = ""
temp = 0

with tab_about:

    st.header("Instructions")
    st.write(
    "To use this app, type a number into the Enter Depth box, then choose whether your depth is in Miles (mi) or "
    "Kilometers (km). After that, click the Find Info button, and the results will print out, showing you the Earth layer, "
    "material, temperature at that depth, etc. Additionally, there are other tabs for more information."
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
        "**IMPORTANT NOTE**: The temperature values are estimates created using formulas, so they might not be accurate."
    )

with tab_find_info:
    st.header("Find Info")
    st.write("")

    find_layer = st.text_input("Enter Depth Between")

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
    


with tab_crust:

    col_left_crust, col_right_crust = st.columns([1, 1.2])

    with col_left_crust:
        st.header("Crust")
        st.write("")
        st.write("To start off, the crust is the most outer layer of our plant, and is the thinist layer. It is next to the manlte, and is 25 miles (40 kilometers) thick. The crust solid, and is made out of two diffrent types of crust, continental, and oceanic. ")

        
    st.write("Oceanic crust, the crust beneath the ocean floor, is mostly made up basalt. On the otherhand, continental crust is mostly composed of diffrent types granite, and can be much thicker that oceanic crust because continetal crust stands taller, and penertrates deeper into the mantle, than oceanic crust. ")
    st.write("")
    st.write("")
    st.markdown("**Summary:**")
    st.write("Earth's Crust is made or two types oceanic, and continental. And is also the thinnest layer of the Earth.")
    st.write("")
    st.markdown("**Information Found:** https://education.nationalgeographic.org/resource/crust/, and https://www.amnh.org/exhibitions/permanent/planet-earth/how-has-the-earth-evolved/the-earths-crust")

    with col_right_crust:
        st.image('https://www.natgeokids.com/wp-content/uploads/2014/04/structure-of-the-earth-%E2%80%93-earths-crust.jpg', caption = 'Picture from National Geographic Kids: The Crust', width = 300)

with tab_mantle:

    col_left_mantle, col_right_mantle = st.columns([1, 1.2])

    with col_left_mantle:
        st.header("Mantle")
        st.write("")
        st.write("To begin with, the mantle is the second layer of the Earth, and lies between the crust, and the outer core. It is a semi-solid, and is about 2,900 kliometers (1,802 miles) thick. The mantle makes up 84% of the Earth's total volume.")
    
    st.write("The mantle is divided up into a few diffrent layers: the upper mantle, transition zone, lower mantle, and the D double-prime. ")

    with col_right_mantle:
        st.image('https://images.nationalgeographic.org/image/upload/v1638890152/EducationHub/photos/mantle-convection.jpg', caption = 'Picture from National Geographic Education: The Mantle', width = 400)
        st.write("")
    st.markdown("**Summary:**")
    st.write("The mantle is largest layer of Earth, and is made up of a few diffrent layers. ")
    st.write("")
    st.markdown("**Information Found:**")
    st.write("https://education.nationalgeographic.org/resource/mantle/")

with tab_outer_core:

    col_left_outer_core, col_right_outer_core = st.columns([1, 0.8])

    with col_right_outer_core:
        st.header("Outer Core")
        st.write("")
        st.write("In the first place, the outer core is the third main layer of Earth, and is between the mantle, and the inner core. The outer core is about 2,200 kilometers (1,367 miles) thick, and is in a liquid form, made from liquid iron and nickel. These two types of metal are very hot, and is about 5,000° C (9,032° F). This is an important layer for Earth because it creates the Earth's magnetic field, keeping us humans on the ground. ")

    with col_left_outer_core:
        st.image('https://collins.in/ebooks/csa/html/images/structure.png', caption = 'Picture from National Geographic Education: The Outer Core', width = 400)
        st.write("")
    st.markdown("**Summary:**")
    st.write("The outer core is the third main layer of the Earth, and creates the Earth's magnetic field.")
    st.write("")
    st.markdown("**Information Found:**")
    st.write("https://education.nationalgeographic.org/resource/core/")

with tab_inner_core:

    col_left_inner_core, col_right_inner_core = st.columns([1, 1.2])

    with col_left_inner_core:
        st.header("Inner Core")
        st.write("")
        st.write("One key aspect of the Earth is its the inner core. The inner core is the last main layer of the Earth, and is surronded by the outer core. This large solid ball is mostly made of iron, and has a radius of about 1,220 kilometers (758 miles). The inner core's temperature is 5,200° C (9,392° F). Since the inner core's temperature is so high the temperature exceeded the melting point of iron. Which is 1538°C (2800°F). ")
    st.write("However, unlike the outer core, the inner core is not liquid, the liquid core is solid! The inner core is solid because of the inner's core pressure. ")
    st.write("")

    with col_right_inner_core:
        st.image('https://www.datocms-assets.com/117510/1722316226-earth-structure20151004-11221-1dikwzi.jpg?auto=format&fit=max&w=1200', caption = 'Picture from Science Learning Hub: The Inner Core', width = 400)
        st.write("")
    st.markdown("**Summary:**")
    st.write("The inner core is the last main layer of the Earth, and is a solid though the temperature is way above iron's melting point.")
    st.write("")
    st.markdown("**Information Found:**")
    st.write("https://education.nationalgeographic.org/resource/core/")

with tab_how:
    st.header("How I Coded My Webstite?")
    st.write("To code this app, I used Streamlit, and used the Streamlit Community Cloud to connect Streamlit to Github. After that, I opened a new project, and started coding.")

    st.divider()

    st.subheader("Basic UI Coding:")
    st.write("")
    st.image('https://snipboard.io/tNAqH1.jpg', caption = 'The First Few Lines of My Code', width = 800)
    st.write("In Streamlit, to code basic UI (User Interface), you have to start the code with st, and then enter whatever you want to do. When using st.*blank*, you can write by coding st.write(""), you can add a button by coding st.button(), you can do a multi-select box by coding st.selectbox(), you can let the user type something by coding st.text_input(""), and there are many UI functions you can code by using st.**blank**.") 
    
    st.divider()

    st.subheader("Use of If Statments")
    st.write("")
    st.image('https://snipboard.io/gXSv68.jpg', caption = 'The If Statements In My Code', width = 800)
    st.write("When coding this website, I uuesdif statements because they helped my program make decision based on what the user type in. ")
