import streamlit as st
import pandas as pd
# import requests
import snowflake.connector
# from urllib.error import URLError

st.title("Zena's Amazing Catalog")

#connect Snowflake
my_cnx = snowflake.connector.connect(**st.secrets["snowflake2"])
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

st.text('selectbox')
st.selectbox('Choose colour:', list(colours))
st.text('selectbox df')
st.selectbox('Choose colour:', list(df))
st.write(df)

# st.text('multiselect colour')
# st.multiselect("Pick colour:", list(colours) )
# st.text('multiselect colour df')
# st.multiselect("Pick colour:", list(df) )
 
st.text('our warm, comf /pink/ sweatuit')



my_cnx.close() 
