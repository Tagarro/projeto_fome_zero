import pandas as pd
import inflection
import plotly.express as px
import folium
import streamlit as st
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium, folium_static
from PIL import Image


st.set_page_config(page_title = 'Countries', page_icon = '🌎', layout = 'wide')

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

country_select = st.sidebar.multiselect('Select the countries: ', ['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada', 'Singapure', 'United Arab Emirates', 'India', 'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey'], default = ['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada', 'Singapure', 'United Arab Emirates', 'India', 'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey'])

countries_selection = df1['country'].isin(country_select)
df1 = df1.loc[countries_selection, :].reset_index()




# ==============================================================================================
# Streamlit Layout
# ==============================================================================================



with st.container():
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        
        # Most cities registered
        aux = df1.loc[:, ['city', 'country']].groupby(['country']).nunique().sort_values(['city'], ascending = False).reset_index().iloc[0,0]
        st.metric('Most cities registered', aux)
        
    with col2:
        
        # Most voted
        aux = df1.loc[:, ['votes', 'country']].groupby('country').sum().sort_values('votes', ascending = False).reset_index().iloc[0,0]
        col2.metric('Most voted', aux)
        
    with col3:
        
        # Country with most cuisines
        aux = df1.loc[:, ['cuisines', 'country']].groupby('country').nunique().sort_values('cuisines', ascending = False).reset_index().iloc[0,0]
        col3.metric('Country with most cuisines', aux)
        
    with col4:
        
        # Biggest rating mean        
        aux = df1.loc[:, ['aggregate_rating', 'country']].groupby('country').mean().sort_values('aggregate_rating', ascending = False).reset_index().iloc[0,0]
        col4.metric('Biggest rating mean', aux)

st.markdown("""---""")
        
with st.container():
    
    # Registered cities by countries chart
    st.markdown("### Registered cities by countries chart")
    
    aux = df1.loc[:, ['city', 'country']].groupby(['country']).nunique().sort_values(['city'], ascending = False).reset_index()
    graph = px.bar(aux, x = 'country', y = 'city')
    st.plotly_chart(graph, use_container_width = True)
    
    st.markdown("""---""")
    
with st.container():
    
    # Registered restaurants by countries chart
    st.markdown("### Registered restaurants by countries chart")
    
    aux = df1.loc[:, ['country', 'restaurant_id']].groupby('country').count().sort_values(['restaurant_id'], ascending = False).reset_index()
    graph = px.bar(aux, x = 'country', y = 'restaurant_id')
    st.plotly_chart(graph, use_container_width = True)
    
    st.markdown("""---""")
    
with st.container():
    
    col1, col2 = st.columns(2)
    
    with col1:
        
        # Votes quantity by country chart
        st.markdown("#### Votes quantity by country chart")
        
        aux = df1.loc[:, ['votes', 'country']].groupby('country').sum().sort_values('votes', ascending = False).reset_index()
        graph = px.bar(aux, x = 'country', y = 'votes')
        st.plotly_chart(graph, use_container_width = True)
        
    with col2:
        
        # Rating mean by country chart
        st.markdown("#### Rating mean by country chart")
        
        aux = df1.loc[:, ['aggregate_rating', 'country']].groupby('country').mean().sort_values('aggregate_rating', ascending = False).reset_index()
        graph = px.bar(aux, x = 'country', y = 'aggregate_rating')
        st.plotly_chart(graph, use_container_width = True)