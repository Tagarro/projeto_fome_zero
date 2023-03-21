import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")


st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown("""---""")

st.write('# Fome Zero Growth Dashboard')

st.markdown(
    """
    Growth Dashboard was built to keep track of the Restaurant's growth metrics.
    ### How to use the Dashboard?
    - Overview:
        - General metrics.
        - Restaurants location's map with the option to add or remove countries on the sidebar.
        
    - Countries:
        - Cities, restaurants, votes and ratings charts by countries with the option to add or remove countries on the sidebar.
        
    - Cities:
        - Cities dashboard with the option to select the number of cities and countries on the dashboard.
        
    - Cuisines:
        - Cuisines dashboard with the option to select the countries, number of restaurants included on the top chart and cuisines included on the bottom two dataframes.
        
    ### Ask For Help
    - Time de Data Science """)