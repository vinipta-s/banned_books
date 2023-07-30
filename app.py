
import streamlit as st
import pandas as pd
import plotly.express as px

from abbrev import us_state_to_abbrev




## read in data 
banned_books_data = pd.read_csv("datasets/PEN America's Index of School Book Bans (July 1, 2021 - June 30, 2022) - Sorted by Author & Title.csv", skiprows=2)            

# column names need to be snake_case format: lowercase, and spaces replaced with _
banned_books_data.columns = banned_books_data.columns.str.lower()
banned_books_data.columns = banned_books_data.columns.str.replace(' ', '_')

# convert date_of_challenge/removal from object to DateTime type
banned_books_data['date_of_challenge/removal'] = pd.to_datetime(banned_books_data['date_of_challenge/removal'], format='%B %Y')

### column with abrevitated states 
banned_books_data['state_abbrev'] = banned_books_data['state'].map(us_state_to_abbrev)

st.dataframe(banned_books_data)

title_bans_by_district = banned_books_data.groupby(['state_abbrev', 'district'])['title'].count().sort_values(ascending=False).reset_index()

fig = px.choropleth(title_bans_by_district,
                    locations='state_abbrev', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='title',
                    #range_color=(0, 500),
                    #color_discrete_sequence="Viridis_r", 
                    title='test',
                    
                    )

st.write(fig)



