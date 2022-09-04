import streamlit as st
import pandas as pd
# import requests
import snowflake.connector
# from urllib.error import URLError

st.title("Zena's Amazing Catalog")

#connect Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake2"])
my_cur = my_cnx.cursor()
#execute color
my_cur.execute("SELECT COLOR_OR_STYLE, PRICE from catalog_for_website") # to jest zaimportowane ze snowflake jako tupla
colours = my_cur.fetchall() #colours to tupla

st.text('data from Snowflake')
st.text(colours)

st.text('Put data into st.dataframe')
st.dataframe(colours)
 
st.text('Put data into pd.DataFrame')
df = pd.DataFrame(colours)
st.text(df)

# streamlit.selectbox('Choose colour:', list(colours))


st.text('our warm, comf /pink/ sweatuit')



my_cnx.close() 
