import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header("Zena's Amazing Catalog")
streamlit.text('Pick a sweatsuit colour or style') 

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake2"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT COLOR_OR_STYLE from catalog_for_website")
colours = my_cur.fetchall()
my_cnx.close() 

#streamlit.dataframe(colours) 
streamlit.select("Choose colour:", list(colours))


streamlit.text('our warm')
