import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header("Zena's Amazing Catalog")
streamlit.text('Pick a sweatsuit colour or style') 

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake2"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from catalog_for_website")
colours = my_cur.fetchall()
# my_cnx.close() 

streamlit.dataframe(colours) 

colours = colours.set_index([0])
streamlit.multiselect("Choose colour:", list(colours.index), ['Pink'] )
