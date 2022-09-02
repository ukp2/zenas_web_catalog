import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header("Zena's Amazing Catalog")
streamlit.text('Pick a sweatsuit colour or style') 


# streamlit.text("Snowflake metadata:")
# streamlit.text(my_data_row_0)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake2"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT color_or_style from catalog_for_website")
colour_list = my_cur.fetchall()

streamlit.multiselect("Pick colour:", list(colour_list.index),['Pink'])
