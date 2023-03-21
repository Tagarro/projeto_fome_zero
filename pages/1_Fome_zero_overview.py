import pandas as pd
import inflection
import plotly.express as px
import folium
import streamlit as st
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium, folium_static
from PIL import Image


st.set_page_config(page_title = 'Overview', page_icon = '📊', layout = 'wide')

#===============================================================================================
# Functions
#===============================================================================================

# Replace country names based on code
def country_name(country_id):
    
    """ This function creates a dictionary wich contains the corresponding country_id value
        
        Operations:
        1- Creates dictionary
        
        Input: Dataframe
        Output: Country Name
        
    """
    
    Countries = {
        1: 'India',
        14: 'Australia',
        30: 'Brazil',
        37: 'Canada',
        94: 'Indonesia',
        148: 'New Zeland',
        162: 'Philippines',
        166: 'Qatar',
        184: 'Singapure',
        189: 'South Africa',
        191: 'Sri Lanka',
        208: 'Turkey',
        214: 'United Arab Emirates',
        215: 'England',
        216: 'United States of America',
}

    return Countries[country_id]





def rename_columns(df):
    
    """ This function cleans the dataset
        
        Types of cleaning:
        1- Make a copy of the dataframe
        2- Creates a variable named "title" to capitalize all the words and replace some characters in the string
        3- Creates a variable named "snakecase" to make an underscored, lowercase form from the expression
        4- Creates a variable named "space" to remove blank spaces
        5- Creates a list containing the columns names
        6- Apply the variable named "title" to edit the column's names
        7- Apply the variable named "spaces" to edit the column's names
        8- Apply the variable named "snakecase" to edit the column's names
        9- Replaces the column's names with the edited column's name
        10- Split the cuisines columns values and select the first value
        11- Drop duplicates
        12- Delete the switch_to_order_menu column
        13- Reset the index
        
        Input: Dataframe
        Output: Dataframe
        
    """
    
    df1 = df.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df1.columns = cols_new
    df1['cuisines'] = df1.loc[:, 'cuisines'].astype(str).apply(lambda x: x.split(',')[0])
    df1 = df1.drop_duplicates(keep = 'first')
    del df1['switch_to_order_menu']
    df1 = df1.reset_index(drop = True)
    
    return df1





#===============================================================================================
# Import Dataset
#===============================================================================================

df = pd.read_csv('dataset/zomato.csv')



#===============================================================================================
# Cleaning Dataset
#===============================================================================================

df1 = rename_columns(df)

#===============================================================================================
# Adding country column
#===============================================================================================


df1['country'] = df1['country_code'].apply(country_name)


#===============================================================================================
# Sidebar
# ==============================================================================================

st.sidebar.markdown("""---""")

image_path = 'imagem_fome_zero.png'
image = Image.open(image_path)
st.sidebar.image(image, width = 100)

st.sidebar.markdown('# Fome Zero')

st.sidebar.markdown("""---""")



# Countries selection

country_select = st.sidebar.multiselect('Select the countries: ', ['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada', 'Singapure', 'United Arab Emirates', 'India', 'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey'], default = ['Philippines', 'Brazil', 'Australia', 'Canada', 'Singapure', 'United Arab Emirates', 'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey'])

countries_selection = df1['country'].isin(country_select)
df1 = df1.loc[countries_selection, :].reset_index()




# ==============================================================================================
# Streamlit Layout
# ==============================================================================================

with st.container():
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        
        unique_restaurants = len(df1['restaurant_name'].unique())
        col1.metric('Restaurants', unique_restaurants)
        
    with col2:
        
        countries_registered = len(df1['country_code'].unique())
        col2.metric('Countries', countries_registered)
        
    with col3:
        
        cities_registered = len(df1['city'].unique())
        col3.metric('Cities', cities_registered)
        
    with col4:
        
        votes_quantity = df1['votes'].sum()
        col4.metric('Votes', votes_quantity)
        
    with col5:
        
        cuisines_quantity = len(df1['cuisines'].unique())
        col5.metric('Cuisines', cuisines_quantity)
             
            
with st.container():
    
    m = folium.Map()

    marker_cluster = MarkerCluster().add_to(m)


    for i in range(len(df1)):
      folium.Marker([df1.loc[i, 'latitude'], df1.loc[i, 'longitude']], popup = f"Name: {df1.loc[i,'restaurant_name']} \nCountry: {df1.loc[i,'country']} \nCity: {df1.loc[i,'city']} \nRating: {df1.loc[i,'aggregate_rating']}", zoom_start = 10 ).add_to(marker_cluster)

    st_folium(m, width = 700)
