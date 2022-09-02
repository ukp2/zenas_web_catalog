import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header("Zena's Amazing Catalog")
streamlit.text('Pick a sweatsuit colour or style') 

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake2"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT color_or_style from catalog_for_website")
colour_list = my_cur.fetchall()
# my_cnx.close() 

streamlit.dataframe(colour_list) 

# colour_list = colour_list.set_index('color_or_style')

streamlit.multiselect("Pick colour:", list(colour_list, ['Pink'])
