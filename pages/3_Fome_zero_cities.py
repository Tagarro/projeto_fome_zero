import pandas as pd
import inflection
import plotly.express as px
import folium
import streamlit as st
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium, folium_static
from PIL import Image


st.set_page_config(page_title = 'Cities', page_icon = '🌃', layout = 'wide')

#===============================================================================================
# Functions
#===============================================================================================


def rating_comparison_over(df1):
    
    """ This function exhibits the top cities with the highest aggregate_rating count above 4
        
        Operations:
        1- Selects all aggregate_rating above 4
        2- Groups by city and make a count
        3- Sort the restaurant_id values from highest to lowest
        4- Reset the index
        5- Exhibits the top cities based on the top_cities_slider slider
        6- Creates a bar chart with the 'city' and 'restaurant_id' values
        
        Input: Dataframe
        Output: Bar chart
        
    """

    df1_aux = df1['aggregate_rating'] > 4
    aux = df1.loc[df1_aux, ['city', 'restaurant_id']].groupby('city').count().sort_values('restaurant_id', ascending = False).reset_index().loc[0 : top_cities_slider, :]
    graph = px.bar(aux, x = 'city', y = 'restaurant_id')

    return graph



def rating_comparison_under(df1):
        
    """ This function exhibits the top cities with the highest aggregate_rating count below 2.5
        
        Operations:
        1- Selects all aggregate_rating below 2.5
        2- Groups by city nad make a count
        3- Sort the restaurant_id values from highest to lowest
        4- Reset the index
        5- Exhibits the top cities based on the top_cities_slider slider
        6- Creates a bar chart with the 'city' and 'restaurant_id' values
        
        Input: Dataframe
        Output: Bar chart
        
    """

    df1_aux = df1['aggregate_rating'] < 2.5
    aux = df1.loc[df1_aux, ['city', 'restaurant_id']].groupby('city').count().sort_values('restaurant_id', ascending = False).reset_index().loc[0 : top_cities_slider, :]
    graph = px.bar(aux, x = 'city', y = 'restaurant_id')

    return graph



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

country_select = st.sidebar.multiselect('Select the countries: ', ['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada', 'Singapure', 'United Arab Emirates', 'India', 'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey'], default = ['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada', 'Singapure', 'United Arab Emirates', 'India', 'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey'])

countries_selection = df1['country'].isin(country_select)
df1 = df1.loc[countries_selection, :].reset_index()



# Top amount select

top_cities_slider = (st.sidebar.slider('How many cities?', min_value = 0, max_value = 100) -1)


# ==============================================================================================
# Streamlit Layout
# ==============================================================================================


with st.container():
    
    # Top cities with most restaurants registrered
    st.markdown('### Top cities with most restaurants registrered')
    
    aux = df1.loc[:, ['city', 'restaurant_id']].groupby('city').count().sort_values(['restaurant_id', ], ascending = False).reset_index().loc[0 : top_cities_slider, :]
    graph = px.bar(aux, x = 'city', y = 'restaurant_id')
    st.plotly_chart(graph, use_container_width = True)
    
    st.markdown("""---""")
    
with st.container():
    
    col1, col2 = st.columns(2)
    
    with col1:
        
        # Top cities with over 4 Rating
        st.markdown('#### Top cities with over 4 Rating')
        
        graph = rating_comparison_over(df1)
        st.plotly_chart(graph, use_container_width = True)

    with col2:
        
        # Top cities with under 2.5 Rating
        st.markdown('#### Top cities with under 2.5 Rating')
        
        graph = rating_comparison_under(df1)
        st.plotly_chart(graph, use_container_width = True)
        
    st.markdown("""---""")
    
with st.container():
    
    # Top cities with the greatest variety of cuisines
    st.markdown('### Top cities with the greatest variety of cuisines')
    
    aux = df1.loc[:, ['city', 'cuisines']].groupby('city').nunique().sort_values('cuisines', ascending = False).reset_index().loc[0 : top_cities_slider, :]
    graph = px.bar(aux, x = 'city', y = 'cuisines')
    st.plotly_chart(graph, use_container_width = True)
