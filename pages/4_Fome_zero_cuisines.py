import pandas as pd
import inflection
import plotly.express as px
import folium
import streamlit as st
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium, folium_static
from PIL import Image


st.set_page_config(page_title = 'Cuisines', page_icon = '🍝', layout = 'wide')

#===============================================================================================
# Functions
#===============================================================================================



def top_cuisines(df1, ascending):
    
    """ This function exhibits the top 100 best and worst cuisine types
        
        Operations:
        1- Remove nan and Others cuisine types
        2- Groups cuisine types
        3- Take the average aggregate_rating
        4- Sort the aggregate_rating values depending on the ascending input
        5- Reset index
        6- Exhibits the top 100 values
        
        Input: Dataframe, ascending type (True or False)
        Output: cuisines Dataframe
        
    """
    
    
    df1_aux = (df1['cuisines'] != 'nan') & (df1['cuisines'] != 'Others')
    cuisines = df1.loc[df1_aux, ['aggregate_rating', 'cuisines']].groupby('cuisines').mean().sort_values('aggregate_rating', ascending = ascending).reset_index().head(100)

    return cuisines




def top_biggest_restaurants(df1):
    
    
    """ This function exhibits the top restaurants with the highest ratings
        
        Operations:
        1- Sort aggregate_rating(ascending) and restaurant_id(descending)
        2- Reset index
        3- Exhibits the top values based on the top_restaurants_slider slider
        4- Creates a chart with restaurant_name and aggregate_rating values
        
        Input: Dataframe
        Output: Bar Chart
        
    """

    aux = df1.loc[:, ['restaurant_name', 'restaurant_id', 'aggregate_rating', 'currency']].sort_values(['aggregate_rating', 'restaurant_id'],  ascending = [False, True]).reset_index(drop = True).loc[0 : top_restaurants_slider, :]
    graph = px.bar(aux, x = 'restaurant_name', y = 'aggregate_rating')

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

st.sidebar.markdown("""---""")

top_restaurants_slider = (st.sidebar.slider('How many restaurants?', min_value = 0, max_value = 100) -1)

st.sidebar.markdown("""---""")

# Cuisines selection

cuisines_select = st.sidebar.multiselect('Select the cuisines: ', ['Italian', 'European', 'Filipino', 'American', 'Korean', 'Pizza',
       'Taiwanese', 'Japanese', 'Coffee', 'Chinese', 'Seafood',
       'Singaporean', 'Vietnamese', 'Latin American', 'Healthy Food',
       'Cafe', 'Fast Food', 'Brazilian', 'Argentine', 'Arabian', 'Bakery',
       'Tex-Mex', 'Bar Food', 'International', 'French', 'Steak',
       'German', 'Sushi', 'Grill', 'Peruvian', 'North Eastern',
       'Ice Cream', 'Burger', 'Mexican', 'Vegetarian', 'Contemporary',
       'Desserts', 'Juices', 'Beverages', 'Spanish', 'Thai', 'Indian',
       'Mineira', 'BBQ', 'Mongolian', 'Portuguese', 'Greek', 'Asian',
       'Author', 'Gourmet Fast Food', 'Lebanese', 'Modern Australian',
       'African', 'Coffee and Tea', 'Australian', 'Middle Eastern',
       'Malaysian', 'Tapas', 'New American', 'Pub Food', 'Southern',
       'Diner', 'Donuts', 'Southwestern', 'Sandwich', 'Irish',
       'Mediterranean', 'Cafe Food', 'Korean BBQ', 'Fusion', 'Canadian',
       'Breakfast', 'Cajun', 'New Mexican', 'Belgian', 'Cuban', 'Taco',
       'Caribbean', 'Polish', 'Deli', 'British', 'nan', 'California',
       'Others', 'Eastern European', 'Creole', 'Ramen', 'Ukrainian',
       'Hawaiian', 'Patisserie', 'Yum Cha', 'Pacific Northwest', 'Tea',
       'Moroccan', 'Burmese', 'Dim Sum', 'Crepes', 'Fish and Chips',
       'Russian', 'Continental', 'South Indian', 'North Indian', 'Salad',
       'Finger Food', 'Mandi', 'Turkish', 'Kerala', 'Pakistani',
       'Biryani', 'Street Food', 'Nepalese', 'Goan', 'Iranian', 'Mughlai',
       'Rajasthani', 'Mithai', 'Maharashtrian', 'Gujarati', 'Rolls',
       'Momos', 'Parsi', 'Modern Indian', 'Andhra', 'Tibetan', 'Kebab',
       'Chettinad', 'Bengali', 'Assamese', 'Naga', 'Hyderabadi', 'Awadhi',
       'Afghan', 'Lucknowi', 'Charcoal Chicken', 'Mangalorean',
       'Egyptian', 'Malwani', 'Armenian', 'Roast Chicken', 'Indonesian',
       'Western', 'Dimsum', 'Sunda', 'Kiwi', 'Asian Fusion', 'Pan Asian',
       'Balti', 'Scottish', 'Cantonese', 'Sri Lankan', 'Khaleeji',
       'South African', 'Drinks Only', 'Durban', 'World Cuisine',
       'Izgara', 'Home-made', 'Giblets', 'Fresh Fish', 'Restaurant Cafe',
       'Kumpir', 'Döner', 'Turkish Pizza', 'Ottoman', 'Old Turkish Bars',
       'Kokoreç'], default = ['Italian', 'European', 'Filipino', 'American', 'Korean', 'Pizza',
       'Taiwanese', 'Japanese', 'Coffee', 'Chinese', 'Seafood',
       'Singaporean', 'Vietnamese', 'Latin American', 'Healthy Food',
       'Cafe', 'Fast Food', 'Brazilian', 'Argentine', 'Arabian', 'Bakery',
       'Tex-Mex', 'Bar Food', 'International', 'French', 'Steak',
       'German', 'Sushi', 'Grill', 'Peruvian', 'North Eastern',
       'Ice Cream', 'Burger', 'Mexican', 'Vegetarian', 'Contemporary',
       'Desserts', 'Juices', 'Beverages', 'Spanish', 'Thai', 'Indian',
       'Mineira', 'BBQ', 'Mongolian', 'Portuguese', 'Greek', 'Asian',
       'Author', 'Gourmet Fast Food', 'Lebanese', 'Modern Australian',
       'African', 'Coffee and Tea', 'Australian', 'Middle Eastern',
       'Malaysian', 'Tapas', 'New American', 'Pub Food', 'Southern',
       'Diner', 'Donuts', 'Southwestern', 'Sandwich', 'Irish',
       'Mediterranean', 'Cafe Food', 'Korean BBQ', 'Fusion', 'Canadian',
       'Breakfast', 'Cajun', 'New Mexican', 'Belgian', 'Cuban', 'Taco',
       'Caribbean', 'Polish', 'Deli', 'British', 'nan', 'California',
       'Others', 'Eastern European', 'Creole', 'Ramen', 'Ukrainian',
       'Hawaiian', 'Patisserie', 'Yum Cha', 'Pacific Northwest', 'Tea',
       'Moroccan', 'Burmese', 'Dim Sum', 'Crepes', 'Fish and Chips',
       'Russian', 'Continental', 'South Indian', 'North Indian', 'Salad',
       'Finger Food', 'Mandi', 'Turkish', 'Kerala', 'Pakistani',
       'Biryani', 'Street Food', 'Nepalese', 'Goan', 'Iranian', 'Mughlai',
       'Rajasthani', 'Mithai', 'Maharashtrian', 'Gujarati', 'Rolls',
       'Momos', 'Parsi', 'Modern Indian', 'Andhra', 'Tibetan', 'Kebab',
       'Chettinad', 'Bengali', 'Assamese', 'Naga', 'Hyderabadi', 'Awadhi',
       'Afghan', 'Lucknowi', 'Charcoal Chicken', 'Mangalorean',
       'Egyptian', 'Malwani', 'Armenian', 'Roast Chicken', 'Indonesian',
       'Western', 'Dimsum', 'Sunda', 'Kiwi', 'Asian Fusion', 'Pan Asian',
       'Balti', 'Scottish', 'Cantonese', 'Sri Lankan', 'Khaleeji',
       'South African', 'Drinks Only', 'Durban', 'World Cuisine',
       'Izgara', 'Home-made', 'Giblets', 'Fresh Fish', 'Restaurant Cafe',
       'Kumpir', 'Döner', 'Turkish Pizza', 'Ottoman', 'Old Turkish Bars',
       'Kokoreç'])

cuisines_selection = df1['cuisines'].isin(cuisines_select)
df1 = df1.loc[cuisines_selection, :].reset_index()


# ==============================================================================================
# Streamlit Layout
# ==============================================================================================


with st.container():
    
    # Top restaurants with the highest rating
    st.markdown('### Top restaurants with the highest rating')
    
    graph = top_biggest_restaurants(df1)
    st.plotly_chart(graph, use_container_width = True)
    
    st.markdown("""---""")
    
with st.container():
    
    col1, col2 = st.columns(2)
    
    with col1:
        
        # Top best cuisine types
        st.markdown('##### Top 100 best cuisine types ratings')
        
        cuisines = top_cuisines(df1, ascending = False)
        st.dataframe(cuisines)
        
    with col2:
        
        # Top worst cuisine types
        st.markdown('##### Top 100 worst cuisine types ratings')
        
        cuisines = top_cuisines(df1, ascending = True)
        st.dataframe(cuisines)
